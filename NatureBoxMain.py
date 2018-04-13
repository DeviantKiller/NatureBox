#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import modules
import RPi.GPIO as GPIO ##Main GPIO module
##import time ##Import time module (apparently not used)
from datetime import datetime ## Date and time module for file-saving
from time import sleep ## Used to control sleep command
import picamera # May not be required yet.
import os # Allows for running of os commands.
import sys
import smtplib # Used for SMTP connection
from email.MIMEText import MIMEText # Used for e-mail
from email.MIMEMultipart import MIMEMultipart ## Used for e-mail
from email.MIMEImage import MIMEImage ## Used for e-mail
##import socks ## Used for proxy
print("Modules imported...")

print("Setting up GPIOs...")
GPIO.setmode(GPIO.BCM) ## Sets GPIO mode as BCM/Broadcom
print("GPIO mode set to Broadcom...")
GPIO.setwarnings(False) # 
GPIO.setup(18, GPIO.IN,pull_up_down=GPIO.PUD_UP)
print("Pin 18 configured as input...")
GPIO.setup(23, GPIO.OUT) ##RED
print("Pin 23 configured as output...")
print("Testing Pin 23 (RED LED)...")
GPIO.output(23, GPIO.HIGH)
sleep(0.2)
GPIO.output(23, GPIO.LOW)
GPIO.setup(24, GPIO.OUT) ##GREEN
print("Pin 24 configured as output...")
GPIO.output(24, GPIO.HIGH)
print("Enable Green LED...")
print("Ready to Capture...")

#Attempt at making find Camera/Pi location and sorting by Earliest created size
def imageSort():
    directory = '/home/pi/Pictures/Camera/'
    os.chdir(directory)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    
    oldest = files[0]
    newest = files[-1]
   
##    print "Oldest:", oldest
##    print "Newest:", newest
##    print "Oldest full path:", directory+newest
##    print "All by modified oldest to newest:", files
    
    return newest

#Attempt of making image save and rename
def takingStill():
    utcDateTime = datetime.utcnow()
    utcDate = utcDateTime.strftime ("%Y-%m-%d")
    utcDay = utcDateTime.strftime ("%A")
    utcTime = utcDateTime.strftime ("%H:%M:%S")
    fileName = 'IMG_' +utcDate+ '-' +utcTime+ '.jpg'
    filePath = '/home/pi/Pictures/Camera/'
    os.system('raspistill -o ' +filePath+ '' + fileName + ' -t 1')
    ## print("Your file is called " +fileName+". It has been saved to "+filePath+". ") ## Old Print
    print("Your file is called \033[1;34m" +fileName+"\033[0;0m. It has been saved to \033[1;34m"+filePath+"\033[0;0m.")

# Create a Function for buttons detection
def pressScan():
    while True:
        input_value = GPIO.input(18)
        if input_value == False:
            print("Who pressed my button!")
            GPIO.output(23, GPIO.HIGH) ## Turns red on 
            GPIO.output(24, GPIO.LOW) ## Turns green off
            print("Preparing E-mail...")
            takingStill()
        
            # Emails
            strFrom = 'YOUR@domain.com'
            strTo = ['exmaple@gmail.com', 'example@virginmedia.com']
        
            #Create Root message and fill in the form from, to, and subject headers   
            msgRoot = MIMEMultipart('related')
            msgRoot['from'] = strFrom
            msgRoot['to'] = strFrom
            msgRoot['cc'] = ", ".join(strTo)
            msgRoot['subject'] = 'Rpi test - natureBoxMain.PY'
            msgRoot.preamble = 'Did someone press a button?'
        
            # Encapsulate the plain and HTML versions of the body in an
            # 'alternative' part so message agents can decide which they want to display
            msgAlternative = MIMEMultipart('alternative')
            msgRoot.attach(msgAlternative)
        
            msgText = MIMEText('This is alternative Plain Text Message')
            msgAlternative.attach(msgText)
        
            #Set up
            utcDateTime = datetime.utcnow()
            utcDate = utcDateTime.strftime ("%Y-%m-%d")
            utcDay = utcDateTime.strftime ("%A")
            utcTime = utcDateTime.strftime ("%H:%M:%S")
            
            # We reference the image in the IMG SRC attribute by the ID we give it below
            msgText = MIMEText('<b>The date is '+utcDate+' <br>And the time is ' +utcTime+ '.<br>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>Nifty!', 'html')
            msgAlternative.attach(msgText)
            
            # Call the ImageSort function and email file
            imageSort()
            newestImage = imageSort()
            # This example assumes the image is in the current directory
            fp = open(newestImage, 'rb')
            print ("using image:" +newestImage+ ".")
            msgImage = MIMEImage(fp.read())
            fp.close()

            # Define the image's ID as referenced above
            msgImage.add_header('Content-ID', '<image1>')
            msgRoot.attach(msgImage)
            
            # Proxy if required. Otherwise comment out
            #socks.setdefaultproxy(TYPE, ADDR, PORT)
            ##socks.setdefaultproxy(socks.SOCKS5, 'IP of proxy', Port8080)
            ##socks.wrapmodule(smtplib)
            
            ##Encrypt
            smtp = smtplib.SMTP()
            smtp.connect('smtp.gmail.com')
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
        
            # Send the email (this example assumes SMTP authentication is required)
        
            smtp.login('YOURLOGIN@gmail.com', 'Password')
            smtp.sendmail(strFrom, strTo, msgRoot.as_string())
            smtp.quit()
        
            print("msgRoot.as_string()")
            print("E-mail sent.")
            print("Starting Video feed for 10 seconds")
            os.system('raspivid -t 10000 -vf -w 1920 -h 1080 -fps 30 -b 4000000 -g 50')
            #10 sec local stream for testing
            print("Video stream finished")
            while input_value == False:
                input_value = GPIO.input(18)
            print("Waiting!")
            GPIO.output(23, GPIO.LOW) # Turns red off
            GPIO.output(24, GPIO.HIGH) # Leaves green on
        sleep(0.2);
 
if __name__ == '__main__':
    try:
        pressScan()
    except (KeyboardInterrupt, SystemExit):
        print("You have Ended the script!")
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.cleanup()

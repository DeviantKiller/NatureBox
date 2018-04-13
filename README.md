<b><h1><u>Dans natureBox</u></h1></b><br><br>

This is a small project i have set up in order to expand my coding knowledge and learn to use a raspberry pi and python.
I have not made a script prior to this and have started from LED's, addind a switch, and then building up to a complete project.<br>

When finished, i hope to have a fully operation Nature box, that will detect motion, trigger and e-mail to be sent notifiying recipients of movement with an attached image of the cause, and stream to youtube and/or save locally/to a dropbox location/to a NAS.<br><br> 
<h2><u>Small project for Motion detector/IR camera nature box.</u></h2><br><br>

The Box will (when complete): <br>
Set GPIO mode to BCM <br>
-  Setup GPIO output pins 23 (RED) and 24 (Green)<br>
-  setup GPIO input pin 18<br>
-  Wait in ready until something triggers GPIO.IN (18) - will be motion detector<br>
   - GPIO18 - Currently set up as tactile switch for manual testing purposes.<br>
-  When triggered Green LED will go LOW and RED LED will go HIGH<br>
-  Calls funtion (takingStill)<br>
   - Taking still uses import time to create a filename based on Date + Time<br>
   - Saves image as IMG_<utcDate>-<utcTime>.jpg<br>
-  Creates MIME form for email<br>
-    strFrom = Sent by and send email to<br>
-    strTo = Who to send to (these will be CC'd)<br>
-    Sets subject, preamble and alternative message with HTML body.<br>
     - Calls the imageSort() function which pulls latest file from set directory within function<br>
-    attachs newestImage to HTML body<br><br>
   
   ## To Do
   - [x] Setup basic script with LEDS <br>
   - [x] Setup Pushbutton to control LEDS (turn off GREEN aand turn on RED) <br>
   - [x] Add PiCamera and local stream on button press <br>
   - [x] Added e-mail capability using smtplib and MIMEText <br>
   - [x] Added MIMEMultipart and HTML body to e-mail <br>
   - [x] Aded attachement to e-maail body <br>
   - [x] Added image capture using raspistill <br>
   - [x] Created Function to name image taken based on Date+Time and save to Camera location. <br>
   - [x] Created Function to find latest created file in Camera location and return it as a variable. <br>
   - [x] Changed location of image attached to e-mail from current working directory to imageSort() value. <br>

   - [ ] Setup GPIO input for exiting code and shutting down pi. <br>
   - [ ] Add in functionality for starting a saved local stream <br>
   - [ ] Add start liveStream capability to stream to Youtube when motion is detected. <br>
   

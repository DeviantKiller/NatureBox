Dans natureBox<br>
Small project for Motion detector/IR camera nature box.
The Box will (when complete): 
  Set GPIO mode to BCM 
  Setup GPIO output pins 23 (RED) and 24 (Green)
  setup GPIO input pin 18
  Wait in ready until something triggers GPIO.IN (18) - will be motion detector
    GPIO18 - Currently set up as tactile switch for manual testing purposes.
  When triggered Green LED will go LOW and RED LED will go HIGH
  Calls funtion (takingStill)
    Taking still uses import time to create a filename based on Date + Time
    Saves image as IMG_<utcDate>-<utcTime>.jpg
  Creates MIME form for email
    strFrom = Sent by and send email to
    strTo = Who to send to (these will be CC'd)
    Sets subject, preamble and alternative message with HTML body.
      Calls the imageSort() function which pulls latest file from set directory within function
    attachs newestImage to HTML body

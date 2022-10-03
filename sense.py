import RPi.GPIO as GPIO
import time
import feed_me_through_the_phone as phone
from twilio.rest import Client 

GPIO.setmode(GPIO.BCM)

trigger = 17
echo = 27

GPIO.setup(trigger,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

def get_distance():
    
    #push trigger
    GPIO.output(trigger, True)
    time.sleep(0.00001)
    GPIO.output(trigger,False)

    pulse_start = time.time()
    pulse_end = time.time()
    
    #listen
    while GPIO.input(echo) == 0:
        pulse_start = time.time()
      
    while GPIO.input(echo) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    return (pulse_duration * 34300) / 2



#Start a Twilio / WhatsApp client
client = phone.start_client()

#6 hour grace period in seconds
GRACE_PERIOD = 21600
hourglass = time.time()
alerted = False

while True:
    GPIO.output(trigger, False)
    time.sleep(1)
    
    distance = get_distance()
    
    #alert if we haven't in the last 6 hours
    if distance >= 24:
        time_now = time.time()
        
        #handle case where first alert is within grace period... prob a better way to do this
        if alerted == False:
            phone.send_alert_msg(client)
            hourglass = time_now
            alerted = True
            
        elif (hourglass - time_now) >= GRACE_PERIOD:
            phone.send_alert_msg(client)
            hourglass = time_now
    
    print ("Distance = %.1f cm" % distance)


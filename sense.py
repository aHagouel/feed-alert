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
CONTAINER_LENGTH = 24
ANOMALY = 5
hourglass = time.time()
alerted = False
prev_distance = 24

while True:
    GPIO.output(trigger, False)
    time.sleep(2)
   
    distance = get_distance()
    
    #ignore any large changes in signal, e.g. when opening lid / feeding for an extended period of time 
    #change in food size is 1 cup every 12 hours, which should be less than 5cm between any two readings
    #don't care about distances becoming much smaller than 24cm
    if distance - prev_distance > ANOMALY:
        continue
    
    #alert if feed distance container length and we haven't in the last 6 hours
    elif distance >= CONTAINER_LENGTH:
        time_now = time.time()
        
        #handle case where first alert is within grace period... prob a better way to do this
        if alerted == False:
            phone.send_alert_msg(client)
            hourglass = time_now
            alerted = True
            
        elif (hourglass - time_now) >= GRACE_PERIOD:
            phone.send_alert_msg(client)
            hourglass = time_now
            
    prev_distance = distance
    
    print ("Distance = %.1f cm" % distance)


import RPi.GPIO as GPIO
import time
import feed_me_through_the_phone as phone
from twilio.rest import Client 

#RaspberryPi config
trigger = 17
echo = 27
GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)

#Container & alerting config
GRACE_PERIOD = 21600
CONTAINER_LENGTH = 30
CRITICAL = 0.01
ANOMALY = 5

#Start a Twilio / WhatsApp client
client = phone.start_client()

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


def calculate_fullness(length=CONTAINER_LENGTH, distance):
    return (1.0-(distance / length))
    

#Execute alerting logic 
hourglass = time.time()
alerts = 0
alerted = False
prev_distance = 30

while True:
    GPIO.output(trigger, False)
    time.sleep(2)
   
    distance = get_distance()
    fullness = calculate_fullness(CONTAINER_LENGTH,distance)
    
    #ignore any large changes in signal, e.g. when opening lid / feeding for an extended period of time 
    #change in food size is 1 cup every 12 hours, which should be less than 5cm between any two readings
    #don't care about distances becoming much smaller than 24cm
    if (distance - prev_distance) > ANOMALY:
        print('Anomaly detected: distance measured at ', distance ,'while previous distance measured at ', prev_distance, '. \n Skipping measurement')
        continue
    
    #alert if feed distance container length and we haven't in the last 6 hours
    elif fullness <= CRITICAL:
        time_now = time.time()
        time_since_last_alert = time_now - hourglass
        
        #handle case where first alert is within grace period... prob a better way to do this
        if alerted == False:
            alerts += 1
            print('Threshold passed with current distance of ', distance, 'and a previous distance of ', prev_distance, '. Alert count: ', alerts)
            phone.send_alert_msg(client)
            hourglass = time_now
            alerted = True
            
        elif time_since_last_alert >= GRACE_PERIOD:
            alerts += 1
            print('Threshold passed with current distance of ', distance, 'and a previous distance of ', prev_distance, '. Previous alert: ', time_since_last_alert, 'Alert count: ', alerts)
            phone.send_alert_msg(client)
            hourglass = time_now
            
        elif time_since_last_alert <= GRACE_PERIOD:
            print('Threshold above maximum distance but within grace period. No alert sent')
            
    prev_distance = distance
    
    print ("Feed measured at", distance, "cm, representing a hopper that is ", fullness*100,"% full.")
    
    

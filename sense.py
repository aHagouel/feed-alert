import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

trigger = 23
echo = 24

GPIO.setup(trigger,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)


def get_distance():
    
    GPIO.output(trigger, False)
    time.sleep(2)

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


while True:
    distance = get_distance()
    print ("Distance = %.1f cm" % distance)
import RPi.GPIO as GPIO
from time import sleep 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(25, GPIO.IN)
led=19
GPIO.setup(led, GPIO.OUT)


while True:
    sensor=GPIO.input(25) #this takes input from sensor

    if sensor==0:   #white
        GPIO.output(led, 0)
        sleep(0.1)
    
    else:           #black
        GPIO.output(led, 1)
        
    
    
import RPi.GPIO as GPIO
from time import sleep 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(25, GPIO.IN)
led=19
GPIO.setup(led, GPIO.OUT)
sensor=GPIO.input(25) #this takes input from sensor
count=0

def counterup(a): 
    global count
    if GPIO.input(a) == 0:
        count += 1
            
    else:
        count += 0
                  
    print(count)

GPIO.add_event_detect(25, GPIO.FALLING, callback = counterup)
while True:
    sensor1=sensor
    if sensor1==0:   #white
        GPIO.output(led, 0)
        sleep(0.1)
    
    else:           #black
        GPIO.output(led, 1)
        
    #GPIO.add_event_detect(25, GPIO.FALLING, callback = counterup)
        
    #GPIO.add_event_detect(25, GPIO.FALLING)
    
    #if GPIO.event_detected(25):
    #    print("rising edge")
    #else:
    #    print("falling edge")
    
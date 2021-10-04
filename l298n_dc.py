# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import RPi.GPIO as GPIO          
from time import sleep

## defining which pins to use
in1 = 24  ## << connect to in1 on your motor board
in2 = 23  ## << connect to in2 on your motor board
en  = 25  ## << connect to the enable A pin on your motor board

temp1=1

##
GPIO.setmode(GPIO.BCM)

## this is setting the GPIO pins defined above
##   to be output pins (for writting)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
##   GPIO.IN would be reading , like from a sensor


## initially set in1 (pin-24) and in2 (pin-23) to low
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

## set pin-25 as pulse with modulation with a frequency of 1000 pulses
##   GPIO.PWM(output channel , frequency of PWM signal)
##   see https://circuitdigest.com/microcontroller-projects/raspberry-pi-pwm-tutorial
p=GPIO.PWM(en,1000)

## this sets the duty cycle or ration of on to off pulse
##   i think that this sets the speed
##   so 25 or 25% should be slow
##   then 100 would be fast
p.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):

    x=raw_input()
    
    if x=='r':
        print("run")
        if(temp1==1):
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         print("forward")
         x='z'
        else:
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         print("backward")
         x='z'


    elif x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        temp1=1
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        temp1=0
        x='z'

    elif x=='l':
        print("low")
        p.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        p.ChangeDutyCycle(50)
        x='z'

    elif x=='h':
        print("high")
        p.ChangeDutyCycle(75)
        x='z'
     
    
    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")

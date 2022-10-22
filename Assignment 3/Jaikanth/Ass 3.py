                 Traffic Light
from gpiozero import LED
from time import sleep
red= LED(17)                      #pin numbers connected to Led's
aster=(22)
green=(27)
while True:
    red.on()                      #RED light
    print("Red light is ON")
    for i in range(100,0,-1):
        print("Remaining time: ",i)
        sleep(1)
    red.off()
    aster.on()                   # ASTER light
    print("Yellow light is ON")
    for i in range(5,0,-1):
        print("Remaining time: ",i)
        sleep(1)
    aster.off()
    green.on                     #GREEN light
    print("Green light is ON")
    for i in range(30,0,-1):
        print("Remaining time: ",i)
        sleep(1)
    green.off()
                                                 Blink LED
      import RPi.GPIO as GP
from time import sleep
GP.setwarnings(False)
GP.setmode(GP.BOARD)
GP.setup(8,GP.OUT,initial=GP.LOW)
while True:                      #infinite loop
    GP.output(8, GPIO.HIGH)               # Turn on
    print("The LED is ON")
    sleep(2)                     # Sleep for 2 second

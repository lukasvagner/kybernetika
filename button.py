from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)
button = Pin(15, Pin.IN, Pin.PULL_DOWN)

while True:
    
    if button.value() == 1:
        led.toggle()
        print(button.value)
        sleep(0.01)
        while button.value() == 1:
            sleep(0.01)
        """
        led.on()
        sleep(0.1)
        
    else:
        led.off()
"""

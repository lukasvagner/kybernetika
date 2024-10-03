import machine
import time

# Initialize the onboard LED (usually GPIO2)
led = machine.Pin(2, machine.Pin.OUT)

while True:
    print("Hello, World!")
    time.sleep(1)
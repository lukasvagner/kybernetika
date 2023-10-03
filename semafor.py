import umachine
import utime
 
 led = umachine.pin(25, umachine.Pin.OUT)

while True:
    led.togle()
    utime.sleep(1)
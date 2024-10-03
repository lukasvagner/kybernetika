from machine import Pin
from time import sleep

# Pin Definitions
latch_pin = Pin(15, Pin.OUT)  # D2 (GPIO 4) - Connected to RCLK
clock_pin = Pin(4, Pin.OUT)  # D1 (GPIO 5) - Connected to SRCLK
data_pin  = Pin(5, Pin.OUT)  # D3 (GPIO 0) - Connected to SER

buzzer_pin = Pin(3, Pin.OUT)  # D3 (GPIO 0) - Connected to the buzzer

def shift_out(data):
    """Shift out 8 bits to the 74HC595 shift register."""
    for i in range(8):
        # Get the current bit
        bit = (data >> (7 - i)) & 1  # Extract the bit
        data_pin.value(bit)           # Send the bit to the shift register
        clock_pin.value(1)            # Pulse the clock to shift the bit
        clock_pin.value(0)            # Reset clock

def write_to_shift_register(data):
    """Write data to the shift register."""
    latch_pin.value(0)              # Prepare to send data
    shift_out(data)                 # Send data to the shift register
    latch_pin.value(1)              # Lock in the data

write_to_shift_register(0b00000001)  # Turn on QA (Q0)

# Main loop
while True:
    buzzer_pin.value(1)            # Turn on the buzzer
    sleep(1)                       # Wait for 1 second
    buzzer_pin.value(0)            # Turn off the buzzer
    sleep(1)                       # Wait for 1 second
    

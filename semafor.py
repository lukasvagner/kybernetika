from machine import Pin
from time import sleep

pin = Pin(25, Pin.OUT)

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', ' ': '/'
}

def latin_to_morse(text):
    morse_code = ""
    for char in text:
        if char.upper() in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char.upper()] + " "
        else:
            morse_code += " "

    return morse_code

def blink_morse_code(morse_code):
    for symbol in morse_code:
        if symbol == ".":
            pin.on()
            sleep(0.2)
            pin.off()
            sleep(0.2)
        elif symbol == "-":
            pin.on()
            sleep(0.6)
            pin.off()
            sleep(0.2)
        elif symbol == " ":
            sleep(0.4)

while True:
    text = input("Enter text to convert to Morse code: ")
    morse_code = latin_to_morse(text)
    print(morse_code)
    blink_morse_code(morse_code)
    sleep(1)

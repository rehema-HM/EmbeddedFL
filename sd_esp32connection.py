# Create a text file and write running numbers.
# Open text file, read and print the content on debug port
   
# The ESP32 pin connections for MicroSD Card Adapter SPI
 
# MicroSD Card Adapter Power Pins
# MicroSD VCC pin to ESP32 +5V
# MicroSD GND pin to ESP32 GND
 
# MicroSD SPI Pins
# MicroSD MISO pin to ESP32 GPIO13
# MicroSD MOSI pin to ESP32 GPIO12
# MicroSD SCK pin to ESP32 GPIO14
# MicroSD CS pin to ESP32 GPIO27
 
# Name:- M.Pugazhendi
# Date:-  20thOct2021
# Version:- V0.1
# e-mail:- muthuswamy.pugazhendi@gmail.com

import machine
from machine import Pin, SPI, SoftSPI
import sdcard
import os
 
toggle = 0
 
# Initialize the onboard LED as output
led = machine.Pin(2, machine.Pin.OUT)

# Toggle LED functionality
def BlinkLED(timer_one):
    global toggle
    if toggle == 1:
        led.value(0)
        toggle = 0
    else:
        led.value(1)
        toggle = 1

# Initialize the SD card
spi = SoftSPI(1, sck=Pin(18), mosi=Pin(23), miso=Pin(19))
sd = sdcard.SDCard(spi, Pin(5))

# Create an instance of MicroPython Unix-like Virtual File System (VFS)
vfs = os.VfsFat(sd)
 
# Mount the SD card
os.mount(sd, '/sd')

# Debug print SD card directory and files
print(os.listdir('/sd'))

# Create / Open a file in write mode.
# Write mode creates a new file.
# If a file already exists, it overwrites the file.
file = open("/sd/sample.txt", "w")

# Write sample text
for i in range(20):
    file.write("Sample text = %s\r\n" % i)
    
# Close the file
file.close()

# Again, open the file in "append mode" for appending a line
file = open("/sd/sample.txt", "a")
file.write("Appended Sample Text at the END \n")
file.close()

# Open the file in "read mode". 
# Read the file and print the text on debug port.
file = open("/sd/sample.txt", "r")
if file != 0:
    print("Reading from SD card")
    read_data = file.read()
    print(read_data)
file.close()

# Initialize timer_one. Used for toggling the onboard LED
timer_one = machine.Timer(0)

# Timer one initialization for onboard blinking LED at 200mS interval
timer_one.init(freq=5, mode=machine.Timer.PERIODIC, callback=BlinkLED)

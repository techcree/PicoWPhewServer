# Lets blink LEDs conected with your Raspberry Pi Pico by SKANTA (TechCree) 
import machine
from machine import Pin
import utime

led25 =  Pin(25, Pin.OUT) #mainboard 
ledrot =  Pin(2, Pin.OUT)
ledblau =  Pin(14, Pin.OUT)


led25.value(0)
ledrot.value(0)
ledblau.value(0)



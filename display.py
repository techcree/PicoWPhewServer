#by 838375 V4.1 - Temperaturmessung und Anzeige mit Display und RGB LEDs
import machine 
import utime
import picodisplay
from machine import ADC #Mainboard Sensor
from machine import Pin
import picodisplay as display # Pico Display boilerplate
import time, random
import gc

# Display Setting
width = display.get_width()
height = display.get_height()
display_buffer = bytearray(width * height * 2)
display.init(display_buffer)
display.set_backlight(0.5)

# Setup Temperaturmessung und Konvertierung
sensor_temp = machine.ADC(4) 
conversion_factor = 3.3 / (65535) 
display.set_backlight(0.5)

# sets up a handy function we can call to clear the screen

display.set_pen(0, 0, 0)
display.clear()
display.update()
    
display.set_pen(0, 0, 139)
display.rectangle(0, 0, 300, 140)
display.set_pen(255, 255, 255)
display.text("IP Adresse", 10, 15, 0, 3)
#display.text((netConfig), 10, 30, 0, 7)
display.update()
#        utime.sleep(3)
        

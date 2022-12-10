# Lets blink LEDs conected with your Raspberry Pi Pico by SKANTA (TechCree) 
import machine
from machine import Pin
import utime

led25 =  Pin(25, Pin.OUT) #mainboard 
ledrot =  Pin(2, Pin.OUT)
ledblau =  Pin(14, Pin.OUT)

#startseqenz onboard led blinkt

counta = 0

while counta < 2:
    led25.value(1)
    utime.sleep(0.5)
    led25.value(0)
    utime.sleep(1)
    
    counta = counta +1
    
    pass


#rote led blinken wlan verbindung herstellen

countb = 0

while countb < 6:
    ledrot.value(1)
    utime.sleep(0.5)
    ledrot.value(0)
    utime.sleep(0.3)
    
    countb = countb +1
    
    pass

countc = 0

#while countc < 2:
#    ledblau.value(1)
#    utime.sleep(0.1)
#    ledblau.value(0)
#    utime.sleep(1)
    
#    countb = countc +1
    
#    pass

ledblau.value(1)
#utime.sleep(10)
#ledblau.value(0)



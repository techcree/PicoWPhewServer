from phew import connect_to_wifi
from secret import ssid, password
import network
from time import sleep
import led

connect_to_wifi(ssid, password)

print("connected to wifi")
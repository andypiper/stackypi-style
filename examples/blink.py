# basic blink code
import machine
import utime

# status LED on GPIO 25
led = machine.Pin(25, machine.Pin.OUT)

while True:
    led.value(1)
    utime.sleep(1)
    led.value(0)
    utime.sleep(1)

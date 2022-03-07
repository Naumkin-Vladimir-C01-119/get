import RPi.GPIO as g
import time
leds = [21, 20, 16, 12, 7, 8, 25, 24]
g.setmode(g.BCM)
g.setup(leds, g.OUT)
for _ in range(3):
    for i in range(8):
        g.output(leds[i], 1)
        time.sleep(0.2)
        g.output(leds[i], 0)
g.output(leds, 0)
g.cleanup()
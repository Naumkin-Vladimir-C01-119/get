import RPi.GPIO as g
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
leds = [21, 20, 16, 12, 7, 8, 25, 24]
g.setmode(g.BCM)
g.setup(dac, g.OUT)
g.setup(leds, g.OUT)
g.setup(troyka, g.OUT, initial = g.HIGH)
g.setup(comp, g.IN)
def d2b(n):
    return [int(x) for x in bin(n)[2:].zfill(8)]
def adc():
    a = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        a[i] = 1
        g.output(dac, a)
        v = int("".join([str(x) for x in a]), 2) / 256 * 3.3
        time.sleep(0.01)
        if g.input(comp) == 0:
            a[i] = 0
    return [a, v]
    
try:
    while True:
        a = adc()
        print("Value = {:^3} -> {}, voltage = {:.2f}".format(int("".join([str(x) for x in a[0]]), 2), a[0], a[1]))
        x = a[1] * 8 / 3.3
        x = int(round(x, 0))
        l = [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(x):
            l[i] = 1
        l = l[::-1]
        g.output(leds, l)
finally:
    g.output(dac, 0)
    g.output(troyka, 0)
    g.cleanup()

import RPi.GPIO as g
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
g.setmode(g.BCM)
g.setup(dac, g.OUT)
g.setup(troyka, g.OUT, initial = g.HIGH)
g.setup(comp, g.IN)
def d2b(n):
    return [int(x) for x in bin(n)[2:].zfill(8)]
def adc():
    for i in range(256):
        g.output(dac, d2b(i))
        v = i / 256 * 3.3
        time.sleep(0.005)
        if g.input(comp) == 0:
            print("Value = {:^3} -> {}, voltage = {:.2f}".format(i, d2b(i), v))
            break
try:
    while True:
        adc()
finally:
    g.output(dac, 0)
    g.output(troyka, 0)
    g.cleanup()

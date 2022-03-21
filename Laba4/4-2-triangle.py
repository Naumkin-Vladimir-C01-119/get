import RPi.GPIO as g
import time
dac = [26, 19, 13, 6, 5, 11, 9, 10]
g.setmode(g.BCM)
g.setup(dac, g.OUT)
def d2b(n):
    return [int(x) for x in bin(n)[2:].zfill(8)]
try:
    print("Enter T")
    t = float(input())
    t = t / 2
    temp = t / 256
    while True:
        for i in range(256):
            g.output(dac, d2b(i))
            time.sleep(temp)
        for i in range(255, -1, -1):
            g.output(dac, d2b(i))
            time.sleep(temp)
finally:
    g.output(dac, 0)
    g.cleanup()

import RPi.GPIO as g
pin = 22
g.setmode(g.BCM)
g.setup(pin, g.OUT)
try:
    while True:
        dc = int(input("duty cycle\n"))
        u = 3.3 * dc / 100
        print("U = " + str(u))
        p = g.PWM(pin, 1000)
        p.start(dc)
        input("Press enter to change duty cycle")
        p.stop()
finally:
    g.output(pin, 0)
    g.cleanup()

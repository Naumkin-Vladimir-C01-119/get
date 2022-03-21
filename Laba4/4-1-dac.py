import RPi.GPIO as g
dac = [26, 19, 13, 6, 5, 11, 9, 10]
g.setmode(g.BCM)
g.setup(dac, g.OUT)
def d2b(n):
    return [int(x) for x in bin(n)[2:].zfill(8)]
def check_integer(x):
    try:
        _ = int(x)
        return 0
    except:
        return 1
try:
    print("Enter q to exit")
    while True:
        n = input()
        if n == 'q':
            break
        if check_integer(n):
            print("Incorrect input, isn't integer. Try again!")
            continue
        n = int(n)
        if n < 0:
            print("Only positive numbers. Try again!")
            continue
        if n > 255:
            print("Too big number, above 255. Try again!")
            continue
        u = (3.3 * n) / 256
        print("U = " + str(u))
        g.output(dac, d2b(n))
finally:
    g.output(dac, 0)
    g.cleanup()

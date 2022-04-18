#imports
import RPi.GPIO as g
import time
import matplotlib.pyplot as plt

#settings
dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17
g.setmode(g.BCM)
g.setup(dac, g.OUT)
g.setup(leds, g.OUT)
g.setup(troyka, g.OUT, initial = g.LOW)
g.setup(comp, g.IN)

#decimal to binary list
def d2b(n):
    return [int(x) for x in bin(n)[2:].zfill(8)]

#convert analog to digital
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

#main    
try:
    data = []
    t_start = time.time()

    #start measurements
    g.output(troyka, 1)
    print('Turn on')
    while True:
        a = adc()
        num = int("".join([str(x) for x in a[0]]), 2)
        data.append(num)
        g.output(leds, a[0])
        print("Value = {:^3} -> {}, voltage = {:.2f}".format(int("".join([str(x) for x in a[0]]), 2), a[0], a[1]))
        if num >= 245:
            print('Turn off')
            break
    
    #turn off voltage
    g.output(troyka, 0)
    while True:
        a = adc()
        num = int("".join([str(x) for x in a[0]]), 2)
        data.append(num)
        g.output(leds, a[0])
        print("Value = {:^3} -> {}, voltage = {:.2f}".format(int("".join([str(x) for x in a[0]]), 2), a[0], a[1]))
        if num <= 5:
            break
    
    #save time of measurements
    t_end = time.time()
    ti = t_end - t_start

#clean GPIO settings
finally:
    g.output(dac, 0)
    g.output(troyka, 0)
    g.output(leds, 0)
    g.cleanup()

#save in file
with open('data.txt', 'w') as save_data:
    save_data.write('\n'.join([str(x) for x in data]))
sample_freq = len(data) / ti
adc_step = 3.3 / 256
with open('settings.txt', 'w') as save_settings:
    save_settings.write('Sample frequency: ' + str(sample_freq) + ' hz\nADC quantum step: ' + str(adc_step) + ' v')

#print info to terminal
print(ti)
print(ti / len(data))
print(sample_freq)
print(adc_step)

#showing plot
plt.plot(data)
plt.show()

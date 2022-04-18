import matplotlib.pyplot as plt
with open('data.txt', 'r') as save_data:
    data = save_data.read().split()
data = [int(x) for x in data]
plt.plot(data)
plt.show()

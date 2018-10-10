import socket
import numpy as np
import pandas as pd
from scipy import pi
import matplotlib.pyplot as plt
from scipy import fftpack
from scipy import hamming
from scipy import signal
import matplotlib.animation as animation
import threading

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.43.184', 6783)
skt.bind(server_address)
N = 5
val_list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]
weights = np.ones(N) / N

skt.listen(1)

fig = plt.figure(num=1, figsize=(20, 8))
plt1 = fig.add_subplot(111)
plt2 = fig.add_subplot(212)

# data = pd.read_csv("../data_files/cup_temp.txt")

def animate(i):

    # data = pd.read_csv("../data_files/cup_temp.txt")
    plt1.clear()
    plt2.clear()
    data = np.convolve(val_list, weights, mode='valid')
    x = np.arange(data.size)
    grad = np.gradient(data, x)
    plt1.plot(data)
    plt2.plot(grad)


def listen_socket():
    print("waiting for a connection")
    connection, client_address = skt.accept()
    try:
        print('connection from', client_address)
        while True:
            try:
                data = connection.recv(16)
                val = float(data.decode("utf-8"));
                val_list.append(val)
                # np.insert(val_list, len(val_list)+1, float(data.decode("utf-8")))
                # print(data.decode("utf-8"))
                print(str(val))

                if len(val_list) > 128:
                    val_list.pop(0)
            except ValueError as e:
                print(str(e))


    finally:
        connection.close()


ani = animation.FuncAnimation(fig, animate, interval=100)
threading.Thread(target=listen_socket).start()
plt.show()
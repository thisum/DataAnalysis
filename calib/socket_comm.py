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
server_address = ('192.168.43.184', 9881)
skt.bind(server_address)

val_list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ]

skt.listen(1)

fig = plt.figure(num=1, figsize=(20, 8))
ax1 = fig.add_subplot(111)

# data = pd.read_csv("../data_files/cup_temp.txt")

def animate(i):

    # data = pd.read_csv("../data_files/cup_temp.txt")
    ax1.clear()
    f, t, Sxx = signal.spectrogram(np.asarray(val_list), fs=10, nperseg=16, noverlap=15, mode='psd')
    ax1.pcolormesh(t, f, Sxx)


def listen_socket():
    print("waiting for a connection")
    connection, client_address = skt.accept()
    try:
        print('connection from', client_address)
        while True:
            try:
                data = connection.recv(16)
                val_list.append(float(data.decode("utf-8")))
                # np.insert(val_list, len(val_list)+1, float(data.decode("utf-8")))
                print(str(len(val_list)) + " : " + str(val_list[0]))
                # print(str(float(data.decode("utf-8"))))

                if len(val_list) > 128:
                    val_list.pop(0)
            except ValueError as e:
                print(str(e))


    finally:
        connection.close()


ani = animation.FuncAnimation(fig, animate, interval=100)
threading.Thread(target=listen_socket).start()
plt.show()
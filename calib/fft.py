import numpy as np
import pandas as pd
from scipy import pi
import matplotlib.pyplot as plt
from scipy import fftpack
from scipy import hamming
from scipy import signal
import matplotlib.animation as animation

fig = plt.figure(num=1, figsize=(20, 8))
ax1 = fig.add_subplot(111)

# data = pd.read_csv("../data_files/cup_temp.txt")

def animate(i):

    data = pd.read_csv("../data_files/cup_temp.txt")
    ax1.clear()
    f, t, Sxx = signal.spectrogram(data.A[i:], fs=10, nperseg=16, noverlap=15, mode='psd')
    ax1.pcolormesh(t, f, Sxx)

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()

# f, t, Sxx = signal.spectrogram(data.B, fs=10, nperseg=16, noverlap=15, mode='psd')
# ax1.pcolormesh(t, f, Sxx)
# plt.title("16 frames")
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
# plt.show()
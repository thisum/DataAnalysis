import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
from scipy import fftpack
import os

N = 5
weights = np.ones(N)/N

#remove DC component

def process_signal(s, w, l, g_min, g_max):

    data_row = []
    conv_ker = np.ones(w)/w
    s = signal.convolve(s.real, [conv_ker], 'valid')
    for k in range(s.shape[1]-2):
        stats = calculate_stats(s[:,k], s[:,k+1])
        data_row.append(stats)
    data_row.append(g_min)
    data_row.append(g_max)
    appened_to_file('../new_data_processing/thisum/stats_grad_16_8_m.csv', data_row, l)

def calculate_stats(s1, s2):
    stats = []
    s1 = get_real_array(s1)
    s2 = get_real_array(s2)

    for e in s1:
        stats.append(e)

    stats.append(np.amin(s1))
    stats.append(np.amax(s1))
    stats.append(np.average(s1))
    stats.append(np.sum(s1))
    stats.append(np.std(s1))
    stats.append(np.median(s1))

    for e in (s2-s1):
        stats.append(e)

    stats.append(s1[0]/s1[1])
    stats.append(s1[0]/s1[2])
    stats.append(s1[0]/s1[3])
    # stats.append(s1[0]/s1[4])
    stats.append(s1[1]/s1[2])
    stats.append(s1[1]/s1[3])
    # stats.append(s1[1]/s1[4])
    stats.append(s1[2]/s1[3])
    # stats.append(s1[2]/s1[4])
    # stats.append(s1[3]/s1[4])

    return stats


def get_real_array(ar):
    list = []
    for j in range(len(ar)):
        list.append(ar[j].real)
    return np.array(list)

def appened_to_file(flie_name, list, pref):

    with open(flie_name, "a") as write_file:
        line = np.array2string(np.array(list), precision=2, separator=',', suppress_small=True)
        line = line.replace("[", "").replace("]", "").replace("\n", "").replace(" ", "")

        #if mean included
        line = line.replace("list(", "").replace(")", "")

        write_file.write(line + "," + pref + "\n" )


data = pd.read_csv("../new_data_processing/thisum/all.csv", header=None)
X = data.values[:, 0:43]
Y = data.values[:, 43]

gradients = []

avg_X = signal.convolve(X, [weights], 'valid')
for i in range(len(avg_X)):
    x = np.arange(avg_X[i].size)
    grad = np.gradient(avg_X[i], x)
    gradients.append(grad)

for i in range(len(gradients)):
    f, t, s = signal.spectrogram(gradients[i], fs=25, nperseg=16, noverlap=15, mode='psd')
    process_signal(s[1:s.shape[0]], 8, Y[i], np.amin(gradients[i]), np.amax(gradients[i]))




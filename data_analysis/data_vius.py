import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
from scipy import fftpack
import os

for root, dirs, files in os.walk("../new_data_processing/same_range_grad/"):
    for i, filename in enumerate(files):
        data = pd.read_csv(root + "/" + filename, header=None)
        X = data.values[:, 0:39]
        Y = data.values[:, 39]

        plus_peak_h = []
        minus_peak_h = []
        plus_peak_s = []
        minus_peak_s = []
        plt.figure(num=1, figsize=(16, 8))
        for i in range(len(X)):
            row = X[i]
            if Y[i] == 'H':
                ax1 = plt.subplot(1, 2, 1)
                ax1.plot(row)
                if row[row>0].size > 0:
                    plus_peak_h.append(np.max(row[row>0]))
                if row[row<0].size > 0:
                    minus_peak_h.append(np.min(row[row<0]))
            elif Y[i] == 'S':
                ax2 = plt.subplot(1, 2, 2)
                ax2.plot(row)
                if row[row > 0].size > 0:
                    plus_peak_s.append(np.max(row[row>0]))
                if row[row < 0].size > 0:
                    minus_peak_s.append(np.min(row[row<0]))
        ax1.set_title(filename + '  H')
        ax2.set_title(filename + '  S')
        a1 = np.average(plus_peak_h)
        print(a1)
        # plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
from scipy import fftpack
import statistics
import os

hpp = []
hpm = []
spp = []
spm = []

def calculate_stats(ary):

    stat_details = []
    # stat_details.append(np.max(ary))
    stat_details.append(np.min(ary))
    stat_details.append(np.median(ary))
    stat_details.append(np.std(ary))
    stat_details.append(np.var(ary))
    stat_details.append(np.ptp(ary))

    return stat_details

def get_padding_row():
    return [0,0]

def appened_to_file(flie_name, list, pref):

    with open(flie_name, "a") as write_file:
        line = np.array2string(np.array(list), precision=2, separator=',', suppress_small=True)
        line = line.replace("[", "").replace("]", "").replace("\n", "").replace(" ", "")

        #if mean included
        line = line.replace("list(", "").replace(")", "")

        write_file.write(line + "," + pref + "\n" )

def data_consolider():
    target_file = target_folder + 'all.csv'
    for root, dirs, files in os.walk("../new_data_processing/normalized_grad_stat_features/"):

        for i, filename in enumerate(files):
            data = pd.read_csv(root + "/" + filename, header=None)
            data.to_csv(target_file, mode='a', header=False)

target_folder = "../new_data_processing/normalized_grad_stat_features/"

for root, dirs, files in os.walk("../new_data_processing/same_range_grad/"):

    for i, filename in enumerate(files):
        data = pd.read_csv(root + "/" + filename, header=None)
        X = data.values[:, 0:39]
        Y = data.values[:, 39]

        plus_peak_h = []
        minus_peak_h = []
        plus_peak_s = []
        minus_peak_s = []

        target_file = target_folder + filename

        length = range(len(X))
        for i in length:
            row = X[i]
            stat_list = []
            if Y[i] == 'H':
                # if row[row>0].size > 0:
                #     stat_list.append(calculate_stats(row[row > 0]))
                # else:
                #     stat_list.append(get_padding_row())
                if row[row<0].size > 0:
                    stat_list.append(calculate_stats(row[row < 0]))
                # else:
                #     stat_list.append(get_padding_row())
                appened_to_file(target_file, stat_list, 'H')
            elif Y[i] == 'S':
                # if row[row > 0].size > 0:
                #     stat_list.append(calculate_stats(row[row > 0]))
                # else:
                #     stat_list.append(get_padding_row())
                if row[row < 0].size > 0:
                    stat_list.append(calculate_stats(row[row < 0]))
                # else:
                #     stat_list.append(get_padding_row())

                appened_to_file(target_file, stat_list, 'S')

data_consolider()
                # ax1.set_title(filename + '  H')
#         ax2.set_title(filename + '  S')
#         ax1.axhline(np.median(plus_peak_h))
#         ax1.axhline(np.median(minus_peak_h))
#         ax2.axhline(np.median(plus_peak_s))
#         ax2.axhline(np.median(minus_peak_s))
#         print(filename + ' HPP:' + str(np.median(plus_peak_h)) + ' HMP:'+str(np.median(minus_peak_h)) + ' SPP:'+ str(np.median(plus_peak_s)) + ' SMP:' + str(np.median(minus_peak_s)))
#         hpp.append(np.median(plus_peak_h))
#         hpm.append(np.median(minus_peak_h))
#         spp.append(np.median(plus_peak_s))
#         spm.append(np.median(minus_peak_s))
    #         ax1.plot(np.average(plus_peak_h))
#         ax1.plot(np.average(minus_peak_h))
#         ax2.plot(np.average(plus_peak_s)
#         ax2.plot(np.average(minus_peak_s)
#         plt.show()
#
# plt.figure(num=1, figsize=(16, 8))
# plt.plot(hpp, color='g')
# plt.plot(hpm, color='b')
# plt.plot(spp, color='r')
# plt.plot(spm, color='y')
# plt.axhline(np.average(hpp), color='g')
# plt.axhline(np.average(hpm), color='b')
# plt.axhline(np.average(spp), color='r')
# plt.axhline(np.average(spm), color='y')



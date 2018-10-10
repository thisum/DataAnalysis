import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
from scipy import fftpack
import os

N = 5
weights = np.ones(N)/N

def appened_to_file(flie_name, list, pref):
    with open(flie_name, "a") as write_file:
        line = np.array2string(np.array(list).transpose(), precision=2, separator=',', suppress_small=True)
        line = line.replace("[", "").replace("]", "").replace("\n", "").replace(" ", "")
        write_file.write(line + "," + pref + "\n")

def calculate_stats(ary):
    stat_details = []
    stat_details.append(np.max(ary))
    stat_details.append(np.min(ary))
    stat_details.append(np.median(ary))
    stat_details.append(np.mean(ary))
    stat_details.append(np.std(ary))
    stat_details.append(np.var(ary))
    stat_details.append(np.ptp(ary))

    return stat_details

# ## TODO reading well defined csv files
# for root, dirs, files in os.walk("../new_data_processing/same_range_grad"):
#     for i, filename in enumerate(files):
#         data = pd.read_csv(root + "/" + filename, header=None)
#         X = data.values[:, 0:43]
#         Y = data.values[:, 43]
#
#         avg_X = signal.convolve(X, [weights], 'valid')
#         for i in range(len(avg_X)):
#             x = np.arange(avg_X[i].size)
#             grad = np.gradient(avg_X[i], x)
#             appened_to_file('../new_data_processing/grad_stat_features/' + filename, grad.transpose(), Y[i])

## TODO reading raw files
target_folder = "../new_data_processing/normalized_grad_stat_features/"

for root, dirs, files in os.walk("../new_data_processing/raw/"):
    for i, filename in enumerate(files):

        target_file = target_folder + filename
        file = open(root + "/" + filename, "r")
        lines = file.readlines()
        for line in lines:
            [l, d] = line.split(":")
            # if ('PS' in l):
                #     print(l)
                d = d.replace('[', '').replace(']', '').replace('\n', '')
                d = np.fromstring(d, dtype=int, sep=',')
                l = l.split("-")[1]
                if l == 'HR':
                    l='H'
                elif l == 'SO':
                    l = 'S'
                elif l == 'RE':
                    l='R'
                elif l == 'MI':
                    l = 'M'

                avg_X = signal.convolve([d], [weights], 'valid')
                x = np.arange(avg_X.size)
                grad = np.gradient(avg_X[0], x)
                stat_list = []
                if l == 'H':
                    if grad[grad>0].size > 0:
                        appened_to_file(target_file, calculate_stats(grad[grad > 0]), 'H')
                    # else:
                    #     stat_list.append(get_padding_row())
                    if grad[grad < 0].size > 0:
                        # stat_list.append(calculate_stats(grad[grad < 0]))
                        appened_to_file(target_file, calculate_stats(grad[grad < 0]), 'H')
                elif l == 'S':
                    # if row[row > 0].size > 0:
                    #     stat_list.append(calculate_stats(row[row > 0]))
                    # else:
                    #     stat_list.append(get_padding_row())
                    if grad[grad < 0].size > 0:
                        # stat_list.append(calculate_stats(grad[grad < 0]))
                        appened_to_file(target_file, calculate_stats(grad[grad < 0]), 'S')
                elif l == 'M':
                # if row[row > 0].size > 0:
                #     stat_list.append(calculate_stats(row[row > 0]))
                # else:
                #     stat_list.append(get_padding_row())
                if grad[grad < 0].size > 0:
                    # stat_list.append(calculate_stats(grad[grad < 0]))
                    appened_to_file(target_file, calculate_stats(grad[grad < 0]), 'M')
                elif l == 'R':
                # if row[row > 0].size > 0:
                #     stat_list.append(calculate_stats(row[row > 0]))
                # else:
                #     stat_list.append(get_padding_row())
                if grad[grad < 0].size > 0:
                    # stat_list.append(calculate_stats(grad[grad < 0]))
                    appened_to_file(target_file, calculate_stats(grad[grad < 0]), 'R')

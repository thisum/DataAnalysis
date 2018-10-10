import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
from scipy import fftpack
import os

LENGTH = 43

target_folder = "../new_data_processing/gradients_with_relax_data/"
N = 5
weights = np.ones(N) / N

def prepare_data(path):
    for root, dirs, files in os.walk(path):
        for i, filename in enumerate(files):

            data = pd.read_csv(root + "/" + filename, header=None)
            data = data.sample(frac=1)
            data = data.iloc[0:42, :]
            df1 = data.loc[:, :42]
            lbls = data.loc[:, 43]
            lbls = np.array(lbls)

            target_file = target_folder + filename

            for j in range(len(df1)):
                row = df1.iloc[j, :]
                avg = np.convolve(row, weights, mode='valid')
                x = np.arange(avg.size)
                grad = np.gradient(avg, x)
                appened_to_file(target_file, grad.tolist(), lbls[j] )


# def appened_to_file(flie_name, list, pref):
#
#     with open(flie_name, "a") as write_file:
#         line = np.array2string(np.array(list), precision=2, separator=',', suppress_small=True)
#         line = line.replace("[", "").replace("]", "").replace("\n", "").replace(" ", "")
#
#         #if mean included
#         line = line.replace("list(", "").replace(")", "")
#
#         write_file.write(line + "," + pref + "\n" )

def appened_to_file(flie_name,str):

    with open(flie_name, "a") as write_file:
        write_file.write(str)

def data_consolider():
    target_file = target_folder + 'all.csv'
    for root, dirs, files in os.walk("../new_data_processing/gradients_with_relax_data/"):

        for i, filename in enumerate(files):
        #     data = pd.read_csv(root + "/" + filename, header=None)
        #     data.to_csv(target_file, mode='a', header=False)
            file = open(root + "/" + filename, "r")
            lines = file.readlines()
            for line in lines:
                appened_to_file(target_file, line)


# prepare_data("../new_data_processing/same_range_raw_without_relax/")
# prepare_data("../new_data_processing/relax_data/")
data_consolider()


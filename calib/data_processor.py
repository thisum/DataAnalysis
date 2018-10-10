import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
from scipy import fftpack
import os

LENGTH = 43


def prepare_data():

    for root, dirs, files in os.walk("../new_data_processing/raw/"):
        for i, filename in enumerate(files):

            hardList = []
            mildList = []
            softList = []
            relaxList = []

            file = open(root + "/" + filename, "r")
            lines = file.readlines()
            for line in lines:
                [l, d] = line.split(":")
                if ('WT' not in l):
                    d = d.replace('[', '').replace(']', '').replace('\n', '')
                    d = np.fromstring(d, dtype=int, sep=',')
                    d = pad_array(d)
                    l = l.split("-")[1]
                    # print(str(d.size))

                    if l == 'HR':
                        hardList.append(d)
                    elif l == 'MI':
                        mildList.append(d)
                    elif l == 'SO':
                        softList.append(d)
                    # elif l == 'RE':
                    #     relaxList.append(d)

            appened_to_file('../new_data_processing/same_range_raw_without_relax/' + filename, hardList, 'H')
            appened_to_file('../new_data_processing/same_range_raw_without_relax/' + filename, mildList, 'M')
            appened_to_file('../new_data_processing/same_range_raw_without_relax/' + filename, softList, 'S')
            # appened_to_file('../new_data_processing/thisum/all.csv', softList, 'R')


def pad_array(ary):

    if ary.size < LENGTH:
        if (LENGTH - ary.size) & 1:
            padded = np.pad(ary, (int(np.floor((LENGTH - ary.size)/2)), int(np.ceil((LENGTH - ary.size)/2))), 'edge')
        else:
            padded = np.pad(ary, (int((LENGTH - ary.size)/2), int((LENGTH - ary.size)/2)), 'edge')

    elif ary.size > LENGTH:
        if (LENGTH - ary.size) & 1:
            padded = np.delete(ary, np.s_[:int(np.ceil((ary.size - LENGTH)/2))])
            if padded.size == LENGTH:
                return padded
            padded = np.delete(padded, np.s_[-int(np.floor((ary.size - LENGTH)/2)):])
        else:
            padded = np.delete(ary, np.s_[:int((ary.size - LENGTH)/2)])
            if padded.size == LENGTH:
                return padded
            padded = np.delete(padded, np.s_[-int((ary.size - LENGTH)/2):])
    else:
        padded = ary

    return padded


def appened_to_file(flie_name, list, pref):
    with open(flie_name, "a") as write_file:
        for ary in list:
            line = np.array2string(ary, precision=2, separator=',', suppress_small=True)
            line = line.replace("[", "").replace("]", "").replace("\n", "").replace(" ", "")
            write_file.write(line + "," + pref + "\n" )




def data_length_stats():

    length_data = []

    for root, dirs, files in os.walk("../new_data_processing/raw/"):
        for i, filename in enumerate(files):

            lengths = []

            file = open(root + "/" + filename, "r")
            lines = file.readlines()
            for line in lines:
                [l, d] = line.split(":")
                d = d.replace('[', '').replace(']', '').replace('\n', '')
                d = np.fromstring(d, dtype=int, sep=',')
                lengths.append(len(d))

            length_data.append(lengths)

    max = np.max(np.array(length_data), axis=1)
    min = np.min(np.array(length_data), axis=1)
    avg = np.mean(np.array(length_data), axis=1)
    med = np.median(np.array(length_data), axis=1)
    sd = np.std(np.array(length_data), axis=1)


# data_length_stats()
prepare_data()
    

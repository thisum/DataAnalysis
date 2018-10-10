import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
from scipy import fftpack
import os

LENGTH = 43

target_folder = "../new_data_processing/same_range_raw_gesture/"
N = 5
weights = np.ones(N) / N

FI_list = []
PI_list = []
TT_list = []
WT_list = []
MW_list = []
PD_list = []
LP_list = []
TP_list = []
LT_list = []
PS_list = []
T2_list = []
IF_list = []
LG_list = []
T3_list = []

all_gestures = []

LENGTH = 43

action = ''

def prepare_data():

    for root, dirs, files in os.walk("../new_data_processing/raw/"):
        for i, filename in enumerate(files):

            file = open(root + "/" + filename, "r")
            lines = file.readlines()
            for line in lines:
                [l, d] = line.split(":")
                d = d.replace('[', '').replace(']', '').replace('\n', '')
                d = np.fromstring(d, dtype=int, sep=',')
                d = pad_array(d)

                pl = l.split("-")[1]
                if pl == 'HR':
                    action = 'H'
                elif pl == 'MI':
                    action = 'M'
                elif pl == 'SO':
                    action = 'S'

                li = d.tolist()
                li.append(action)


                if ('FI' in l):
                    FI_list.append(li)
                elif 'PI' in l:
                    PI_list.append(li)
                elif 'TT' in l:
                    TT_list.append(li)
                elif 'WT' in l:
                    WT_list.append(li)
                elif 'MW' in l:
                    MW_list.append(li)
                elif 'PD' in l:
                    PD_list.append(li)
                elif 'LP' in l:
                    LP_list.append(li)
                elif 'TP' in l:
                    TP_list.append(li)
                elif 'LT' in l:
                    LT_list.append(li)
                elif 'PS' in l:
                    PS_list.append(li)
                elif 'T2' in l:
                    T2_list.append(li)
                elif 'IF' in l:
                    IF_list.append(li)
                elif 'LG' in l:
                    LG_list.append(li)
                elif 'T3' in l:
                    T3_list.append(li)

    # all_gestures.append(FI_list)
    # all_gestures.append(PI_list)
    # all_gestures.append(TT_list)
    # all_gestures.append(WT_list)
    # all_gestures.append(MW_list)
    # all_gestures.append(PD_list)
    # all_gestures.append(LP_list)
    # all_gestures.append(TP_list)
    # all_gestures.append(LT_list)
    # all_gestures.append(PS_list)
    # all_gestures.append(T2_list)
    # all_gestures.append(IF_list)
    # all_gestures.append(LG_list)
    # all_gestures.append(T3_list)

    appened_to_file(target_folder + "/FI_list.csv", FI_list, '')
    appened_to_file(target_folder + "/PI_list.csv", PI_list, '')
    appened_to_file(target_folder + "/TT_list.csv", TT_list, '')
    appened_to_file(target_folder + "/WT_list.csv", WT_list, '')
    appened_to_file(target_folder + "/MW_list.csv", MW_list, '')
    appened_to_file(target_folder + "/PD_list.csv", PD_list, '')
    appened_to_file(target_folder + "/LP_list.csv", LP_list, '')
    appened_to_file(target_folder + "/TP_list.csv", TP_list, '')
    appened_to_file(target_folder + "/LT_list.csv", LT_list, '')
    appened_to_file(target_folder + "/PS_list.csv", PS_list, '')
    appened_to_file(target_folder + "/T2_list.csv", T2_list, '')
    appened_to_file(target_folder + "/IF_list.csv", IF_list, '')
    appened_to_file(target_folder + "/LG_list.csv", LG_list, '')
    appened_to_file(target_folder + "/T3_list.csv", T3_list, '')

    # for j in


def pad_array(ary):
    if ary.size < LENGTH:
        if (LENGTH - ary.size) & 1:
            padded = np.pad(ary, (int(np.floor((LENGTH - ary.size) / 2)), int(np.ceil((LENGTH - ary.size) / 2))),
                            'edge')
        else:
            padded = np.pad(ary, (int((LENGTH - ary.size) / 2), int((LENGTH - ary.size) / 2)), 'edge')

    elif ary.size > LENGTH:
        if (LENGTH - ary.size) & 1:
            padded = np.delete(ary, np.s_[:int(np.ceil((ary.size - LENGTH) / 2))])
            if padded.size == LENGTH:
                return padded
            padded = np.delete(padded, np.s_[-int(np.floor((ary.size - LENGTH) / 2)):])
        else:
            padded = np.delete(ary, np.s_[:int((ary.size - LENGTH) / 2)])
            if padded.size == LENGTH:
                return padded
            padded = np.delete(padded, np.s_[-int((ary.size - LENGTH) / 2):])
    else:
        padded = ary

    return padded


def appened_to_file(flie_name, list, pref):
    with open(flie_name, "a") as write_file:
        for ary in list:
            line = ','.join(str(e) for e in ary)
            line = line.replace("[", "").replace("]", "").replace("\n", "").replace(" ", "")
            write_file.write(line + "\n")

prepare_data()


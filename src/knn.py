# Import Basics
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# ~/dsi/capstones/cap_2/

# Import modeling tools
from sklearn.metrics import pairwise_distances
from scipy.spatial import distance
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

# import os
# print(os.listdir("../input"))



if __name__ == '__main__':
    
    # Load Data
    df_train = pd.read_csv('~/dsi/capstones/cap_2/data/forest-cover-competition/train.csv')
    # df_test = pd.read_csv('~/dsi/capstones/cap_2/data/forest-cover-competition/test.csv')

    # Remove Competition IDs
    df_train.drop(axis=0, columns='Id', inplace=True)
    # df_test.drop(axis=0, columns='Id', inplace=True)

    df_continuous = df_train.iloc[:, 0:10]

    df_toy = df_continuous[:1000]



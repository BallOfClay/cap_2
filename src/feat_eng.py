import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
from seaborn import heatmap


if __name__ == '__main__':

     # Load Data
     df_train = pd.read_csv('~/dsi/capstones/cap_2/data/forest-cover-competition/train.csv') # Training
     df_test = pd.read_csv('~/dsi/capstones/cap_2/data/forest-cover-competition/test.csv') # Testing
     df_all = pd.read_csv('~/dsi/capstones/cap_2/data/forest_coverage/covtype.csv')  # Entire Dataset

     # Preliminary
     df_all.info()
     df_all.describe()
     df_train.describe()

     # Seperate Train Dataframes for variable types
     df_cart = df_train.iloc[:, 0:10]
     df_wild = df_train.iloc[:, 10:14]
     df_soil = df_train.iloc[:, 14:54]
     df_binary = df_train.iloc[:, 10:54]

    
    plt.figure(figsize=(15,8))
    sns.heatmap(df_cart.corr(),cmap='coolwarm',linewidths=1,annot=True)
    
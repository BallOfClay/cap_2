import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math


# Constants

conv_m_2_ft = 3.28084
nine_hundred_m2_to_acres = 0.22239484


# Additional Information

wild_acreage_1 = 73068  # Wilderness Area 1
wild_acreage_2 = 9924   # Wilderness Area 2
wild_acreage_3 = 66791  # Wilderness Area 3
wild_acreage_4 = 9238   # Wilderness Area 4


# Helper Functions

def calc_acreage_forest(df, wild_area):
     series_wild = df.groupby(f'Wilderness_Area{wild_area}').get_group(1)
     acreage_forest = int(round(len(series_wild) * nine_hundred_m2_to_acres))
     return acreage_forest

def calc_percentage_forest(acreage_forest, wild_acreage):
     return float("{0:.3f}".format(acreage_forest/wild_acreage))

def calc_min_max(df, feature_name):
     series_feature = df.feature_name
     feature_min_max = [series_feature.min(), series_feature.max()]
     return feature_min_max

def calc_reduced_aspects(df, reduced_at=5):
     aspect_sums = df.Aspect.value_counts().sort_index()

     aspect_sums[0] += aspect_sums[360] # combine 0 and 360 degrees
     aspect_sums = aspect_sums[0:360] 

     reduced_aspect_sums = np.add.reduceat(np.array(aspect_sums), 
                                        np.arange(0, len(aspect_sums), reduced_at))
     return reduced_aspect_sums


'''
def plot_elevation(df):
    # Skipping a lot of other complexity her
    fig, ax = plt.subplots()
    ax.plot(x,y, ...)
    # further stuff
    return ax
'''


if __name__ == '__main__':

     # Load Data
     df_train = pd.read_csv('~/dsi/capstones/cap_2/data/forest-cover-competition/train.csv') # Training
     df_test = pd.read_csv('~/dsi/capstones/cap_2/data/forest-cover-competition/test.csv') # Testing
     df_all = pd.read_csv('~/dsi/capstones/cap_2/data/forest_coverage/covtype.csv')  # Entire Dataset

     # Preliminary
     df_all.info()
     df_all.describe()
     df_train.describe()


     # COMPLETE DATASET ANALYSIS

     # Calculate percent forests for wilderness area
     acres_wild_1 = calc_acreage_forest(df_all, 1)
     acres_wild_2 = calc_acreage_forest(df_all, 2)
     acres_wild_3 = calc_acreage_forest(df_all, 3)
     acres_wild_4 = calc_acreage_forest(df_all, 4)

     percent_forest_1 = calc_percentage_forest(acres_wild_1, wild_acreage_1)
     percent_forest_2 = calc_percentage_forest(acres_wild_2, wild_acreage_2)
     percent_forest_3 = calc_percentage_forest(acres_wild_3, wild_acreage_3)
     percent_forest_4 = calc_percentage_forest(acres_wild_4, wild_acreage_4)


     # Plot setup
     fig, ax = plt.subplots(figsize=(8,4))
     plt.style.use('ggplot')

     # Plot total number of each forest type
     cover_counts = df_all.Cover_Type.value_counts()
     ax.hist(df_all['Cover_Type'], bins=7)
     ax.set_title('Total Number of Coverage Type Patches')
     ax.set_xlabel('Coverage Type', fontsize=16)
     ax.set_ylabel('Counts', fontsize=16)
     fig.savefig('cover_counts.png')
     

     # Plot distribution of total forest at each elevation
     ax.hist(df_all['Evelation'], bins=50)
     ax.set_title('Distribution of Elevations')
     ax.set_xlabel('Coverage Type', fontsize=16)
     ax.set_ylabel('Counts', fontsize=16)
     fig.savefig('elevation_counts.png')

     # Plot distribution of total forest on each slope
     ax.hist(df_all['Slope'], bins=50)
     ax.set_title('Distribution of Elevations')
     ax.set_xlabel('Coverage Type', fontsize=16)
     ax.set_ylabel('Counts', fontsize=16)
     fig.savefig('elevation_counts.png')

     
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math


# Color Palettes
flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
"muted"
"coolwarm"
"PRGn"
"YlOrBr"
"rainbow"

# hue
'Cover_Type'


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

     # Seperate Train Dataframes for variable types
     df_cart = df_train.iloc[:, 0:10]
     df_wild = df_train.iloc[:, 10:14]
     df_soil = df_train.iloc[:, 14:54]
     df_binary = df_train.iloc[:, 10:54]


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
     # fig, ax = plt.subplots(figsize=(8,6))
     # plt.style.use('ggplot')

     # Plot total number of each forest type
     fig, ax = plt.subplots(figsize=(8,6))
     plt.style.use('ggplot')

     cover_counts = df_all.Cover_Type.value_counts()
     ax.hist(df_all['Cover_Type'], bins=7)
     ax.set_title('Total Number of Coverage Type Patches')
     ax.set_xlabel('Coverage Type', fontsize=16)
     ax.set_ylabel('Counts', fontsize=16)
     plt.show()
     

     # Plot distribution of total forest at each elevation
     fig, ax = plt.subplots(figsize=(8,6))
     plt.style.use('ggplot')

     ax.hist(df_all['Elevation'], bins=50)
     ax.set_title('Distribution of Elevations')
     ax.set_xlabel('Elevation in meters', fontsize=16)
     ax.set_ylabel('Counts', fontsize=16)
     plt.show()

     # Plot distribution of total forest on each slope
     fig, ax = plt.subplots(figsize=(8,6))
     plt.style.use('ggplot')

     ax.hist(df_all['Slope'], bins=65)
     ax.set_title('Distribution of Slopes')
     ax.set_xlabel('Slope', fontsize=16)
     ax.set_ylabel('Counts', fontsize=16)
     plt.show()

     # Plot polar distribution of percent total forest at each aspect
     ax2 = plt.subplot(polar=True)
     plt.style.use('ggplot')

     ax2.set_theta_direction(-1)

     polar_reduction = 5
     summed_aspect_sums = calc_reduced_aspects(df_all, polar_reduction)
     degrees = np.arange(0,360,polar_reduction)

     ax2.plot(degrees*math.pi/180, summed_aspect_sums/sum(summed_aspect_sums))
     ax2.set_theta_offset(math.pi/2)
     ax2.set_title('Distribution of Aspects')
     plt.show()
     # plt.close('all')

     fig, ax = plt.subplots(figsize=(8,6))
     plt.style.use('ggplot')

     ax.hist(df_all['Elevation']*conv_m_2_ft, bins=50)
     ax.set_title('Distribution of Elevations (feet)')
     ax.set_xlabel('Elevation in feet', fontsize=16)
     ax.set_ylabel('Counts', fontsize=16)
     plt.show()


     # TRAIN DATASET ANALYSIS
     
     # Plot number of each forest type
     fig3, ax3 = plt.subplots(figsize=(8,6))
     plt.style.use('ggplot')

     cover_counts = df_train.Cover_Type.value_counts()
     ax3.hist(df_train['Cover_Type'], bins=7)
     ax3.set_title('Total Number of Coverage Type Patches')
     ax3.set_xlabel('Coverage Type', fontsize=16)
     ax3.set_ylabel('Counts', fontsize=16)
     plt.show()
     plt.close('all')

     # Box Plots
     '''
     chosen = ['Elevation' , 'Aspect' , 'Slope', 'Horizontal_Distance_To_Hydrology' , 
               'Vertical_Distance_To_Hydrology' ,'Horizontal_Distance_To_Roadways','Hillshade_9am',
               'Hillshade_Noon','Hillshade_3pm','Horizontal_Distance_To_Fire_Points','Cover_Type']
     '''

     
     chosen = ['Elevation' , 'Aspect' , 'Slope', 'Horizontal_Distance_To_Hydrology', 
               'Vertical_Distance_To_Hydrology', 'Hillshade_Noon', 'Horizontal_Distance_To_Fire_Points',
               'Cover_Type']

     df_chosen = df_train[chosen]

     df_chosen['Cover_Type'] = df_chosen['Cover_Type'].astype('category')

     for idx, col in enumerate(df_chosen.columns):
          plt.figure(idx, figsize=(8,4))
          sns.boxplot(x=df_chosen['Cover_Type'], y=chosen, data=df_chosen, palette="PRGn")
     

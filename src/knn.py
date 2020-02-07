# Import Basics
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import pickle

# ~/dsi/capstones/cap_2/

# Import modeling tools
from sklearn.metrics import pairwise_distances
from scipy.spatial import distance
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix


pruned_features = ['']



if __name__ == '__main__':
    
    # Load Data
    df_train = pd.read_csv('~/dsi/capstones/cap_2/data/forest-cover-competition/train.csv')
    df_test = pd.read_csv('~/dsi/capstones/cap_2/data/forest-cover-competition/test.csv') #Unseen Data


    # Remove Competition IDs
    df_train.drop(axis=0, columns='Id', inplace=True)
    df_test.drop(axis=0, columns='Id', inplace=True)


    # Run Train DF 
    X = df_train.iloc[:,:-1]
    y = df_train.iloc[:,-1]

    seed = 0
    test_split = .2

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_split, random_state=seed)

    min_max_scaler = MinMaxScaler()
    X_min_max = min_max_scaler.fit_transform(X_train)
    # matrix_max_min = pairwise_distances(df_max_min, metric = 'euclidean')

    std_scaler = StandardScaler()
    X_std = std_scaler.fit_transform(X_train)
    # matrix_max_min = pairwise_distances(df_max_min, metric = 'euclidean')

    # Without scalers
    knn_classifier = KNeighborsClassifier(n_neighbors=7, n_jobs=-2)
    knn_classifier.fit(X_train, y_train)

    y_pred = knn_classifier.predict(X_test)

    test_accuracy = knn_classifier.score(X_test, y_test) 

    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    '''
    # Min Max Scaler
    knn_classifier = KNeighborsClassifier(n_neighbors=7, n_jobs=-2)
    knn_classifier.fit(X_min_max, y_train)

    y_pred = knn_classifier.predict(X_test)

    test_accuracy = knn_classifier.score(X_test, y_test) 

    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))

    # Standard Scaler
    knn_classifier = KNeighborsClassifier(n_neighbors=7, n_jobs=-2)
    knn_classifier.fit(X_std, y_train)

    y_pred = knn_classifier.predict(X_test)

    test_accuracy = knn_classifier.score(X_test, y_test) 

    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    '''


    # Unseen Dataset
    X_unseen = df_test
    # y = df_test

    seed = 0
    test_split = .2

    '''
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_split, random_state=seed)

    min_max_scaler = MinMaxScaler()
    X_min_max = min_max_scaler.fit_transform(X_train)
    # matrix_max_min = pairwise_distances(df_max_min, metric = 'euclidean')

    std_scaler = StandardScaler()
    X_std = std_scaler.fit_transform(X_train)
    # matrix_max_min = pairwise_distances(df_max_min, metric = 'euclidean')

    knn_classifier = KNeighborsClassifier(n_neighbors=7, n_jobs=-2)
    knn_classifier.fit(X_train, y_train)
    '''

    y_pred_unseen = knn_classifier.predict(X_unseen)

    '''
    test_accuracy = knn_classifier.score(X_test, y_test) 

    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    '''
    
    with open('results_knn', 'wb') as fp: 
        pickle.dump(y_pred_unseen, fp) 

    with open('results_knn.txt', 'w') as f:
        for item in y_pred_unseen:
            print >> f, item

    
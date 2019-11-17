import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from dateutil.parser import parse

# helper functions

def data_overview(data_set):
    """
    Takes in the smell data, prints column names, shape, value counts
    """
    print('Column headings: ')
    print(data_set.columns)
    # Index([u'epoch time', u'date & time', u'smell value', 
    #       u'skewed latitude', u'skewed longitude', u'zipcode', u'smell description', 
    #       u'symptoms', u'additional comments'],
    #      dtype='object')
    print('Shape: ')
    print(data_set.shape)
    # (34488, 9)
    print('Zipcode value counts: ')
    print(data_set['zipcode'].value_counts())
    # 15217     5497
    # 15218     2972
    # 15206     2721
    # 15221     1997
    # 15025     1367
    # 15213     1313
    # ...
    # 15047     1
    print('Earliest data point date: ')
    print(data_set['date & time'].min())
    # June 1, 2016
    print('Latest data point date: ')
    print(data_set['date & time'].max())
    # November 3, 2019
    print('Smell number value counts: ')
    print(data_set['smell value'].value_counts())
    
    

def plot_geo_data(data_set):
    """
    Plot latitude versus longitude for the dataset.
    """
    plt.scatter(data_set['skewed latitude'], data_set['skewed longitude'])
    plt.title('Geographical Distribution of Data Points')
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.show()
    
def plot_time_vs_smell(data_set):
    """
    Plot time only vs smell to see whether all times of day are represented.
    """
    times = [dt.time() for dt in data_set['date & time']]
    plt.scatter(times, data_set['smell value'])
    plt.title('Time of day versus smell value')
    plt.xlabel('Time of day')
    plt.ylabel('Smell value')
    plt.show()
    
    

# load data
raw_data = pd.read_csv('smell_reports.csv')


# Initial data prep
raw_data['date & time'] = pd.to_datetime(raw_data['date & time'])












#data_overview(raw_data)
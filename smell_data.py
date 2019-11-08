import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dateutil import parser

raw_data = pd.read_csv('smell_reports.csv')
#print(data.head())
#print(data.columns) = Index([u'epoch time', u'date & time', u'smell value', u'skewed latitude',
#       u'skewed longitude', u'zipcode', u'smell description', u'symptoms',
#       u'additional comments'],
#      dtype='object')
#data.shape = (34488, 9)

# Figure out which zipcodes to consider - some seem to have much more data than others
#zipcodes = raw_data['zipcode'].unique()
#print(raw_data['zipcode'].value_counts())

#plot latitude, longitude to estimate geographic spread of data
plt.scatter(raw_data['skewed latitude'], raw_data['skewed longitude'])
plt.title('geographical distribution of data points')
plt.show()





## code for scatter plot
#plt.scatter(raw_data['zipcode'], raw_data['smell value'])
#plt.title('Zipcode vs smell value')
#plt.xlabel('zipcode')
#plt.ylabel('smell value')
#plt.show()
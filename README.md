# SmellPghWeather
Using weather data to predict the strength of the smell of pollution

## Summary of Plan
Data has been collected from the public in the Pittsburgh region by [Smell Pittsburgh](smellpgh.org), and they have probably done a lot of cool analysis of the data. I have chosen not to read exactly what they've done until I've played with the data myself. I plan to use machine learning to predict when there will be a bad smell.

## The Smell Data
I downloaded [the smell data](./smell_reports.csv) November 3, 2019. Some initial analysis: this data set of 34488 entries contains the following information.
* Epoch time
* Date & Time
* Smell Value - a number between 1 and 5
* Skewed Latitude
* Skewed Longitude
* Zipcode
* Smell Description
* Symptoms
* Additional Comments

The following is the geographic distribution of data points. ![GeoDist](/geography.png) Further analysis of the points around the edges might be necessary. The data points in this set range from June 1, 2016 to November 3, 2019. This helps narrow down the weather data we need to gather in order to do the comparison.


from datetime import datetime

import pandas as pd
import numpy as np

from scipy.stats.stats import pearsonr

# PRICES

df_prices = pd.read_csv('data/SPOT.csv')
# sourced from; https://uk.finance.yahoo.com/quote/SPOT/history?period1=1522713600&period2=1696464000&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true

# import as dates, or you will pass strings to matplotlib and it will create thousands of ticks!
dates = [datetime.strptime(date_str, '%Y-%m-%d') for date_str in df_prices['Date']]
close_prices = df_prices['Close'].tolist()


# Monthly Active Users (MAU)

df_MAU = pd.read_csv('data/MAU.csv')
# sourced from; https://www.statista.com/statistics/367739/spotify-global-mau/

quarters = df_MAU['Quarter'].tolist()
mau = df_MAU['MAU'].tolist()

# Define a mapping of quarters to month ranges
quarter_to_month = {
    'Q1': (1, 3),  # January to March
    'Q2': (4, 6),  # April to June
    'Q3': (7, 9),  # July to September
    'Q4': (10, 12)  # October to December
}

# Function to convert quarterly dates to date objects
def quarterly_to_date(quarterly_date):
    quarter, year = quarterly_date.split()
    start_month, end_month = quarter_to_month[quarter]
    #start_date = datetime(int(year), start_month, 1)
    end_date = datetime(int(year), end_month, 1)
    return end_date

# Convert quarterly dates to date objects
date_objects = [quarterly_to_date(date) for date in quarters]

# SUBS (monthly premium subscribers)

df_SUBS = pd.read_csv('data/SUBS.csv')
# sourced from; https://www.statista.com/statistics/244995/number-of-paying-spotify-subscribers/

quarters = df_SUBS['Quarter'].tolist()
subs = df_SUBS['SUBS'].tolist()

date_objects_subs = [quarterly_to_date(date) for date in quarters]

# ANALYSIS

# 0 indicates no linear correlation between two variables
# 1 indicates a perfectly positive linear correlation between two variables
correlation = np.corrcoef(subs, mau)[0,1]
print(str(correlation))

# test if this correlation is statistically significant
# calculate the p-value associated with the Pearson correlation coefficient
# the p-value is the second number returned
pvalue = pearsonr(subs, mau)[1]
print(pvalue)

# CHARTING...

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot()

ax.text(0.5, 0.95, 'Correlation Coefficient:' + str(round(correlation,4)), transform=ax.transAxes, fontsize=10)
ax.text(0.5, 0.90, 'p Value:' + str(format(pvalue, '.20f')), transform=ax.transAxes, fontsize=10)

xpoints1 = np.array(dates)
ypoints1 = np.array(close_prices)

ax.plot(xpoints1, ypoints1, label='Share Price')

xpoints2 = np.array(date_objects)
ypoints2 = np.array(mau)

ax.plot(xpoints2, ypoints2, label='MAU\'s')

xpoints3 = np.array(date_objects_subs)
ypoints3 = np.array(subs)

ax.plot(xpoints3, ypoints3, label='Subscribers')

plt.title("Spotify Correlations (MAU vs Subscribers)")
plt.legend()
plt.show()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 19:09:58 2021

@author: youpele
"""

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pylab as plt
from matplotlib import pyplot

from matplotlib.pylab import rcParams

rcParams['figure.figsize'] = 10,6



df = pd.read_csv('./Assets/eurcad_price.csv', header= None)


series = pd.read_csv('./Assets/eurcad_price.csv', header= None,  index_col=0, parse_dates=True, squeeze=True)

series.plot.line()
pyplot.show()

std = series.std(skipna=True)

annual_standard_deviation = std * math.sqrt(12)

series.describe()
series.plot()





df = series.to_frame()

df = df.reset_index()

df = df.rename(columns={0:"date_column", 1: 'security'})



df['year_month'] = df['date_column'].dt.to_period('D')


series_M=series.resample('1M').mean()

series_M.plot()
std_M = series_M.std(skipna=True)
annual_standard_deviation = std_M * math.sqrt(12)

df.plot()

plt.plot(df['year_month'].values, df['security'].values, linewidth=2.0)


df['month_year'] = df['date_column'].dt.to_period('M')



series.plot(style='k.')
pyplot.show()


series = read_csv('daily-minimum-temperatures.csv', header=0, index_col=0, parse_dates=True, squeeze=True)
print(series.head())



, infer_datetime_format=True)

plt.plot(df)

df['Time'] = pd.to_datetime(df.iloc[0:,0])
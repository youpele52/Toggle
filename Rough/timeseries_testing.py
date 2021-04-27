#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 16:21:19 2021

@author: youpele
"""


import pandas as pd

df= pd.read_csv('./Assets/eurcad_price.csv')


import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np



def parser(s):
    return datetime.strptime(s, '%d/%m/%Y')


eurcad_price = pd.read_csv('./Assets/eurcad_price.csv', parse_dates=[0], index_col=1, squeeze=True, date_parser=parser)

eurcad_price = eurcad_price.asfreq(eurcad_price)

eurcad_price


eurcad_price = eurcad_price['a'] + pd.offsets.SemiMonthEnd()





import pandas as pd
date = pd.to_datetime("30/10/1989")
date

date + pd.to_timedelta(np.arange(12), 'D')

	16/10/1989
9	30/10/1989


dates = pd.to_datetime([datetime(2015, 7, 3), '4th of July, 2015',
                       '2015-Jul-6', '07-07-2015', '20150708'])
dates

dates.to_period('M')



from pandas_datareader import data

goog = data.DataReader('GOOG', start='2004', end='2016',
                       data_source='yahoo')
goog.head()

goog = goog['Close']

%matplotlib inline
import matplotlib.pyplot as plt
import seaborn; seaborn.set()


goog.plot();
goog.plot(alpha=0.5, style='-')
goog.resample('BA').mean().plot(style=':')
goog.asfreq('BA').plot(style='--');
plt.legend(['input', 'resample', 'asfreq'],
           loc='upper left');



fig, ax = plt.subplots(3, sharey=True)

# apply a frequency to the data
goog = goog.asfreq('d', method='pad')

goog.plot(ax=ax[0])
goog.shift(900).plot(ax=ax[1])
goog.tshift(900).plot(ax=ax[2])

# legends and annotations
local_max = pd.to_datetime('2007-11-05')
offset = pd.Timedelta(900, 'D')

ax[0].legend(['input'], loc=2)
ax[0].get_xticklabels()[2].set(weight='heavy', color='red')
ax[0].axvline(local_max, alpha=0.3, color='red')

ax[1].legend(['shift(900)'], loc=2)
ax[1].get_xticklabels()[2].set(weight='heavy', color='red')
ax[1].axvline(local_max + offset, alpha=0.3, color='red')

ax[2].legend(['tshift(900)'], loc=2)
ax[2].get_xticklabels()[1].set(weight='heavy', color='red')
ax[2].axvline(local_max + offset, alpha=0.3, color='red');



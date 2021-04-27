#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 14:21:49 2021

@author: youpele
"""


import requests
from bs4 import BeautifulSoup


def extract_info(url):

    url = url.split('?')
    compnay_profile_url = url[0] + '/profile?' + url[1]
    
    page = requests.get(compnay_profile_url)
    soup = BeautifulSoup(page.content, 'html.parser')
        
    results = soup.find('p', class_='D(ib) Va(t)' )
    
    info = results.find_all('span', class_='Fw(600)')
    
    return {"Sector(s)": info[0].get_text(),
                    "Industry":info[1].get_text(),
                    "Full-time employees": info[2].get_text()}


# Example 
url = 'https://uk.finance.yahoo.com/quote/TSLA?p=TSLA'
extract_info(url)



url = 'https://uk.finance.yahoo.com/quote/HSBA.L?p=HSBA.L'
extract_info(url)

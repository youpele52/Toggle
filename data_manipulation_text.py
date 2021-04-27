#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 11:04:50 2021

@author: youpele
"""


import pandas as pd

# importing the dataset and 
df_temp = pd.read_csv('./assets/stock_names.csv', delimiter=':', error_bad_lines=False)
# resetting the default index and renaming it to Ticker
df_temp = df_temp.reset_index()
df_temp = df_temp.rename(columns={"index":"Ticker"})

# creating the exchange and name columns 
df_temp[['Exchange', 'Name']] =  df_temp['full_name'].str.split('-', 1, expand=True)
df_temp = df_temp.drop(columns='full_name')



#  list of ancillaries
ancillaries  = [ 'SA', 'ASA', 'PLC', 'AG', 'A/S', 'SE', 'NV', 'NA', 'OYJ',  'AB', 'DSM', 'G', 'SGBS', 'ORD', 'CORPORATION','CORP', 'INCORPORATED', 'INC', 
                'LIMITED', 'LTD', 'LP', 'ASE' 'CO', 'LLC', 'INCO', 'INC.']


clean_name_list = []
no_ancilliary = []

# loops through the company names to check if it contains any of the ancilllaries, if it does the ancillary is removed
for company in df_temp['Name']:
    company = str(company)

    company_temp = company.upper().replace('.', ' ').split(" ")
    
    if company_temp[-1] in ancillaries:

        company_temp.remove(company_temp[-1])
        
        clean_name_list.append(" ".join(company_temp).title())
    else:
        clean_name_list.append(company)
      
        
        
clean_name_df = pd.DataFrame( {'Clean_Name': clean_name_list}, index=range(0,len(clean_name_list))    )

# merging the clean name df and the orginal df_temp
df_merged = df_temp.merge(clean_name_df, how='outer', left_index=True, right_index=True)


# export to CSV
df_merged.to_csv('./assets/data_manipulation_text.csv')
#%%

import pandas as pd
import json
import requests
from datawrapper import Datawrapper
import datetime

#%%
now = datetime.datetime.now()
today = now.strftime('%Y-%m-%d')
today
# %%

req_text = requests.get('https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/en/json/?date='+today).json()

#%%
df = pd.DataFrame(req_text[0]['currencies'])

#%%
df.info()

# filter some columns into a new df
new_df = df[['code','quantity','rate', 'name', 'diff']]

new_df

#%%

dw_token = ''  # <--- Add your datawrapper token here

# What is the ID of the Chart?
chart_id = 'oZ8QK'

# Authenticate into Datawrapper
dw = Datawrapper(access_token = dw_token)

#%%

dw.add_data(chart_id, new_df)

dw.publish_chart(chart_id, display=False)

#%%
# You save it as csv - only once to style the table in Datawrapper
new_df.to_csv('exchangerates.csv')

#%%
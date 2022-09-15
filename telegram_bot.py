#%%

import requests
import json
import pandas as pd
import datetime

token = ''


# Get all the Updates from the Telegram Chat
answer = requests.get(f'https://api.telegram.org/bot{token}/getUpdates')
answer

# Convert it to JSON structure
data = json.loads(answer.content)

# Put the json into a dataframe
df = pd.DataFrame(data['result'])

# normalize the nested structure
messages = pd.json_normalize(df['message'])

# Get the last row of the dataframe
search = messages.iloc[-1].text

now = datetime.datetime.now()
today = now.strftime('%Y-%m-%d')
today

req_text = requests.get('https://nbg.gov.ge/gw/api/ct/monetarypolicy/currencies/en/json/?date='+today).json()

df = pd.DataFrame(req_text[0]['currencies'])



# Filter the Dataframe to find the correct currency
try:
    rate = df[df['code'] == search].rateFormated.item()
except:
    rate = 'No rate has been found'


# Now, we want to send something

params = {'chat_id':messages.iloc[-1]['chat.id'], 'text':f'The current exchange rate for {search} is {rate}'}

url = f'https://api.telegram.org/bot{token}/sendMessage'

message = requests.post(url, params=params)


# %%

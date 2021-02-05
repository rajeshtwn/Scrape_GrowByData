import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Scrape the data from the page
url = 'https://covid19.who.int/region/searo/country/np'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# Extract and display the latest number of confirmed cases and deaths in Nepal
span = soup.find_all('span', {'class': 'sc-fznAgC'})

res_cases = re.findall(r'\d+', str(span[0]))
confirmed_cases = int(''.join(res_cases))

res_deaths = re.findall(r'\d+', str(span[1]))
deaths = int(''.join(res_deaths))

print('Confirmed cases: {}, Deaths: {}'.format(confirmed_cases, deaths))

# Extract and list the top 10 countries data, sorted by descending order of
# total cummulative cases
url = 'https://covid19.who.int/table'
json_data_url = 'https://covid19.who.int/page-data/index/page-data.json'
n = 10

r = requests.get(json_data_url)
json_data = r.json()

data = json_data['result']['pageContext']['rawDataSets']['lastDayPerCountry']

#n_items = {k: data[k] for k in list(data.keys())[:n]}
new = pd.DataFrame.from_dict(data).transpose()
new.reset_index(inplace=True)
new.rename(columns = {'index':'country'}, inplace = True)

#new_dict = pd.DataFrame.to_dict(new.transpose())

print(new.head(n))

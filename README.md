# Scrape_GrowByData_Assignment
### Python Packages Used:
Requests - for sending HTTP requests

BeautifulSoup - for parsing HTML documents

First request is sent to the website "https://covid19.who.int/region/searo/country/np" and the returned response is parsed using 'html.parser' provided by BeautifulSoup package.

```{python}
url = 'https://covid19.who.int/region/searo/country/np'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
```

#### a) Extract and display the latest number of confirmed cases and deaths for Nepal.
When looking at the parsed html, data for the latest number of confirmed cases and deaths are within a <span> tag with class name "sc-fznAgC". So for this, we find all the <span> tag with class name "sc-fznAgC" from the parsed html, which will provide us with a python list having exactly two items - first for confirmed cases, second for deaths. Then, looping around the list generated we use regular expression to extract digit portion from the captured <span>s for confirmed cases and deaths.

```{python}
span = soup.find_all('span', {'class': 'sc-fznAgC'})

res_cases = re.findall(r'\d+', str(span[0]))
confirmed_cases = int(''.join(res_cases))

res_deaths = re.findall(r'\d+', str(span[1]))
deaths = int(''.join(res_deaths))

print('Confirmed cases: {}, Deaths: {}'.format(confirmed_cases, deaths))
```

#### b) Extract and list the top 10 countries data, sorted by descending order of total cumulative cases. Use the data obtained by clicking the link “Data Table”
First we click on the "Data Table" button in the given url "https://covid19.who.int/region/searo/country/np". This will redirect us to "https://covid19.who.int/table". On this page there is a data table which is loaded from a external json file from url "https://covid19.who.int/page-data/index/page-data.json" which was found by doing "Inspect Element" on the page. A request is sent to this json data url and the response data is parsed to json format. This json file is more than 12 MB in size and has a lot of data. The portion of data that we require is within the key "lastDayPerCountry". We can use python package pandas to convert the json (dictionary) obtained to dataframe because working with data is more easier in dataframes. Then, we print the first top 10 data. There is no need to sort the data based on total cummulative cases as it is already sorted on this.

```{python}
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
```

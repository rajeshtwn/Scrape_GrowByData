# Scrape_GrowByData_Assignment
#### Python Packages Used:
Requests - for sending HTTP requests
BeautifulSoup - for parsing HTML documents

First request is sent to the website "https://covid19.who.int/region/searo/country/np" and the returned response is parsed using 'html.parser' provided by BeautifulSoup package.

```{python}
url = 'https://covid19.who.int/region/searo/country/np'

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
```

#### Extract and display the latest number of confirmed cases and deaths for Nepal.
When looking at the parsed html, data for the latest number of confirmed cases and deaths are within a <span> tag with class name "sc-fznAgC". So for this, we find all the <span> tag with class name "sc-fznAgC" from the parsed html, which will provide us with a python list having exactly two items - first for confirmed cases, second for deaths. Then, looping around the list generated we use regular expression to extract digit portion from the captured <span>s for confirmed cases and deaths.

```{python}
span = soup.find_all('span', {'class': 'sc-fznAgC'})

res_cases = re.findall(r'\d+', str(span[0]))
confirmed_cases = int(''.join(res_cases))

res_deaths = re.findall(r'\d+', str(span[1]))
deaths = int(''.join(res_deaths))

print('Confirmed cases: {}, Deaths: {}'.format(confirmed_cases, deaths))
```

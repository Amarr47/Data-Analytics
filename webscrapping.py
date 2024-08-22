from bs4 import BeautifulSoup as bs
import pandas as pd
import requests as r
url = 'https://en.wikipedia.org/wiki/World_population'
req = r.get(url).text
s = bs(req,'html5lib')
tables = s.find_all('table')
#load data from html tables using read_html and beautifulsoup
dp =pd.read_html(url,flavor='bs4')
#print(dp[0])
#load data from specific html tables using read_html
df =pd.read_html(url,match='World historical and predicted populations',flavor='bs4')[0]
print(df)
for index,table in enumerate(tables):
      if("10 most densely populated countries"in str(table)):
         table_index = index
#print(table_index)
#load data from html tables using pandas and beautiful soup
pdata = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])
for row in tables[table_index].tbody.find_all('tr'):
      col = row.find_all('td')
      if(col != []):
            rank = col[0].text
            country= col[1].text
            population = col[2].text
            area = col[3].text
            density = col[4].text
            pdata = pdata.append({"Rank":rank,"Country":country, "Population":population, "Area":area, "Density":density},ignore_index=True)
#print(pdata)
read =pd.read_html(str(tables[5]),flavor='bs4')
#print(read)

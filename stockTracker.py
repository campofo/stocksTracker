import requests
from bs4 import BeautifulSoup
import pandas as pd
yahoo = "https://finance.yahoo.com/most-active"
html = requests.get(yahoo)
data = html.text
soup = BeautifulSoup(data,'lxml')
codes =[]
names=[]
prices=[]
changes=[]
percentage_changes=[]
total_volumes=[]
market_caps=[]
price_earning_ratios=[]
#GETTING THE TABLE FROM YAHOO FINANACE
table =soup.find("tbody")
for listing in table.find_all("tr"):
    code =listing.find('td',attrs= {'aria-label':'Symbol'})
    codes.append(code.text)
    name = listing.find('td',attrs={"aria-label":"Name"})
    names.append(name.text)
    price = listing.find('td',attrs={'aria-label':"Price (Intraday)"})
    prices.append(price.text)
    # change =listing.find('tr',attrs={'aria-label':"Change"})
    # changes.append(change.text)
    # percentage_change= listing.find('tr',attrs={"aria-label":"% Change"})
    # percentage_changes.append(percentage_change.text)
    # total_volume = listing.find("tr",attrs={"aria-label":"Volume"})
    # total_volumes.append(total_volume.text)
    # marketcap = listing.find("tr",attrs={'aria-label':"Market Cap"})
    # market_caps.append(marketcap.text)
    # price_earning_ratio = listing.find('tr',attrs={"aria-label":"PE Ratio (TTM)"})
    # price_earning_ratios.append(price_earning_ratio.text)
# print (codes)
# print(names)
# print(prices)
# print(changes)
# print(percentage_changes)
# print(total_volumes)
# print(market_caps)
# print(price_earning_ratios)
df = pd.DataFrame({
    "Symbols": codes,
    "Names": names,
    "Prices": prices

})
print(df)


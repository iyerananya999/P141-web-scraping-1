from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars"

# Webdriver
page = requests.get(START_URL)
soup = BeautifulSoup(page.text, 'html.parser')
star_table  = soup.find('table')
time.sleep(10)

star_data = []

# Define Exoplanet Data Scrapping Method
table_rows  = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row =[i.text.rstrip()for i in td]
    star_data.append(row)

names = []
distance = []
mass = []
radius = []
lum = []
for i in range(1,len(star_data)):
    names.append(star_data[i][1])
    distance.append(star_data[i][3])
    mass.append(star_data[i][5])
    radius.append(star_data[i][6])
    lum.append(star_data[i][7])


# Define pandas DataFrame   
star_df = pd.DataFrame(list(zip(names, distance, radius, mass, lum)), columns = ['Star_name','Distance','Mass','Radius','Luminosity'])
star_df.to_csv('bright_stars.csv')

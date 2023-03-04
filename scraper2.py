from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import csv

# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Webdriver
browser = webdriver.Chrome("./IEDriverServer.exe")
browser.get(START_URL)

time.sleep(10)

stars_data = []
soup=BeautifulSoup(browser.text,"html.parser")
startable=soup.find("table")
tablerows=startable.find_all("tr")
for i in tablerows:
    td=i.find_all("td")
    row=[j.text.rstrip() for j in td]
    stars_data.append(row)


Star_names = [] 
Distance =[] 
Mass = [] 
Radius =[] 
Lum = [] 
for i in range(1,len(stars_data)):
     Star_names.append(stars_data[i][1]) 
     Distance.append(stars_data[i][3]) 
     Mass.append(stars_data[i][5]) 
     Radius.append(stars_data[i][6]) 
      
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),
columns=['Star_name','Distance','Mass','Radius']) 
print(df2) 
df2.to_csv('brown_dwarfs.csv')

from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

def pobierz_dane():
  url = "https://link.springer.com/article/10.1186/1744-9081-3-42/tables/2"
kod_strony = requests.get(url).text    #pobieranie strony
soup = BeautifulSoup(kod_strony, "html.parser")

tabela = soup.find("table")    #wyciąganie danych z tabeli
wiersze = tabela.find_all("tr")

wyniki = []
for wiersz in wiersze:
  komorki = wiersz.find_all(["td", "th"])
  wyniki.append([k.text.strip() for k in komorki])

df = pd.DataFrame(wyniki)      #zapis w folderze data
os.makedirs("data", exist_ok=True)
df.to_csv("data/tabela_dane.csv", index=False, header=False)
print("Pobrano dane!")

from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

#Ta funkcja automatycznie pobiera dane z internetu
def pobierz_dane():
#Link do strony z badaniami nad ADHD
    url = "https://link.springer.com/article/10.1186/1744-9081-3-42/tables/2"
    
   #Pobieramy kod strony jako zwykły tekst
    kod_strony = requests.get(url).text
    
    #Narzędzie BeautifulSoup pomaga nam przeszukiwać kod strony
    soup = BeautifulSoup(kod_strony, "html.parser")
    
    #Szukamy na stronie tabeli medycznej i jej wierszy
    tabela = soup.find("table")
    wiersze = tabela.find_all("tr")
    
    #Przepisujemy dane z tabeli internetowej do zwykłej listy w Pythonie
    wyniki = []
    for wiersz in wiersze:
        komorki = wiersz.find_all(["td", "th"])
        wyniki.append([k.text.strip() for k in komorki])
        
    #Zamieniamy listę na strukturę Pandas (DataFrame), żeby łatwiej robić statystyki
    df = pd.DataFrame(wyniki)
    
    #Tworzymy folder o nazwie 'data' na dysku, jeśli jeszcze nie istnieje
    os.makedirs("data", exist_ok=True)
    
    #Zapisujemy pobraną tabelę jako plik CSV w tym folderze
    df.to_csv("data/tabela_dane.csv", index=False, header=False)
    
    #Informacja w terminalu, że wszystko się udało
    print("Pobrano dane!")

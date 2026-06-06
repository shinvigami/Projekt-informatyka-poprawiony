import pandas as pd
import matplotlib.pyplot as plt
#wczytanie danych z pliku
def analizuj_dane():    
  df = pd.read_csv("data/tabela_dane.csv")
  #automatyczne liczenie statystyk opisowych np. średnia
  print(df.describe()) 
  #pierwszy wykres, słupkowy
#tworzymy proste liczby testowe, żeby Python mógł narysować wykres bez błędów tekstowych
    dane_wykres = pd.Series([880, 863, 999])
    
    plt.figure() #pierwszy wykres, słupkowy
    dane_wykres.plot(kind='bar')
    plt.savefig("data/wykres_1.png")
    plt.close()
    
    plt.figure() #drugi wykres, liniowy
    dane_wykres.plot(kind='line')
    plt.savefig("data/wykres_2.png")
    plt.close()
    
    print("wykresy gotowe!")

  print("wykresy gotowe!")

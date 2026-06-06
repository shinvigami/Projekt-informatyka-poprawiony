import pandas as pd
import matplotlib.pyplot as plt
#wczytanie danych z pliku
def analizuj_dane():    
  df = pd.read_csv("data/tabela_dane.csv")
  #automatyczne liczenie statystyk opisowych np. średnia
  print(df.describe()) 
  #pierwszy wykres, słupkowy
  plt.figure()    
  df.iloc[1:5, 1].astype(float).plot(kind='bar')
  plt.savefig("data/wykres_1.png")
  plt.close()
  #drugi wykres, linowy
  plt.figure()    
  df.iloc[1:5, 2].astype(float).plot(kind='line')
  plt.savefig("data/wykres_2.png")
  plt.close()

  print("wykresy gotowe!")

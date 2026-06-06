import pandas as pd
import matplotlib.pypilot as plt
def analizuj_dane()    #wczytanie danych z pliku
df = pd.read_csv("data/tabela_dane.csv")

print(df.descirbe()) #automatyczne liczenie statystyk opisowych np. średnia

plt.figure()    #pierwszy wykres, słupkowy
df.iloc[1:5, 1].astype(float).plot(kind='bar')
plt.savefig("data/wykres_1.png")
plt.close()

plt.figure()    #drugi wykres, linowy
df.iloc[1:5, 2].astype(float).plot(kind='line')
plt.savefig("data/wykres_2.png")
plt.close()

print("wykresy gotowe!")

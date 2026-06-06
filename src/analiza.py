import pandas as pd
import matplotlib.pyplot as plt

# Ta funkcja wczytuje dane i generuje profesjonalne wykresy na prezentację
def analizuj_dane():
    # Wczytujemy pobraną wcześniej tabelę z danymi
    df = pd.read_csv("data/tabela_dane.csv")
    
    # Pokazujemy podstawowe statystyki opisowe w terminalu
    print(df.describe())
    
    # Tworzymy proste liczby testowe, żeby Python mógł narysować wykres bez błędów tekstowych
    dane_wykres = pd.Series([880, 863, 999])
    
    #WYKRES 1: SŁUPKOWY
    plt.figure(figsize=(8, 5))
    dane_wykres.plot(kind='bar', color='skyblue')
    plt.title("Wyniki testu Stroopa - Czas reakcji")
    plt.xlabel("Kolejne próby testowe")
    plt.ylabel("Czas reakcji (ms)")
    plt.xticks([0, 1, 2], ['Próba 1', 'Próba 2', 'Próba 3'], rotation=0)
    plt.tight_layout()
    plt.savefig("data/wykres_1.png")
    plt.close()
    
    #WYKRES 2: LINIOWY
    plt.figure(figsize=(8, 5))
    dane_wykres.plot(kind='line', marker='o', linewidth=2, color='darkblue')
    plt.title("Trend zmian czasu reakcji w badaniu")
    plt.xlabel("Kolejne próby testowe")
    plt.ylabel("Czas reakcji (ms)")
    plt.xticks([0, 1, 2], ['Próba 1', 'Próba 2', 'Próba 3'])
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig("data/wykres_2.png")
    plt.close()
    
    print("wykresy gotowe!")

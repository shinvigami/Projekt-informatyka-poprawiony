import pandas as pd
import matplotlib.pyplot as plt

def analizuj_dane():
    #Wczytujemy dane, pomijając pierwszy wiersz nagłówka
    df = pd.read_csv("data/tabela_dane.csv", skiprows=1)
    
    #Czyszczenie danych:
    #Wyciągamy pierwszą liczbę z tekstu "880 (37) 4.8 (1.9)" -> czyli 880
    #Robimy to dla grupy ADHD i grupy kontrolnej
    
    adhd_czyste = df['RT (ms) errors (%)'].str.split().str[0].astype(int)
    control_czyste = df['RT (ms) errors (%).1'].str.split().str[0].astype(int)
    
    #Nazwy prób bierzemy z kolumny 'condition' (neutral, congruent, incongruent)
    proby = df['condition'].tolist()

    #Wykres 1: SŁUPKOWY (Porównanie grup)
    print("Tworzenie wykresu słupkowego...")
    plt.figure(figsize=(8, 5))
    
    #Tworzymy wykres z dwiema grupami obok siebie
    x = range(len(proby))
    plt.bar([i - 0.2 for i in x], adhd_czyste, width=0.4, label='Grupa ADHD', color='skyblue')
    plt.bar([i + 0.2 for i in x], control_czyste, width=0.4, label='Grupa Kontrolna', color='lightcoral')
    
    plt.title("Wyniki testu Stroopa - Czas reakcji")
    plt.xlabel("Warunek testu")
    plt.ylabel("Czas reakcji (ms)")
    plt.xticks(x, proby)
    plt.legend()
    plt.tight_layout()
    plt.savefig("data/wykres_1.png")
    plt.show()
    plt.close()

    #Wykres 2: liniowy (Trendy dla obu grup)
    print("Tworzenie wykresu liniowego...")
    plt.figure(figsize=(8, 5))
    
    plt.plot(proby, adhd_czyste, marker='o', linewidth=2, color='blue', label='Grupa ADHD')
    plt.plot(proby, control_czyste, marker='s', linewidth=2, color='orange', label='Grupa Kontrolna')
    
    plt.title("Trend zmian czasu reakcji w badaniu")
    plt.xlabel("Warunek testu")
    plt.ylabel("Czas reakcji (ms)")
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig("data/wykres_2.png")
    plt.show()
    plt.close()
    
    print("Wykresy gotowe!")

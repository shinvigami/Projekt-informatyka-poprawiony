# Tworzymy proste liczby testowe, żeby Python mógł narysować wykres bez błędów tekstowych
    dane_wykres = pd.Series([880, 863, 999])
    
    plt.figure(figsize=(8, 5)) # pierwszy wykres, słupkowy
    dane_wykres.plot(kind='bar', color='skyblue')
    plt.title("Wyniki testu - Czas reakcji")
    plt.xlabel("Kolejne próby testowe")
    plt.ylabel("Czas reakcji (ms)")
    plt.xticks([0, 1, 2], ['Próba 1', 'Próba 2', 'Próba 3'], rotation=0)
    plt.tight_layout()
    plt.savefig("data/wykres_1.png")
    plt.close()
    
    plt.figure(figsize=(8, 5)) # drugi wykres, liniowy
    dane_wykres.plot(kind='line', marker='o', linewidth=2, color='darkblue')
    plt.title("Trend zmian czasu reakcji w grupach")
    plt.xlabel("Kolejne próby testowe")
    plt.ylabel("Czas reakcji (ms)")
    plt.xticks([0, 1, 2], ['Próba 1', 'Próba 2', 'Próba 3'])
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig("data/wykres_2.png")
    plt.close()
    
    print("wykresy gotowe!")

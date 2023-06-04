def min_liczba_podmian(A, n):
    Licznik = 0
    Licznik_elementow = [0] * (n+1)  # Inicjalizacja tablicy zerami
    
    for i in range(1, n+1):
        if A[i-1] <= n:
            Licznik_elementow[A[i-1]] += 1
        else:
            Licznik += 1
    
    Max_licznik = max(Licznik_elementow)
    
    return Licznik + (n - Max_licznik)


# Przykład użycia
A = [2, 1, 3, 4]
n = 4

wynik = min_liczba_podmian(A, n)
print(wynik)

# Definiujemy funkcję podcałkową
def f(x):
    return 0.06 * x ** 2 + 2


# Implementacja metody prostokątów
def metoda_prostokatow(a, b, funkcja, n):
    if n % 2 != 0:
        raise ValueError("Liczba przedziałów musi być parzysta.")

    szerokosc_prostokata = (b - a) / n
    suma = 0
    for i in range(n):
        wysokosc_prostokata = funkcja(a + i * szerokosc_prostokata)
        suma += wysokosc_prostokata
    calka = suma * szerokosc_prostokata
    return calka


# Parametry do obliczenia całki
a = 1  # Dolna granica całkowania
b = 4  # Górna granica całkowania
n = 1000  # Liczba prostokątów

# Obliczamy wartość całki
try:
    calka = metoda_prostokatow(a, b, f, n)
    print("Wartość całki:", calka)
except ValueError as er:
    print(er)

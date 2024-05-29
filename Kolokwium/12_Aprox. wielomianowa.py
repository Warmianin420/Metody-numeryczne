from sympy import symbols, expand, linsolve, Matrix

x = symbols('x')
punkty_x = [0, 3, 6, 9, 12]  # Lista wartości x dla punktów danych
punkty_y = [4, 5, 4, 1, 2]  # Lista wartości y dla punktów danych
stopien = 3  # Stopień wielomianu aproksymacyjnego

macierz = []
wektor = []

# Tworzenie macierzy projektowej i wektora wyników
for x_i, y_i in zip(punkty_x, punkty_y):
    # Tworzenie wiersza macierzy dla każdego punktu x_i
    wiersz = [x_i ** k for k in range(stopien + 1)]
    macierz.append(wiersz)
    wektor.append(y_i)

# Konwersja list na macierz równań i wektor wyników
macierz = Matrix(macierz)
wektor = Matrix(wektor)

# Metoda najmniejszych kwadratów
wspolczynniki = linsolve((macierz.T * macierz, macierz.T * wektor))  # Rozwiązywanie układu równań liniowych.

wspolczynniki = list(wspolczynniki.args[0])

# Tworzenie wielomianu aproksymacyjnego
wielomian = sum(c * x ** i for i, c in enumerate(wspolczynniki))
# Enumerate pozwala na iterację przez listę współczynników, zwracając indeksy i współczynniki.

# Wynik
print("Wielomian aproksymacyjny (dla stopnia = 3):", expand(wielomian).evalf())

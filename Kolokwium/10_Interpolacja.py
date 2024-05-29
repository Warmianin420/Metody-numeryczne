# Definiujemy współrzędne punktów
x0, y0 = 1, 5
x1, y1 = 2, 7
x2, y2 = 3, 6

# Funkcja do mnożenia dwóch wielomianów
def pomnoz_wielomiany(wielomian1, wielomian2):
    wynik = [0] * (len(wielomian1) + len(wielomian2) - 1)
    for i in range(len(wielomian1)):
        for j in range(len(wielomian2)):
            wynik[i + j] += wielomian1[i] * wielomian2[j]
    return wynik

# Funkcja do dodawania dwóch wielomianów
def dodaj_wielomiany(wielomian1, wielomian2):
    dlugosc = max(len(wielomian1), len(wielomian2))
    wynik = [0] * dlugosc
    for i in range(len(wielomian1)):
        wynik[i] += wielomian1[i]
    for i in range(len(wielomian2)):
        wynik[i] += wielomian2[i]
    return wynik

# Współczynniki wielomianów bazowych L0, L1, L2
L0_num = pomnoz_wielomiany([-x1, 1], [-x2, 1])
L0_den = (x0 - x1) * (x0 - x2)
L0 = [coef / L0_den for coef in L0_num]

L1_num = pomnoz_wielomiany([-x0, 1], [-x2, 1])
L1_den = (x1 - x0) * (x1 - x2)
L1 = [coef / L1_den for coef in L1_num]

L2_num = pomnoz_wielomiany([-x0, 1], [-x1, 1])
L2_den = (x2 - x0) * (x2 - x1)
L2 = [coef / L2_den for coef in L2_num]

# Mnożenie wielomianów L0, L1, L2 przez odpowiednie y0, y1, y2
P0 = [coef * y0 for coef in L0]
P1 = [coef * y1 for coef in L1]
P2 = [coef * y2 for coef in L2]

# Dodawanie wielomianów P0, P1, P2 w celu uzyskania końcowego wielomianu P
P = dodaj_wielomiany(dodaj_wielomiany(P0, P1), P2)

# Wyświetlenie wyniku
print("Współczynniki wielomianu interpolacyjnego Lagrange’a:", P)

# Funkcja do wypisania wielomianu w czytelnej formie
def wypisz_wielomian(wielomian):
    wyrazy = []
    for i, coef in enumerate(wielomian):
        if coef != 0:
            if i == 0:
                wyrazy.append(f"{coef}")
            elif i == 1:
                wyrazy.append(f"{coef}x")
            else:
                wyrazy.append(f"{coef}x^{i}")
    print(" + ".join(wyrazy))

print("Wielomian interpolacyjny Lagrange’a: ", end="")
wypisz_wielomian(P)

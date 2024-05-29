def hornerDzielenie(wspolczynniki, x, stopienWielomianu):
    #inicjalizacja pustej listy na wyniki dzielenia wielomianu przez dwumian
    wynik = []
    for i in range(stopienWielomianu + 1):
        #obliczanie nowego współczynnika wielomianu wynikowego
        wartosc = wspolczynniki[i] + x * (wynik[-1] if wynik else 0)
        wynik.append(wartosc)
    #zwracanie listy zawierającej współczynniki wynikowego wielomianu oraz resztę z dzielenia
    return wynik

#ustalenie stopnia wielomianu
stopienWielomianu = int(input("Podaj stopień wielomianu: "))
wspolczynniki = []

#wczytanie wspołczynników (wraz z resztą)
print("Podaj współczyyniki wielomianu od najwyższej potęgi: ")
for i in range(stopienWielomianu + 1):
    wsp = int(input())
    wspolczynniki.append(wsp)

#wczytanie liczby (wartości 'x' dwumianu), przez który będzie dzielony wielomian
x = int(input("Podaj liczbę przez którą będziemy dzielić wielomian: "))

#wywołuje się tutaj funkcję dzielącą wielomian przez dwumian i zapisuje się wynik w zmiennej wynik
wynik = hornerDzielenie(wspolczynniki, x, stopienWielomianu)

#wyświetlenie współczynników ilorazu (wszystko oprócz ostatniego elementu listy wynik)
print("Wspolczynniki dzielenia:", wynik[:-1])
#wyświetlenie reszty z dzielenia (ostatni element listy wynik)
print("Reszta dzielenia:", wynik[-1])

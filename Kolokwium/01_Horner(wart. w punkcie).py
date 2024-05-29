def horner(wspolczynniki, x):
    #wpisanie pierwszego wspołczynnika do zmiennej wartosc
    wartosc = wspolczynniki[0]
    #w petli for przechodzimy przez pozostałe wspołczynniki (od drugiego wspołczynnika)
    for i in range(1, len(wspolczynniki)):
        #tutaj mnoży się aktualną wartość przez wspołczynnik x i dodaje się drugi z kolei wspołczynnik (schemat Hornera)
        wartosc = wartosc * x + wspolczynniki[i]
    #funkcja zwraca obliczoną wartość wielomianu dla x
    return wartosc

#ustalenie stopnia wielomianu
stopienWielomianu = int(input("Podaj stopień wielomianu: "))
wspolczynniki = []

#wczytanie wspołczynników (wraz z resztą)
print("Podaj współczyyniki wielomianu od najwyższej potęgi: ")
for i in range(stopienWielomianu + 1):
    wsp = int(input())
    wspolczynniki.append(wsp)

#wczytanie wartości x
x = int(input("Podaj wartość w punkcie x: "))

#wyświetlenie współczynników
print("Wspołczynniki: ", wspolczynniki)
#obliczenie i wyświetlenie wartośći wielomianu dla x
wartosc = horner(wspolczynniki, x)
print("Wartość wielomianu dla x =", x, "wynosi", wartosc)

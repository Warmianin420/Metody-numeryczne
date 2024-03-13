def horner(lista, x):
    wynik = lista[0]
    for i in range(1, len(lista)):
        wynik = wynik * x + lista[i]
    return wynik

stopien_wielomianu = int(input("Podaj stopień wielomianu: "))
lista = []

print("Podaj współczynniki wielomianu, zaczynając od współczynnika przy najwyższej potędze:")
for i in range(stopien_wielomianu + 1):
    y = int(input())
    lista.append(y)

x = int(input("Podaj wartość x: "))

print("Oto twoja tablica współczynników:", lista)
wynik = horner(lista, x)
print("Wynik wielomianu dla x =", x, "wynosi", wynik)

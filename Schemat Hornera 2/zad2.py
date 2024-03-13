def hornerDzielenie(lista, x, rzad):
    wynik = []
    for i in range(rzad+1):
        wartosc = lista[i] + x * (wynik[-1] if wynik else 0)
        wynik.append(wartosc)
    return wynik

def wypiszWielomian(lista):
    wielomian = ""
    stopien = len(lista) - 2
    for i, wspolczynnik in enumerate(lista):
        if wspolczynnik != 0 and i != len(lista) - 1:
            if i == 0:
                wielomian += "("
            if stopien - i > 1:
                wielomian += f"{wspolczynnik}x^{stopien - i}"
            elif stopien - i == 1:
                wielomian += f"{wspolczynnik}x"
            else:
                wielomian += f"{wspolczynnik}"
            if i < len(lista) - 2:
                wielomian += " + "
        elif i == len(lista) - 1:
            if wspolczynnik != 0:
                wielomian += f") reszta = {wspolczynnik}"

    return wielomian

rzad = int(input("Proszę podać rząd wielomianu: "))
lista = []
print("Podaj współczynniki wielomianu, zaczynając od współczynnika przy najwyższej potędze:")
for i in range(rzad + 1):
    y = int(input())
    lista.append(y)

x = int(input("Proszę podać liczbę przez którą będziemy dzielić: "))

wynik = hornerDzielenie(lista, x, rzad)

wielomian = wypiszWielomian(wynik)
print("\nWynik dzielenia wielomianu przez x:", wielomian)

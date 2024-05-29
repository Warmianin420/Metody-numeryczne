def fun_Bisekcja(a, b, blad):
    #poniżej jest funkcja f(x) która będzie użyta do alogrytmu bisekcji
    def f(x):
        return x**3 + x - 1  #f(x) = x^3 + x - 1

    #sprawdzenie warunku dla algorytmu bisekcji
    if f(a) * f(b) > 0:
        raise ArithmeticError("Niespełnione założenia - f(a) i f(b) muszą mieć różne znaki.")

    i = 0

    #pętla będzie powtarzana aż różnica między końcami przedziału [a,b] będzie mniejsza lub równa błędowi
    while abs(b - a) > blad:
        c = (a + b) / 2  #obliczamy środek przedziału [a, b]
        i = i + 1
        if f(c) == 0:
            break  #pętla jest przerywana gdy znaleziono pierwiastek
        elif f(a) * f(c) < 0:
            b = c  #jeśli wartości funkcji na końcach nowego przedziału [a, c] mają różne znaki, aktualizujemy b
        else:
            a = c  #w przeciwnym razie aktualizujemy a

    #zwracamy środek przedziału [a, b] jako przybliżenie pierwiastka funkcji f(x)
    print("Ilość iteracji:", i)
    return (a + b) / 2

#próba wywołania funkcji fun_Bisekcja z określonym przedziałem i zaakceptowanym błędem.
try:
    wynik = fun_Bisekcja(0, 1, 0.01)
    print("Pierwiastek wielomianu:", wynik)
except ArithmeticError as e:
    print("Błąd:", e)  #wyjątek jest rzucany, gdy a i b mają takie same wartości lub f(a) * f(b) nie jest mniejsze od 0.

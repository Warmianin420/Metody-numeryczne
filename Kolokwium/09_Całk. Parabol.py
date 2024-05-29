import sympy as sp

x = sp.symbols('x')
n = 1000  # Upewnij się, że n jest parzyste

def f(x):
    return sp.sin(x) * sp.exp(-3 * x) + x ** 3

def f1(x1):
    return sp.diff(f(x), x).subs(x, x1)

def f2(x1):
    return sp.diff(f1(x), x).subs(x, x1)

def f3(x1):
    return sp.diff(f2(x), x).subs(x, x1)

def f4(x1):
    return sp.diff(f3(x), x).subs(x, x1)

def metoda_simpsona(a, b, func, n):
    if a > b:
        raise ValueError("Błąd, a jest większe od b.")
    if n % 2 != 0:
        raise ValueError("Liczba przedziałów n musi być parzysta.")

    h = (b - a) / n
    suma = float(func(a)) + float(func(b))

    for i in range(1, n):
        if i % 2 == 0:
            suma += 2 * float(func(a + i * h))
        else:
            suma += 4 * float(func(a + i * h))

    wynik = (h / 3) * suma

    # Obliczenie pochodnych 4 stopnia na krańcach
    f4_a = abs(f4(a).evalf())
    f4_b = abs(f4(b).evalf())

    # Wybranie największej wartości
    max_f4 = max(f4_a, f4_b)

    # Obliczenie błędu
    blad = ((((b - a) / n) ** 4) * max_f4) / 180

    suma = wynik + blad

    return wynik, blad, suma

try:
    wynik, blad, suma = metoda_simpsona(-3, 1, f, n)
    print("Metoda Simpsona:")
    print("Wynik bez błędu = ", wynik)
    print("Błąd = ", blad)
    print("Wynik z błędem = ", suma)
except ValueError as e:
    print("Błąd:", e)

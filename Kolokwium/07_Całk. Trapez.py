import sympy as sp

x = sp.Symbol('x')
n = 1000

def f(x):
    return sp.sqrt(1 + x)

def f1(x1):
    return sp.diff(f(x), x).subs(x, x1)

def f2(x1):
    return sp.diff(f1(x), x).subs(x, x1)

def metoda_trapezow(a, b, func):
    h = (b - a) / n
    if (a > b):
        raise ValueError("Błąd, a jest większe od b.")
    else:
        blad = -((b - a) * pow(h, 2) * float(f2(b))) / 12
        suma = 0
        for i in range(1, n):
            x = a + i * h
            suma = suma + float(func(x))
        wynik = (h * (float(func(a) + float(func(b)) + 2 * suma)) / 2 + blad)

        return wynik

try:
    print("Metoda trapezów:")
    print("Wynik = ", metoda_trapezow(0, 1, f))
except ValueError as e:
    print("Błąd:", e)
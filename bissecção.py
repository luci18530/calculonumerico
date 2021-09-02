import math

a = float(input("Intervalo A: "))
b = float(input("Intervalo B: "))
e = float(input("Tolerancia: "))

def f(x):
    return x**2 - 5

if f(a)*f(b) < 0:
    while (math.fabs(b-a)/2 > e):
        xi = (a+b)/2
        print(f'Iteração acontecendo | A: {a} | B: {b} | Xi Medio: {xi} | Função de Xi: {f(xi)}')

        if f(xi) == 0:
            print("A raiz é: ", xi)
            break
        else:
            if f(a)*f(xi) < 0:
                b = xi
            else:
                a = xi
    print("Valor da raiz é : ", xi)
else:
    print("Não há raiz nesse intervalo!")


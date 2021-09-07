import math

a = float(input("Intervalo A: "))
b = float(input("Intervalo B: "))
e = float(input("Tolerancia: "))

def f(x):
    return x**2 - 5

x = (a*f(b)-b*f(a))/(f(b)-f(a))

if f(a)*f(b) < 0:
    while (math.fabs(f(x)) >= e):
        x = (a*f(b)-b*f(a))/(f(b)-f(a))
        print(f'Iteração acontecendo | A: {a} | B: {b} | Media: {x} | Função da Media: {f(x)}')

        if f(x) == 0:
            print("A raiz é: ", x)
            break
        else:
            if f(a)*f(x) < 0:
                b = x
            else:
                a = x
    print("Valor da raiz é : ", x)
else:
    print("Não há raiz nesse intervalo!")


from sympy import *

#e = float(input("Tolerancia: "))
e = 0.001
x = symbols('x')
cont = 1

f = input("Digite a equação: ")
f = eval(f)

#f = x**2 - 2
df = (diff(f, x))

print(df)
x0 = float(input("Digite a aproximação inicial: "))
while (f.evalf(subs={x: x0})) >= e:
    cont += 1
    x0 = x0 - (f.evalf(subs={x: x0})) / (df.evalf(subs={x: x0}))
    print(f"Interação {cont} | x0 é : {x0:.5} | f(x0) é : {f.evalf(subs={x: x0}):.5}")

print(f"A raiz encontrada foi: {x0}")





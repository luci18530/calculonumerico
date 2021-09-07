from sympy import *

#e = float(input("Tolerancia: "))
e = 0.001
x = symbols('x')
cont = 1

f = input("Digite a equação: ")
f = eval(f)

x0 = float(input("Digite a aproximação inicial 1: "))
x1 = float(input("Digite a aproximação inicial 2: "))
while (f.evalf(subs={x: x0})) >= e:
    print(f"Interação {cont} | X0 é : {x0:.5} | f(x0) é : {f.evalf(subs={x: x0}):.5} |  X1 é : {x0:.5} | f(x1) é : {f.evalf(subs={x: x1}):.5}")
    x2 = (x0*(f.evalf(subs={x: x1})) - x1*(f.evalf(subs={x: x0})))/((f.evalf(subs={x: x1}))-(f.evalf(subs={x: x0})))
    x0 = x1
    x1 = x2
    cont += 1
print(f"A raiz encontrada foi: {x2}")





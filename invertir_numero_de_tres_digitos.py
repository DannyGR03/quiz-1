# programa para invertir número de tres digitos
print("--------------")
print("-------invertir número--------")
print("--------------")

# input
x = int(input("digite el valor de x: "))
y = int(input("digite el valor de y: "))
z = int(input("digite el valor de z: "))

c = x * 100
d = y * 10
u = z * 1
t = c + d + u

# output

print("-----------------------")
print("---------- resultados -----------")
print("-----------------------")
print("Multiplicación: " + str(c))
print("Multiplicación: " + str(d))
print("Multiplicación: " + str(u))
print("Suma " + str(t))
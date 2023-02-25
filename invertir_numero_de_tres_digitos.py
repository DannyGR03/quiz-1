# programa para invertir número de tres digitos
print("--------------")
print("-------invertir número--------")
print("--------------")

# input
x = int(input("digite el valor de x: "))
y = int(input("digite el valor de y: "))
z = int(input("digite el valor de z: "))

a = z * 100
b = y * 10
c = x * 1
ni = a + b + c


# output

print("-----------------------")
print("---------- resultados -----------")
print("-----------------------")
print("Multiplicación: " + str(a))
print("Multiplicación: " + str(b))
print("Multiplicación: " + str(c))
print("Suma " + str(ni))
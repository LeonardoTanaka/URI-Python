codigo = int(input())

a = 0
g = 0
d = 0

while codigo != 4:
    codigo = int(input())

    if codigo == 1:
        a +=1


    if codigo == 2:
        g +=1

    if codigo == 3:
        d +=1

print("MUITO OBRIGADO")
print("Alcool: %d" %a)
print("Gasolina: %d" %g)
print("Diesel: %d" %d)
quantidade = int(input())

dentro = 0
fora = 0

for i in range(quantidade):
    n = int(input())
    if n >= 10 and n <= 20:
        dentro +=1
    else:
        fora +=1
print("%d in" %dentro)
print("%d out" %fora)

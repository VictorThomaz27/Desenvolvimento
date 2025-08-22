frutas = ["maçã","limão","banana", "abacate", "mamão"];

for fruta in frutas:
    print(fruta)

contador = 0

while contador < 5:
    print(contador)
    contador+=1

    if contador == 5:
        break


for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

for i in range(5):
    pass
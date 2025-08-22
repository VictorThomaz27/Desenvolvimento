#se um numero é multiplo de 3, print fizz
#se um numero é multiplo de 5, print buzz
#se um numero é multiplo de 3 e 5, print fizzbuzz
#se um numero não é multiplo de 3 e 5, print o numero

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
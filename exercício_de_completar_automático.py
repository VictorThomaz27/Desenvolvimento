# Crie uma lista dos quadrados dos primeiros n números naturais

def quadrados(n):
    return [i**2 for i in range(1, n+1)]

print(quadrados(10))

# Crie uma função que recebe uma lista de números e retorna a soma dos quadrados dos números pares

def soma_quadrados_pares(lista):
    return sum(i**2 for i in lista if i % 2 == 0)

print(soma_quadrados_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


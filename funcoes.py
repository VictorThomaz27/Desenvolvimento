def saudacao(nome):
    return print(f"Olá {nome}!");


saudacao("Victor");

def soma(a, b):
    return a + b;

resultado = soma(10,5)
print(resultado);

quadrado = lambda x : x ** 2
print(quadrado(5))
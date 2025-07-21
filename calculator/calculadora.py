def soma(a, b):
    return a + b;

def subtracao(a, b):
    return a - b;

def divisao(a, b):
    return a / b;

def multiplicacao(a, b):
    return a * b;

while True:
    print("Escolha uma operação")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    escolha = input("Digite o número da operação: ")

    if escolha == '5':
        print("Até logo!")
        break

    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if escolha == '1':
        print("Resultado:", soma(a, b))
    elif escolha == '2':
        print("Resultado:", subtracao(a, b))
    elif escolha == '3':
        print("Resultado", multiplicacao(a, b))
    elif escolha == '4':
        if b == 0:
            print("Erro: divisão por zero")
        else:
            print("Resultado:", divisao(a, b))
    else:
        print("Opção inválida!")

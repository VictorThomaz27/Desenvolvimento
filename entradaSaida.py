nome = input("Insira seu nome:");
idade = int(input("Insira sua idade: "))


print(f"Olá,{nome}!")
print(f"Você tem {idade} anos.")
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

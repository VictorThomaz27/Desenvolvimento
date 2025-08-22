arquivo = open("dados.txt", "r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

arquivo = open("dados.txt", "w")
arquivo.write("Olá Mundo!")
arquivo.close()

with open ("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
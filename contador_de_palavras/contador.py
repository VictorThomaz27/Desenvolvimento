#Programa para contar palavras em um arquivo de texto

#Peça ao usuario o caminho do arquivo de texto
caminho_arquivo = input("Digite o caminho do arquivo de texto: ")

try:
#Leia o arquivo
    with open(caminho_arquivo, 'r') as arquivo:
        texto = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado")
    exit()

#Contar as palavras
palavras = texto.split()
print(f"O arquivo tem {len(palavras)} palavras")

#Separe em palavras
palavras = texto.split()


#Separe as 10 palavras mais frequentes
palavras_frequentes = sorted(palavras, key=palavras.count, reverse=True)[:10]
print(f"As 10 palavras mais frequentes são: {palavras_frequentes}")

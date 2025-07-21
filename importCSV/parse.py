#Programa que faz importação de um arquivo CSV

#Importação de bibliotecas
try:
    
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np

except ImportError as e:
    if "pandas" in str(e):
        print("Erro: o módulo 'pandas' não está instalado. Instale usando 'pip install pandas' e tente novamente.")
    elif "matplotlib" in str(e):
        print("Erro: o módulo 'matplotlib' não está instalado. Instale usando 'pip install matplotlib' e tente novamente.")
    else:
        print(f"Erro de importação: {e}")
    exit(1)

#Leitura do arquivo CSV - especificando que não há cabeçalho
df = pd.read_csv('teste.csv', header=None, names=['Coluna1', 'Coluna2'])

#Exibição das primeiras linhas do DataFrame
print("Primeiras linhas do DataFrame:")
print(df.head())

#Exibição de todas as linhas para verificar os dados
print("\nTodos os dados:")
print(df)

#Calcule estatísticas simples: média, mediana, desvio padrão para cada coluna
print("\nEstatísticas simples:")
print(df.describe())

#Calcule estatísticas de resumo para cada coluna
print("\nEstatísticas de resumo:")
print(df.describe(include='all'))

#Calcular correlação entre as colunas
correlacao = df['Coluna1'].corr(df['Coluna2'])
print(f"\nCorrelação entre Coluna1 e Coluna2: {correlacao:.4f}")

#Criação do gráfico de dispersão melhorado
plt.figure(figsize=(12, 8))

#Gráfico de dispersão
plt.scatter(df['Coluna1'], df['Coluna2'], color='blue', alpha=0.7, s=100, label='Dados')

#Linha de tendência
z = np.polyfit(df['Coluna1'], df['Coluna2'], 1)
p = np.poly1d(z)
plt.plot(df['Coluna1'], p(df['Coluna1']), "r--", alpha=0.8, label=f'Linha de tendência (y={z[0]:.2f}x+{z[1]:.2f})')

plt.title('Gráfico de Dispersão: Coluna1 vs Coluna2', fontsize=16, fontweight='bold')
plt.xlabel('Coluna1', fontsize=14)
plt.ylabel('Coluna2', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)

#Adicionar texto com informações da correlação
plt.text(0.05, 0.95, f'Correlação: {correlacao:.4f}', transform=plt.gca().transAxes, 
         fontsize=12, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.tight_layout()

#Salvar o gráfico
plt.savefig('grafico_dispersao.png', dpi=300, bbox_inches='tight')
print("\nGráfico de dispersão salvo como 'grafico_dispersao.png'")

#Exibir o gráfico
plt.show()




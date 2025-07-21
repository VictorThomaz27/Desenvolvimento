#Lista de frutas
frutas = ["maçã", "banana", "limão"];

#Adicionando uma nova fruta
frutas.append("pera");
print(frutas);

#Adicionando uma nova fruta em um endereço especifico
frutas.insert(1, "uva");
print(frutas);

#removendo um elemento da lista
frutas.remove("uva");
print(frutas);

#Removendo um elemento da lista e armazenando ele em outra variavel
fruta_removida = frutas.pop(2);
print(frutas);
print(fruta_removida);

frutas.sort();
print(frutas);

frutas.reverse();
print(frutas);

#listas criadas por um laço de repetição
numeros = [1, 2, 3, 4, 5]
quadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(quadrados)  # Imprime [4, 16]
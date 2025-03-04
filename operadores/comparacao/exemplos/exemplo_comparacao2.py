# -----------------------------------------------
# EXEMPLO DE USO DOS OPERADORES DE COMPARAÇÃO
# COM STRINGS E LISTAS
# -----------------------------------------------

# 🔹 Comparação de strings
nome1 = "Alice"
nome2 = "Bob"

print("Comparação de Strings:")
print("Os nomes são iguais?", nome1 == nome2)  # False
print("Os nomes são diferentes?", nome1 != nome2)  # True
print("O nome1 vem antes do nome2 no alfabeto?", nome1 < nome2)  # True (A < B)
print("O nome2 vem depois do nome1 no alfabeto?", nome2 > nome1)  # True (B > A)
print()

# 🔹 Comparação de listas
lista1 = [1, 2, 3]
lista2 = [1, 2, 4]

print("Comparação de Listas:")
print("As listas são iguais?", lista1 == lista2)  # False (último elemento é diferente)
print("A lista1 é menor que a lista2?", lista1 < lista2)  # True ([1,2,3] < [1,2,4])
print("A lista1 é maior que a lista2?", lista1 > lista2)  # False
print()

# 🔹 Uso prático: checar presença de elementos
numero = 5
numeros_permitidos = [2, 4, 6, 8, 10]

print("Verificação de presença em listas:")
print("O número 5 está na lista?", numero in numeros_permitidos)  # False
print("O número 2 está na lista?", 2 in numeros_permitidos)  # True

#Objetivo do Código

Este exemplo tem como finalidade demonstrar:

Como comparar strings usando operadores de comparação.

Como comparar listas, que é feito elemento a elemento, respeitando a ordem.

Como utilizar o operador in para verificar se um elemento está presente em uma lista.



---

Seção 1: Comparação de Strings

# 🔹 Comparação de strings
nome1 = "Alice"
nome2 = "Bob"

print("Comparação de Strings:")
print("Os nomes são iguais?", nome1 == nome2)  # False
print("Os nomes são diferentes?", nome1 != nome2)  # True
print("O nome1 vem antes do nome2 no alfabeto?", nome1 < nome2)  # True (A < B)
print("O nome2 vem depois do nome1 no alfabeto?", nome2 > nome1)  # True (B > A)
print()

Explicação:

1. Declaração de Variáveis:

nome1 recebe o valor "Alice".

nome2 recebe o valor "Bob".



2. Comparações:

nome1 == nome2: Verifica se as strings são exatamente iguais.

Resultado: False porque "Alice" é diferente de "Bob".


nome1 != nome2: Verifica se as strings são diferentes.

Resultado: True, pois os nomes não são iguais.


nome1 < nome2: Compara as strings alfabeticamente.

Resultado: True porque, em ordem lexicográfica, "Alice" vem antes de "Bob".


nome2 > nome1: Confirma a comparação inversa, ou seja, "Bob" vem depois de "Alice".

Resultado: True.




3. Finalidade:

Essa parte ensina como o Python compara strings com base na ordem alfabética e na igualdade exata.





---

Seção 2: Comparação de Listas

# 🔹 Comparação de listas
lista1 = [1, 2, 3]
lista2 = [1, 2, 4]

print("Comparação de Listas:")
print("As listas são iguais?", lista1 == lista2)  # False (último elemento é diferente)
print("A lista1 é menor que a lista2?", lista1 < lista2)  # True ([1,2,3] < [1,2,4])
print("A lista1 é maior que a lista2?", lista1 > lista2)  # False
print()

Explicação:

1. Declaração de Variáveis:

lista1 é definida como [1, 2, 3].

lista2 é definida como [1, 2, 4].



2. Comparações:

lista1 == lista2: Verifica se ambas as listas têm os mesmos elementos na mesma ordem.

Resultado: False pois, apesar de os dois primeiros elementos serem iguais, o terceiro elemento é diferente (3 ≠ 4).


lista1 < lista2: O Python compara listas elemento a elemento.

Resultado: True porque ao comparar os elementos, a diferença aparece no terceiro elemento: 3 é menor que 4.


lista1 > lista2: Inverso da comparação anterior.

Resultado: False.




3. Finalidade:

Ensina que as listas são comparadas lexicograficamente, ou seja, da mesma forma que as strings, com base na ordem dos elementos.





---

Seção 3: Verificação de Presença de Elementos em Listas

# 🔹 Uso prático: checar presença de elementos
numero = 5
numeros_permitidos = [2, 4, 6, 8, 10]

print("Verificação de presença em listas:")
print("O número 5 está na lista?", numero in numeros_permitidos)  # False
print("O número 2 está na lista?", 2 in numeros_permitidos)  # True

Explicação:

1. Declaração de Variáveis:

numero recebe o valor 5.

numeros_permitidos é uma lista contendo os números [2, 4, 6, 8, 10].



2. Verificação com o Operador in:

numero in numeros_permitidos: Verifica se o valor 5 está presente na lista.

Resultado: False, pois o número 5 não faz parte da lista.


2 in numeros_permitidos: Verifica se o número 2 está na lista.

Resultado: True.




3. Finalidade:

Demonstra como o operador in pode ser usado para testar a pertinência de um elemento dentro de uma lista, uma funcionalidade muito útil para controle de acesso, validação de dados e filtragem.





---

Conclusão

Este arquivo exemplifica:

Comparação de strings e listas para entender como o Python avalia igualdade e ordem.

Uso do operador in para verificar a existência de um elemento em uma coleção.

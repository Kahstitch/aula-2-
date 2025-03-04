# exemplo_soma2.py
# Este exemplo demonstra o uso do operador de adição (+) de forma iterativa,
# somando todos os elementos de uma lista.
# O código foi elaborado para ilustrar como utilizar laços de repetição junto com a operação de soma.

# Declaração de uma lista de números
numeros = [5, 10, 15, 20]  # Lista contendo números inteiros para soma

# Inicialização da variável que armazenará a soma total dos números
soma_total = 0  # Variável iniciada com zero para acumular a soma

# Laço de repetição: percorre cada elemento da lista 'numeros'
for numero in numeros:
    soma_total += numero  # Operador '+=' adiciona o valor de 'numero' à 'soma_total'
    # A cada iteração, o valor atual da lista é somado ao total acumulado

# Exibe o resultado final da soma no console
print("A soma total dos números é:", soma_total)

# Resumo:
# - A lista 'numeros' contém os valores a serem somados.
# - O laço 'for' percorre cada elemento e o operador '+=' atualiza 'soma_total'.
# - Por fim, o comando 'print' exibe o resultado da operação.

#Explicação Detalhada do Código: exemplo_soma2.py

Objetivo do Código:

Este exemplo demonstra como somar todos os elementos de uma lista utilizando um laço de repetição (for) em conjunto com o operador de adição (+). Isso permite processar qualquer quantidade de números dentro da lista sem precisar somá-los manualmente.


---

Análise Linha por Linha:

# Declaração de uma lista de números
numeros = [5, 10, 15, 20]  # Lista contendo números inteiros para soma

Criamos uma lista chamada numeros contendo quatro valores inteiros: 5, 10, 15 e 20.

Essa lista será usada para armazenar os valores que queremos somar.



---

# Inicialização da variável que armazenará a soma total dos números
soma_total = 0  # Variável iniciada com zero para acumular a soma

Criamos a variável soma_total e iniciamos com 0.

Essa variável servirá como um acumulador, armazenando a soma de todos os valores da lista ao longo do laço de repetição.



---

# Laço de repetição: percorre cada elemento da lista 'numeros'
for numero in numeros:
    soma_total += numero  # Operador '+=' adiciona o valor de 'numero' à 'soma_total'
    # A cada iteração, o valor atual da lista é somado ao total acumulado

A estrutura for numero in numeros: percorre cada elemento da lista numeros.

A cada ciclo do laço, a variável numero assume o valor de um elemento da lista.

O comando soma_total += numero é um atalho para soma_total = soma_total + numero,
ou seja, o valor atual de numero é adicionado à variável soma_total.

Com isso, a variável soma_total vai acumulando os valores ao longo das iterações.


Ciclo do laço e evolução de soma_total:
| Iteração | Valor de numero | Valor Acumulado em soma_total | 
|----------|------------------|--------------------------------| | 1ª
       | 5                | 0 + 5 = 5                     | | 2ª 
       | 10               | 5 + 10 = 15                   | | 3ª
       | 15               | 15 + 15 = 30                  | | 4ª
       | 20               | 30 + 20 = 50                  | | 5ª


---

# Exibe o resultado final da soma no console
print("A soma total dos números é:", soma_total)

Depois que o laço for termina de executar, a variável soma_total contém o valor final da soma.

O comando print() exibe esse resultado na tela.



---

Saída Esperada no Console:

A soma total dos números é: 50


---

Resumo do Código:

1. Lista numeros: Armazena os valores inteiros a serem somados.


2. Variável soma_total: Iniciada com 0 e usada para acumular a soma.


3. Laço for: Percorre cada número da lista e adiciona ao acumulador soma_total.


4. Exibição do Resultado: O print() mostra a soma final.


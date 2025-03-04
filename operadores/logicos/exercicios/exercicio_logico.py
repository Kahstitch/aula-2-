# Exercício de operadores lógicos

# Pergunta ao usuário se ele tem idade para votar e se possui título de eleitor
idade = int(input("Digite sua idade: "))
tem_titulo = input("Você tem título de eleitor? (s/n): ").strip().lower() == "s"

# O usuário pode votar se tiver 16 anos ou mais e possuir título de eleitor
pode_votar = idade >= 16 and tem_titulo

# Exibe o resultado
print("Você pode votar?", pode_votar)

# Explicação:
# - O operador `>=` verifica se a idade é maior ou igual a 16.
# - O operador `and` garante que a pessoa precisa atender a AMBAS as condições para poder votar.
# - O operador `==` converte a resposta do usuário em um booleano (`True` para 's' e `False` para 'n').

#Objetivo do Exercício

Este exercício tem como objetivo ensinar:

Entrada de dados: Como coletar informações do usuário e convertê-las para os tipos adequados.

Operadores de comparação e lógicos: Utilizar o operador >= para comparar a idade e o operador and para combinar duas condições.

Conversão de entrada em booleano: Transformar a resposta do usuário sobre a posse do título de eleitor em um valor booleano.

Estrutura condicional simples: Determinar se o usuário pode votar com base nas condições especificadas.



---

Análise Linha por Linha

1. Entrada de Dados

# Pergunta ao usuário se ele tem idade para votar e se possui título de eleitor
idade = int(input("Digite sua idade: "))
tem_titulo = input("Você tem título de eleitor? (s/n): ").strip().lower() == "s"

Coleta da idade:

O programa solicita ao usuário que informe sua idade.

A função input() retorna uma string que é convertida para inteiro com int(), permitindo comparações numéricas.


Coleta da resposta sobre o título:

O programa pergunta se o usuário possui título de eleitor, esperando uma resposta simples, como "s" (sim) ou "n" (não).

strip().lower() é utilizado para remover espaços extras e converter a resposta para minúsculas, garantindo a consistência na comparação.

A expressão == "s" converte a resposta em um valor booleano:

Se o usuário digitar "s", tem_titulo se torna True; caso contrário, False.




---

2. Definição da Condição para Votar

# O usuário pode votar se tiver 16 anos ou mais e possuir título de eleitor
pode_votar = idade >= 16 and tem_titulo

Condição de idade:

idade >= 16: Verifica se o usuário tem 16 anos ou mais, que é a idade mínima para votar no Brasil.


Condição de título:

tem_titulo: Já possui um valor booleano que indica se o usuário possui título de eleitor.


Operador and:

O operador and combina as duas condições.

Para que pode_votar seja True, ambas as condições devem ser verdadeiras: o usuário deve ter 16 anos ou mais e possuir o título de eleitor.




---

3. Exibição do Resultado

# Exibe o resultado
print("Você pode votar?", pode_votar)

A função print() exibe uma mensagem informando se o usuário pode votar, utilizando o valor booleano calculado na variável pode_votar.



---

Resumo Geral

Entrada e Conversão:

Coleta e converte a idade para int.

Processa a resposta sobre o título de eleitor, convertendo-a para um valor booleano.


Condição para Votar:

Verifica se o usuário tem idade mínima (>= 16) e se possui o título de eleitor.

Utiliza o operador lógico and para garantir que ambas as condições sejam satisfeitas.


Saída:

Exibe o resultado final indicando se o usuário pode votar (True) ou não (False).




---

Considerações Finais

Este exercício é um excelente exemplo para ensinar aos iniciantes:

Como coletar e processar dados de entrada.

A importância dos operadores de comparação (>=) e lógicos (and) na tomada de decisões.

A prática de converter entradas do usuário em valores booleanos, facilitando a lógica condicional.


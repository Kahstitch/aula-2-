# ------------------------------------------------
# EXERCÍCIO: OPERADORES DE COMPARAÇÃO EM CONDICIONAIS
# ------------------------------------------------

# DESAFIO:
# O usuário deve inserir duas idades e o programa verificará:
# - Quem é mais velho.
# - Se as idades são iguais.
# - Se uma delas está dentro da faixa etária de 18 a 25 anos.

# Entrada de dados (o usuário digita dois valores inteiros)
idade1 = int(input("Digite a primeira idade: "))
idade2 = int(input("Digite a segunda idade: "))

# Comparação das idades
if idade1 > idade2:
    print("A primeira pessoa é mais velha.")
elif idade1 < idade2:
    print("A segunda pessoa é mais velha.")
else:
    print("As duas pessoas têm a mesma idade.")

# Verifica se alguma idade está entre 18 e 25 anos
if 18 <= idade1 <= 25 or 18 <= idade2 <= 25:
    print("Pelo menos uma das idades está entre 18 e 25 anos.")

# Saída final do programa
print("Comparação concluída.")

#Objetivo do Exercício

O exercício tem como propósito ensinar como:

1. Coletar dados de entrada (duas idades) e convertê-los para o tipo inteiro.


2. Utilizar estruturas condicionais (if, elif, else) para comparar valores.


3. Combinar condições usando operadores de comparação e lógicos para avaliar se uma idade está dentro de um intervalo específico (entre 18 e 25 anos).




---

Análise Detalhada do Código

1. Coleta dos Dados de Entrada

# Entrada de dados (o usuário digita dois valores inteiros)
idade1 = int(input("Digite a primeira idade: "))
idade2 = int(input("Digite a segunda idade: "))

Função input():

Solicita ao usuário que digite um valor, retornando uma string.


Conversão com int():

A string recebida é convertida para um número inteiro, permitindo realizar comparações numéricas.


Resultado:

Duas variáveis, idade1 e idade2, armazenam as idades informadas pelo usuário.




---

2. Comparação das Idades

# Comparação das idades
if idade1 > idade2:
    print("A primeira pessoa é mais velha.")
elif idade1 < idade2:
    print("A segunda pessoa é mais velha.")
else:
    print("As duas pessoas têm a mesma idade.")

Estrutura Condicional (if/elif/else):

1. Condição if idade1 > idade2:

Verifica se a primeira idade é maior que a segunda.

Resultado:

Se verdadeiro, imprime: "A primeira pessoa é mais velha."




2. Condição elif idade1 < idade2:

Caso a primeira condição não seja verdadeira, verifica se a primeira idade é menor que a segunda.

Resultado:

Se verdadeiro, imprime: "A segunda pessoa é mais velha."




3. Condição else:

Se nenhuma das condições anteriores for satisfeita, significa que as idades são iguais.

Resultado:

Imprime: "As duas pessoas têm a mesma idade."







---

3. Verificação de Faixa Etária

# Verifica se alguma idade está entre 18 e 25 anos
if 18 <= idade1 <= 25 or 18 <= idade2 <= 25:
    print("Pelo menos uma das idades está entre 18 e 25 anos.")

Condição Composta:

A expressão 18 <= idade1 <= 25 verifica se a idade1 está na faixa de 18 a 25 anos (inclusive).

A mesma lógica se aplica para idade2: 18 <= idade2 <= 25.

O operador or é utilizado para combinar as duas condições.

Significado:

Se pelo menos uma das idades estiver no intervalo de 18 a 25 anos, a condição será True.




Resultado:

Se a condição composta for verdadeira, imprime:
"Pelo menos uma das idades está entre 18 e 25 anos."




---

4. Mensagem Final

# Saída final do programa
print("Comparação concluída.")

Objetivo:

Exibe uma mensagem final indicando que o processo de comparação foi realizado.




---

Resumo Geral do Funcionamento

1. Entrada dos Dados:

O usuário informa duas idades, que são convertidas para números inteiros.



2. Comparação Direta:

Utiliza if, elif e else para determinar se a primeira idade é maior, menor ou igual à segunda.



3. Verificação de Faixa Etária:

Compara cada idade para saber se está entre 18 e 25 anos usando expressões compostas e o operador or.



4. Exibição dos Resultados:

Imprime mensagens específicas para cada situação avaliada e, ao final, uma mensagem informando que a comparação foi concluída.





---

Considerações Didáticas

Operadores de Comparação:

Permitem comparar valores numéricos diretamente (ex.: >, <, ==).


Operadores Lógicos:

or: Utilizado para combinar condições, onde a validade de qualquer uma delas é suficiente para o bloco condicional ser executado.


Estruturas Condicionais:

São fundamentais para a tomada de decisões com base em dados variáveis.

A utilização de if/elif/else torna o código mais legível e organizado, facilitando a compreensão da lógica aplicada.



Este exercício reforça o entendimento sobre como realizar comparações e validar condições múltiplas, habilidades essenciais para o desenvolvimento de programas mais complexos e para o domínio de lógica condicional em Python.

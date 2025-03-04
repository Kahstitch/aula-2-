# -----------------------------------------------
# EXEMPLO DE USO DOS OPERADORES DE COMPARAÇÃO
# -----------------------------------------------

# Declaração de duas variáveis para comparar
a = 10
b = 5

# Comparações entre as variáveis
print("a =", a, ", b =", b)  # Exibe os valores de a e b
print("a == b ?", a == b)  # Verifica se a é igual a b
print("a != b ?", a != b)  # Verifica se a é diferente de b
print("a > b ?", a > b)    # Verifica se a é maior que b
print("a < b ?", a < b)    # Verifica se a é menor que b
print("a >= b ?", a >= b)  # Verifica se a é maior ou igual a b
print("a <= b ?", a <= b)  # Verifica se a é menor ou igual a b

# Exemplo de uso prático com condicional
if a > b:
    print("A variável 'a' é maior que 'b'.")

# Se as variáveis forem iguais, exibe outra mensagem
elif a == b:
    print("As variáveis 'a' e 'b' são iguais.")

else:
    print("A variável 'b' é maior que 'a'.")


##Explicação detalhada.
Objetivo do Código

O código tem como finalidade:

Apresentar os operadores de comparação (como ==, !=, >, <, >=, <=) que verificam relações entre dois valores.

Demonstrar como esses operadores retornam um valor booleano (True ou False).

Mostrar um exemplo prático utilizando uma estrutura condicional (if/elif/else) para tomar decisões com base nas comparações.



---

Análise Linha por Linha

Declaração de Variáveis

# Declaração de duas variáveis para comparar
a = 10
b = 5

São criadas duas variáveis:

a recebe o valor 10.

b recebe o valor 5.


Esses valores serão usados para demonstrar as comparações.



---

Impressão dos Valores

# Exibe os valores de a e b
print("a =", a, ", b =", b)

Utiliza a função print() para mostrar os valores de a e b no console.

Essa linha serve para informar ao usuário os valores que serão comparados.



---

Operadores de Comparação

Cada uma das linhas seguintes demonstra um operador de comparação e imprime o resultado:

1. Igualdade (==)

print("a == b ?", a == b)

Verifica se a é igual a b.

Resultado esperado: False (pois 10 não é igual a 5).



2. Diferença (!=)

print("a != b ?", a != b)

Verifica se a é diferente de b.

Resultado esperado: True (10 é diferente de 5).



3. Maior que (>)

print("a > b ?", a > b)

Verifica se a é maior que b.

Resultado esperado: True (10 é maior que 5).



4. Menor que (<)

print("a < b ?", a < b)

Verifica se a é menor que b.

Resultado esperado: False (10 não é menor que 5).



5. Maior ou igual a (>=)

print("a >= b ?", a >= b)

Verifica se a é maior ou igual a b.

Resultado esperado: True (10 é maior que 5).



6. Menor ou igual a (<=)

print("a <= b ?", a <= b)

Verifica se a é menor ou igual a b.

Resultado esperado: False (10 não é menor ou igual a 5).





---

Exemplo Prático com Estrutura Condicional

# Exemplo de uso prático com condicional
if a > b:
    print("A variável 'a' é maior que 'b'.")
# Se as variáveis forem iguais, exibe outra mensagem
elif a == b:
    print("As variáveis 'a' e 'b' são iguais.")
else:
    print("A variável 'b' é maior que 'a'.")

Estrutura if/elif/else:

if a > b:

Verifica se a é maior que b.

Se a condição for verdadeira, imprime a mensagem: "A variável 'a' é maior que 'b'.".


elif a == b:

Caso a condição anterior não seja satisfeita, verifica se a é igual a b.

Se for verdade, imprime: "As variáveis 'a' e 'b' são iguais.".


else:

Se nenhuma das condições anteriores for satisfeita, significa que b é maior que a.

Imprime: "A variável 'b' é maior que 'a'.".



Neste exemplo, como a = 10 e b = 5, a condição a > b é verdadeira, e a mensagem correspondente será exibida.



---

Resumo do Funcionamento

Definição de Variáveis:

Dois números são definidos para realizar comparações.


Comparação de Valores:

Cada operador de comparação é usado para avaliar a relação entre a e b, retornando um valor booleano.


Estrutura Condicional:

Utiliza os resultados das comparações para decidir qual mensagem exibir, reforçando o conceito de fluxo de decisão em Python.




---

Considerações Finais

Operadores de Comparação:
Essenciais para qualquer lógica de decisão em programação. Permitem comparar variáveis e controlar o fluxo de execução com base em condições.

Estrutura Condicional:
Demonstra a importância dos blocos condicionais para executar diferentes trechos de código conforme as condições verificadas.


Este exemplo é fundamental para que iniciantes compreendam como realizar comparações e implementar lógica condicional, habilidades indispensáveis para a construção de programas mais complexos.



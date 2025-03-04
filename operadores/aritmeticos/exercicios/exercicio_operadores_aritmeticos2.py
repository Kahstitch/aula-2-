# exercicio_operadores_aritmeticos2.py
# Exercício: Cálculo de Total e Desconto
#
# Descrição:
# Crie um programa que solicite ao usuário o preço de três produtos e, em seguida,
# realize as seguintes operações:
# 1. Calcule a soma total dos três preços.
# 2. Calcule a média aritmética dos preços.
# 3. Aplique um desconto de 10% sobre o valor total.
#
# Cada etapa do programa é detalhadamente comentada para facilitar o aprendizado.

# Entrada de dados:
# Solicita o preço do primeiro produto e converte a entrada para float
preco1 = float(input("Digite o preço do primeiro produto: "))
# Solicita o preço do segundo produto e converte a entrada para float
preco2 = float(input("Digite o preço do segundo produto: "))
# Solicita o preço do terceiro produto e converte a entrada para float
preco3 = float(input("Digite o preço do terceiro produto: "))

# Operações aritméticas:
# 1. Soma: calcula a soma total dos três preços.
soma_total = preco1 + preco2 + preco3  # Soma dos três preços

# 2. Média: calcula a média aritmética dividindo a soma total pelo número de produtos.
media_precos = soma_total / 3  # Média dos preços

# 3. Desconto: calcula 10% do valor total e deduz esse valor da soma total.
desconto = soma_total * 0.10  # Calcula 10% de desconto
valor_com_desconto = soma_total - desconto  # Valor final após aplicar o desconto

# Saída de dados:
# Exibe os resultados de forma clara e organizada.
print("\nResultados:")
print("Soma Total dos Produtos: R$", soma_total)
print("Média dos Preços: R$", media_precos)
print("Desconto (10%): R$", desconto)
print("Valor com Desconto: R$", valor_com_desconto)

# Explicação adicional:
# - O operador '+' soma os valores de 'preco1', 'preco2' e 'preco3'.
# - A divisão por 3 obtém a média aritmética dos três preços.
# - Multiplicar a soma_total por 0.10 calcula o valor do desconto (10%).
# - A subtração final aplica o desconto ao valor total.
# - A conversão para float permite que sejam usados valores decimais, comuns em preços.

#Objetivo do Exercício

Este exercício propõe que o aluno:

1. Solicite os preços de três produtos.


2. Calcule a soma total dos preços.


3. Calcule a média aritmética dos preços.


4. Aplique um desconto de 10% sobre o valor total e exiba o valor com desconto.



O código é completamente comentado para facilitar o entendimento dos conceitos de entrada de dados, operações aritméticas e formatação de saída.


---

Análise Linha por Linha

Entrada de Dados

# Solicita o preço do primeiro produto e converte a entrada para float
preco1 = float(input("Digite o preço do primeiro produto: "))
# Solicita o preço do segundo produto e converte a entrada para float
preco2 = float(input("Digite o preço do segundo produto: "))
# Solicita o preço do terceiro produto e converte a entrada para float
preco3 = float(input("Digite o preço do terceiro produto: "))

Função input(): Coleta dados informados pelo usuário.

Conversão para float: Garante que os valores inseridos, que podem conter casas decimais (como preços normalmente possuem), sejam convertidos para o tipo numérico adequado, permitindo cálculos precisos.



---

Operações Aritméticas

1. Cálculo da Soma Total

# Soma: calcula a soma total dos três preços.
soma_total = preco1 + preco2 + preco3  # Soma dos três preços

O operador + é utilizado para somar os valores de preco1, preco2 e preco3.

O resultado é armazenado na variável soma_total, representando o valor total sem descontos.



2. Cálculo da Média dos Preços

# Média: calcula a média aritmética dividindo a soma total pelo número de produtos.
media_precos = soma_total / 3  # Média dos preços

Utiliza o operador / para dividir o total dos preços por 3, o número de produtos.

Essa operação gera a média aritmética, que é uma medida importante para avaliar os valores individualmente.



3. Cálculo do Desconto e Valor com Desconto

# Desconto: calcula 10% do valor total e deduz esse valor da soma total.
desconto = soma_total * 0.10  # Calcula 10% de desconto
valor_com_desconto = soma_total - desconto  # Valor final após aplicar o desconto

Primeiro, multiplica-se soma_total por 0.10 para obter o valor correspondente a 10% do total.

Em seguida, subtrai-se esse valor (desconto) da soma_total, resultando no valor_com_desconto.





---

Saída de Dados

# Exibe os resultados de forma clara e organizada.
print("\nResultados:")
print("Soma Total dos Produtos: R$", soma_total)
print("Média dos Preços: R$", media_precos)
print("Desconto (10%): R$", desconto)
print("Valor com Desconto: R$", valor_com_desconto)

Função print(): Utilizada para mostrar os resultados finais.

O caractere \n no início do primeiro print adiciona uma linha em branco, organizando a saída.

Cada linha exibe uma operação realizada, facilitando a visualização dos resultados.



---

Resumo Geral

Entrada: O programa solicita três preços e os converte para o tipo float para lidar com valores decimais.

Processamento:

Soma: Calcula a soma total dos preços.

Média: Divide a soma total por 3 para obter a média aritmética.

Desconto: Calcula 10% de desconto sobre o valor total e subtrai esse valor do total.


Saída: Os resultados são impressos de forma organizada, exibindo a soma total, a média, 
o valor do desconto e o valor final com desconto.

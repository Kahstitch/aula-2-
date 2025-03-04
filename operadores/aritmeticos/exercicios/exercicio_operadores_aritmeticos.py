# exercicio_operadores_aritmeticos.py
# Exercício: Operadores Aritméticos
#
# Descrição:
# Crie um programa que solicite ao usuário que informe dois números e, em seguida, 
# exiba o resultado das seguintes operações:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão (com resultado em ponto flutuante)
# 5. Divisão inteira (apenas a parte inteira)
# 6. Módulo (resto da divisão)
#
# O programa deve ser bem comentado e demonstrar o funcionamento de cada operação.

# Importante: Ao realizar testes, digite números válidos (inteiros ou decimais)

# Entrada de dados:
# Solicita ao usuário que insira o primeiro número e converte a entrada para float.
numero1 = float(input("Digite o primeiro número: "))
# Solicita ao usuário que insira o segundo número e converte a entrada para float.
numero2 = float(input("Digite o segundo número: "))

# Operações aritméticas:
# 1. Soma: utiliza o operador '+' para somar os dois números.
soma = numero1 + numero2  # Soma de numero1 e numero2

# 2. Subtração: utiliza o operador '-' para subtrair o segundo número do primeiro.
subtracao = numero1 - numero2  # Diferença entre numero1 e numero2

# 3. Multiplicação: utiliza o operador '*' para multiplicar os dois números.
multiplicacao = numero1 * numero2  # Produto de numero1 e numero2

# 4. Divisão: utiliza o operador '/' para dividir o primeiro número pelo segundo.
#    Obs: Se o segundo número for zero, isso gerará um erro (divisão por zero).
divisao = numero1 / numero2  # Resultado da divisão em ponto flutuante

# 5. Divisão inteira: utiliza o operador '//' para obter apenas a parte inteira da divisão.
divisao_inteira = numero1 // numero2  # Resultado da divisão inteira

# 6. Módulo: utiliza o operador '%' para obter o resto da divisão entre os dois números.
modulo = numero1 % numero2  # Resto da divisão de numero1 por numero2

# Saída de dados:
# Exibe os resultados de cada operação no console.
print("\nResultados das operações:")
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Divisão Inteira:", divisao_inteira)
print("Módulo:", modulo)

# Explicação do exercício:
# Este exercício tem como objetivo fixar o uso dos operadores aritméticos em Python.
# Cada operação é realizada utilizando o operador correspondente e o resultado é impresso.
# O aluno pode testar com diferentes números e observar como cada operação se comporta,
# especialmente quando se trata de divisões e módulos.

#Objetivo do Exercício

O código tem como finalidade fixar o uso dos operadores aritméticos em Python. Ele solicita que o usuário informe dois números e, a partir destes, realiza diversas operações:

1. Soma


2. Subtração


3. Multiplicação


4. Divisão (resultado em ponto flutuante)


5. Divisão inteira (apenas a parte inteira do quociente)


6. Módulo (resto da divisão)



Cada operação é realizada utilizando seu respectivo operador e o resultado é exibido no console.


---

Análise Linha por Linha

Entrada de Dados

# Solicita ao usuário que insira o primeiro número e converte a entrada para float.
numero1 = float(input("Digite o primeiro número: "))
# Solicita ao usuário que insira o segundo número e converte a entrada para float.
numero2 = float(input("Digite o segundo número: "))

input(): Recebe uma entrada do usuário, que é uma string.

float(): Converte essa string para um número do tipo ponto flutuante, permitindo trabalhar tanto com inteiros quanto com decimais.

Objetivo: Garantir que os valores informados possam ser utilizados em operações matemáticas, inclusive divisões, sem problemas de conversão.



---

Realização das Operações Aritméticas

1. Soma

# Soma: utiliza o operador '+' para somar os dois números.
soma = numero1 + numero2  # Soma de numero1 e numero2

Operador +: Adiciona os dois números.

Resultado: Armazenado na variável soma.



2. Subtração

# Subtração: utiliza o operador '-' para subtrair o segundo número do primeiro.
subtracao = numero1 - numero2  # Diferença entre numero1 e numero2

Operador -: Subtrai o valor de numero2 do valor de numero1.

Resultado: Armazenado na variável subtracao.



3. Multiplicação

# Multiplicação: utiliza o operador '*' para multiplicar os dois números.
multiplicacao = numero1 * numero2  # Produto de numero1 e numero2

Operador *: Multiplica os dois números.

Resultado: Armazenado na variável multiplicacao.



4. Divisão

# Divisão: utiliza o operador '/' para dividir o primeiro número pelo segundo.
# Obs: Se o segundo número for zero, isso gerará um erro (divisão por zero).
divisao = numero1 / numero2  # Resultado da divisão em ponto flutuante

Operador /: Realiza a divisão normal, retornando um resultado com casas decimais (float).

Observação: Se numero2 for zero, o código gerará um erro de divisão por zero. Em contextos mais robustos, é comum tratar essa exceção.



5. Divisão Inteira

# Divisão inteira: utiliza o operador '//' para obter apenas a parte inteira da divisão.
divisao_inteira = numero1 // numero2  # Resultado da divisão inteira

Operador //: Realiza a divisão e retorna apenas a parte inteira do quociente, descartando as casas decimais.

Aplicação: Útil quando apenas a parte inteira do resultado é necessária.



6. Módulo

# Módulo: utiliza o operador '%' para obter o resto da divisão entre os dois números.
modulo = numero1 % numero2  # Resto da divisão de numero1 por numero2

Operador %: Calcula o resto da divisão entre numero1 e numero2.

Aplicação: Muito utilizado para verificar a paridade (se um número é par ou ímpar) ou em cálculos de ciclos.





---

Exibição dos Resultados

# Saída de dados:
# Exibe os resultados de cada operação no console.
print("\nResultados das operações:")
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Divisão Inteira:", divisao_inteira)
print("Módulo:", modulo)

print(): Imprime os resultados no console, mostrando cada operação e seu respectivo resultado.

A utilização de \n no início do primeiro print serve para pular uma linha e deixar a saída mais organizada.



---

Explicação Geral do Exercício

1. Interação com o Usuário:
O programa começa solicitando dois números, convertendo-os para o tipo float para que operações com decimais possam ser realizadas sem erros.


2. Uso de Operadores Aritméticos:
Cada operação (soma, subtração, multiplicação, divisão, divisão inteira e módulo) é demonstrada de forma simples, utilizando os operadores básicos de Python. Isso ajuda o aluno a entender a sintaxe e a funcionalidade de cada operador.

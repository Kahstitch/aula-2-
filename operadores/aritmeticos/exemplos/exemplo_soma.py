# exemplo_soma.py
# Este exemplo demonstra como utilizar o operador de adição (+) para somar valores numéricos em Python.

# Declaração de variáveis com valores inteiros
valor1 = 15  # Primeiro número para soma
valor2 = 10  # Segundo número para soma

# Realiza a soma dos dois valores utilizando o operador +
soma = valor1 + valor2  # A variável 'soma' armazena o resultado da operação

# Exibe o resultado da soma no console
print("A soma de", valor1, "e", valor2, "é:", soma)

# Explicação adicional:
# - O operador '+' soma os valores de 'valor1' e 'valor2'.
# - O comando 'print' é utilizado para mostrar o resultado na tela.

#Explicação Detalhada

1. Declaração de Variáveis

Criamos duas variáveis: valor1 e valor2, ambas do tipo inteiro (int), armazenando os números 15 e 10, respectivamente.



2. Operação de Soma

Utilizamos o operador + para somar valor1 e valor2.

O resultado dessa soma é armazenado na variável soma.



3. Exibição do Resultado

O comando print() exibe o resultado no console.

No Python, ao utilizar print() com múltiplos argumentos separados por vírgula (,), os valores são automaticamente separados por um espaço ao serem exibidos.



4. Exemplo de Saída do Código

A soma de 15 e 10 é: 25




---

Extensões e Possíveis Modificações

Usando Input do Usuário: Podemos permitir que o usuário digite os números a serem somados.

Convertendo para Float: Para somar números decimais, basta converter os valores para float.

Formatando a Saída: Podemos usar f-strings para uma exibição mais clara.


Exemplo Modificado com Input

# Solicita entrada do usuário e converte para número inteiro
valor1 = int(input("Digite o primeiro número: "))
valor2 = int(input("Digite o segundo número: "))

# Realiza a soma
soma = valor1 + valor2

# Exibe o resultado usando f-string
print(f"A soma de {valor1} e {valor2} é: {soma}")


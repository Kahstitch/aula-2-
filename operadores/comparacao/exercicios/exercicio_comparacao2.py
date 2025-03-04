# ------------------------------------------------
# EXERCÍCIO: COMPARAÇÃO DE STRINGS EM PYTHON
# ------------------------------------------------

# 🔹 Entrada de dados
palavra1 = input("Digite a primeira palavra: ").strip().lower()
palavra2 = input("Digite a segunda palavra: ").strip().lower()

# 🔹 Comparações entre as palavras
print("\nResultados da Comparação:")
if palavra1 == palavra2:
    print("As palavras são IGUAIS.")
else:
    print("As palavras são DIFERENTES.")

# 🔹 Verifica a ordem alfabética
if palavra1 < palavra2:
    print(f"A palavra '{palavra1}' vem antes de '{palavra2}' no alfabeto.")
else:
    print(f"A palavra '{palavra2}' vem antes de '{palavra1}' no alfabeto.")

# 🔹 Verifica se uma palavra está contida na outra
if palavra1 in palavra2 or palavra2 in palavra1:
    print("Uma das palavras está contida dentro da outra.")

# 🔹 Mensagem final
print("\nComparação concluída!")

#Objetivo do Exercício

Este exercício ensina conceitos fundamentais sobre manipulação e comparação de strings, incluindo:

1. Normalização de entrada (remoção de espaços extras e conversão para letras minúsculas).


2. Comparação de igualdade entre duas palavras.


3. Ordenação alfabética para verificar qual palavra vem primeiro.


4. Verificação de substring (se uma palavra está contida dentro da outra).




---

Explicação Detalhada do Código

1. Entrada de Dados e Normalização

# 🔹 Entrada de dados
palavra1 = input("Digite a primeira palavra: ").strip().lower()
palavra2 = input("Digite a segunda palavra: ").strip().lower()

input():

Solicita que o usuário digite duas palavras.


strip():

Remove espaços extras antes e depois da palavra, evitando erros acidentais.


lower():

Converte todas as letras para minúsculas, garantindo que a comparação não seja afetada por diferenças de maiúsculas e minúsculas.

Exemplo: "Python" e "python" seriam tratados como iguais.




---

2. Comparação de Igualdade

# 🔹 Comparações entre as palavras
print("\nResultados da Comparação:")
if palavra1 == palavra2:
    print("As palavras são IGUAIS.")
else:
    print("As palavras são DIFERENTES.")

Objetivo:

Verifica se palavra1 e palavra2 são idênticas (após normalização).


if palavra1 == palavra2:

Se forem exatamente iguais, exibe:
"As palavras são IGUAIS."


else:

Se forem diferentes, exibe:
"As palavras são DIFERENTES."




---

3. Verificação da Ordem Alfabética

# 🔹 Verifica a ordem alfabética
if palavra1 < palavra2:
    print(f"A palavra '{palavra1}' vem antes de '{palavra2}' no alfabeto.")
else:
    print(f"A palavra '{palavra2}' vem antes de '{palavra1}' no alfabeto.")

Comparação de Strings (<):

Em Python, palavras são comparadas alfabeticamente com base na tabela ASCII.

"abacaxi" < "banana" → True, pois "abacaxi" vem antes.


Como funciona?

Se palavra1 vier antes de palavra2, exibe:
"A palavra 'palavra1' vem antes de 'palavra2' no alfabeto."

Caso contrário, inverte a mensagem para refletir corretamente a ordem.




---

4. Verificação de Substring

# 🔹 Verifica se uma palavra está contida na outra
if palavra1 in palavra2 or palavra2 in palavra1:
    print("Uma das palavras está contida dentro da outra.")

in (operador de substring):

Verifica se uma palavra faz parte da outra.

Exemplo:

"pro" in "programação"  # True
"grama" in "programa"   # True


Combinação com or:

A condição verifica ambas as direções:

palavra1 está dentro de palavra2

palavra2 está dentro de palavra1



Se verdadeiro, exibe: "Uma das palavras está contida dentro da outra."



---

5. Mensagem Final

# 🔹 Mensagem final
print("\nComparação concluída!")

Apenas uma mensagem para indicar que o programa terminou.



---

Exemplo de Execução

Entrada do Usuário:

Digite a primeira palavra: Programação
Digite a segunda palavra: programa

Saída:

Resultados da Comparação:
As palavras são DIFERENTES.
A palavra 'programa' vem antes de 'programação' no alfabeto.
Uma das palavras está contida dentro da outra.

Comparação concluída!


---

Resumo dos Conceitos Aplicados

1. Manipulação de strings (strip(), lower())


2. Comparação de igualdade (==)


3. Ordenação alfabética (<)


4. Verificação de substring (in)


5. Uso de if e else para controle de fluxo



Este exercício é uma introdução prática à manipulação e comparação de strings, um conceito essencial para lidar com textos em Python.

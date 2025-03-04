# Exemplo de operadores lógicos em Python

# Declaração de variáveis booleanas
tem_carteira_motorista = True
tem_carro = False

# Uso do operador AND (E lógico)
# Só pode dirigir se tiver carteira de motorista E um carro
pode_dirigir = tem_carteira_motorista and tem_carro
print("Pode dirigir?", pode_dirigir)  # False

# Uso do operador OR (OU lógico)
# Pode viajar de carro se tiver um carro ou um amigo com carro
amigo_tem_carro = True
pode_viajar = tem_carro or amigo_tem_carro
print("Pode viajar?", pode_viajar)  # True

# Uso do operador NOT (Negação lógica)
# Se não tem carteira de motorista, não pode dirigir
nao_pode_dirigir = not tem_carteira_motorista
print("Não pode dirigir?", nao_pode_dirigir)  # False

#Objetivo do Código

Este exemplo tem como finalidade:

Ensinar o uso dos operadores lógicos: and, or e not.

Mostrar como esses operadores podem ser aplicados para tomar decisões em função de múltiplas condições.



---

Análise Linha por Linha

Declaração de Variáveis Booleanas

# Declaração de variáveis booleanas
tem_carteira_motorista = True  # Indica se a pessoa possui carteira de motorista
tem_carro = False               # Indica se a pessoa possui um carro

tem_carteira_motorista: Armazena o valor True, ou seja, a pessoa possui carteira de motorista.

tem_carro: Armazena o valor False, indicando que a pessoa não possui um carro.

Essas variáveis serão usadas para avaliar condições relacionadas à direção.



---

Uso do Operador AND (and)

# Uso do operador AND (E lógico)
# Só pode dirigir se tiver carteira de motorista E um carro
pode_dirigir = tem_carteira_motorista and tem_carro
print("Pode dirigir?", pode_dirigir)  # False

Conceito:

O operador and retorna True apenas se ambas as condições forem verdadeiras.


Aplicação:

Para dirigir, a pessoa precisa ter carteira de motorista e carro.

Aqui, mesmo tendo a carteira (True), a ausência de carro (False) resulta em False para a variável pode_dirigir.




---

Uso do Operador OR (or)

# Uso do operador OR (OU lógico)
# Pode viajar de carro se tiver um carro ou um amigo com carro
amigo_tem_carro = True
pode_viajar = tem_carro or amigo_tem_carro
print("Pode viajar?", pode_viajar)  # True

Conceito:

O operador or retorna True se pelo menos uma das condições for verdadeira.


Aplicação:

Para viajar de carro, basta ter um carro ou ter um amigo que possua um carro.

Apesar de tem_carro ser False, a variável amigo_tem_carro é True, resultando em True para pode_viajar.




---

Uso do Operador NOT (not)

# Uso do operador NOT (Negação lógica)
# Se não tem carteira de motorista, não pode dirigir
nao_pode_dirigir = not tem_carteira_motorista
print("Não pode dirigir?", nao_pode_dirigir)  # False

Conceito:

O operador not inverte o valor booleano da condição.


Aplicação:

Se a pessoa não tem carteira de motorista, então ela não pode dirigir.

Como tem_carteira_motorista é True, o uso de not resulta em False para nao_pode_dirigir.




---

Resumo do Funcionamento

1. Operador and:

Condição: tem_carteira_motorista and tem_carro

Resultado: False porque, apesar de ter carteira, a pessoa não possui carro.



2. Operador or:

Condição: tem_carro or amigo_tem_carro

Resultado: True porque o amigo tem carro, permitindo a viagem.



3. Operador not:

Condição: not tem_carteira_motorista

Resultado: False porque a pessoa realmente tem carteira.





---

Conclusão

Este exemplo ensina de forma clara como os operadores lógicos:

and: Exigem que todas as condições sejam verdadeiras.

or: Aceitam que pelo menos uma condição seja verdadeira.

not: Invertem o valor de uma condição.


Esses conceitos são essenciais para a construção de fluxos de decisão e para o controle de execução de programas em Python. Com a compreensão desses operadores, você estará apto a criar lógicas mais complexas e condicionalmente dinâmicas em seus projetos.

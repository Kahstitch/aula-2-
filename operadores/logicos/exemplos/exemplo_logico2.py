# ---------------------------------------------
# Exemplo Avançado de Operadores Lógicos
# ---------------------------------------------

# Simulação de um sistema de controle de acesso baseado em idade e permissão dos pais

# Pergunta ao usuário a idade e se tem autorização dos pais
idade = int(input("Digite sua idade: "))
tem_autorizacao_pais = input("Possui autorização dos pais? (s/n): ").strip().lower() == "s"

# Definição das regras
# - Pode entrar sozinho se tiver 18 anos ou mais
# - Pode entrar com autorização dos pais se tiver entre 13 e 17 anos
# - Não pode entrar se tiver menos de 13 anos

pode_entrar_sozinho = idade >= 18
pode_entrar_com_pais = 13 <= idade < 18 and tem_autorizacao_pais
nao_pode_entrar = idade < 13

# Verificação e exibição da mensagem adequada
if pode_entrar_sozinho:
    print("Acesso permitido: Você pode entrar sozinho.")
elif pode_entrar_com_pais:
    print("Acesso permitido: Você pode entrar com autorização dos pais.")
else:
    print("Acesso negado: Você não pode entrar.")

# Explicação:
# - `idade >= 18`: Permite entrada livre para maiores de idade.
# - `13 <= idade < 18 and tem_autorizacao_pais`: Permite entrada com autorização.
# - `idade < 13`: Bloqueia acesso para crianças menores de 13 anos.

#Objetivo do Código

O programa simula um sistema de controle de acesso onde:

Maiores de 18 anos podem entrar sozinhos.

Adolescentes entre 13 e 17 anos podem entrar apenas se tiverem autorização dos pais.

Pessoas com menos de 13 anos não podem entrar.


O código utiliza operadores lógicos para combinar condições e definir regras de acesso.


---

Análise Linha por Linha

1. Entrada de Dados

# Pergunta ao usuário a idade e se tem autorização dos pais
idade = int(input("Digite sua idade: "))
tem_autorizacao_pais = input("Possui autorização dos pais? (s/n): ").strip().lower() == "s"

Entrada da idade:

O programa solicita que o usuário digite sua idade.

A função input() coleta a informação em forma de string.

A função int() converte essa entrada para um número inteiro, permitindo comparações numéricas.


Entrada da autorização dos pais:

O programa pergunta se o usuário possui autorização dos pais.

input() capta a resposta (espera-se "s" para sim ou "n" para não).

strip().lower() garante que espaços extras sejam removidos e que a resposta seja convertida para minúsculas, padronizando a entrada.

A expressão == "s" converte a resposta em um valor booleano: True se a resposta for "s" e False caso contrário.




---

2. Definição das Regras de Acesso

# - Pode entrar sozinho se tiver 18 anos ou mais
pode_entrar_sozinho = idade >= 18

# - Pode entrar com autorização dos pais se tiver entre 13 e 17 anos
pode_entrar_com_pais = 13 <= idade < 18 and tem_autorizacao_pais

# - Não pode entrar se tiver menos de 13 anos
nao_pode_entrar = idade < 13

pode_entrar_sozinho:

A condição idade >= 18 verifica se o usuário é maior ou igual a 18 anos.

Se verdadeiro, o usuário tem permissão para entrar sozinho.


pode_entrar_com_pais:

A condição 13 <= idade < 18 verifica se o usuário tem entre 13 e 17 anos.

O operador and combina essa condição com tem_autorizacao_pais.

Ou seja, o acesso com a autorização dos pais só é permitido se o usuário estiver nessa faixa etária e tiver autorização.


nao_pode_entrar:

A condição idade < 13 determina que usuários com menos de 13 anos não podem entrar.




---

3. Verificação e Exibição da Mensagem Adequada

# Verificação e exibição da mensagem adequada
if pode_entrar_sozinho:
    print("Acesso permitido: Você pode entrar sozinho.")
elif pode_entrar_com_pais:
    print("Acesso permitido: Você pode entrar com autorização dos pais.")
else:
    print("Acesso negado: Você não pode entrar.")

Estrutura Condicional:

A estrutura if/elif/else é utilizada para determinar qual mensagem será exibida com base nas condições definidas.

Primeira condição (if pode_entrar_sozinho):
Se pode_entrar_sozinho for True (idade 18 ou mais), o programa exibe que o acesso é permitido sem restrições.

Segunda condição (elif pode_entrar_com_pais):
Se a primeira condição for falsa, verifica se o usuário se enquadra na faixa etária de 13 a 17 anos e se possui autorização dos pais. Se sim, exibe uma mensagem permitindo o acesso com autorização.

Caso contrário (else):
Se nenhuma das condições anteriores for satisfeita, o acesso é negado e uma mensagem informando isso é exibida.




---

Explicação Geral

Operadores Lógicos Aplicados:

>= e <: Usados para verificar faixas de idade.

and: Combina condições, como garantir que o usuário tenha uma idade específica e autorização dos pais.

==: É usado para converter a resposta do usuário em um valor booleano, permitindo a comparação direta.


Fluxo do Programa:

1. O programa coleta os dados do usuário (idade e autorização).


2. Define as regras de acesso com base na idade e na autorização.


3. Utiliza uma estrutura condicional para decidir e exibir a mensagem apropriada.





---

Considerações Finais

Este exemplo é uma ótima demonstração de como combinar condições lógicas para implementar regras de negócio em Python. Com ele, os alunos aprendem a:

Coletar e converter entradas do usuário.

Usar operadores lógicos e de comparação para definir regras.

Estruturar decisões complexas utilizando if, elif e else.


Esses conceitos são fundamentais para construir programas mais robustos e interativos, permitindo a criação de sistemas que tomam decisões de forma automatizada com base em condições pré-definidas.

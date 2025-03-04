# -----------------------------------------------------
# Exercício: Verificação de Acesso a Conta Bancária
# -----------------------------------------------------

# O usuário só pode acessar a conta se:
# 1. Ele souber a senha correta.
# 2. Ele estiver usando um dispositivo confiável OU inserir um código de verificação.

# Definição da senha correta
senha_correta = "Python123"

# Pergunta ao usuário a senha
senha_digitada = input("Digite sua senha: ")

# Verifica se a senha está correta
senha_valida = senha_digitada == senha_correta

# Pergunta se está em um dispositivo confiável
dispositivo_confiavel = input("Este é um dispositivo confiável? (s/n): ").strip().lower() == "s"

# Pergunta o código de verificação caso o dispositivo NÃO seja confiável
if not dispositivo_confiavel:
    codigo_verificacao = input("Digite o código de verificação enviado ao seu e-mail: ")
    codigo_correto = "4321"  # Código fictício para simulação
    codigo_valido = codigo_verificacao == codigo_correto
else:
    codigo_valido = True  # Se o dispositivo for confiável, o código é automaticamente válido

# Verifica se o usuário pode acessar a conta
acesso_permitido = senha_valida and (dispositivo_confiavel or codigo_valido)

# Exibe a mensagem correspondente
if acesso_permitido:
    print("Acesso permitido: Bem-vindo à sua conta!")
else:
    print("Acesso negado: Senha ou código de verificação incorretos.")

# Explicação:
# - `senha_digitada == senha_correta`: Garante que a senha esteja correta.
# - `dispositivo_confiavel`: Se for "s", ignora a necessidade de código de verificação.
# - `not dispositivo_confiavel`: Se for "n", exige um código de verificação correto.
# - `acesso_permitido = senha_valida and (dispositivo_confiavel or codigo_valido)`: 
#    → O usuário precisa da senha correta **E** estar em um dispositivo confiável **OU** inserir um código válido.

#Objetivo do Exercício

Este exercício tem como objetivo ensinar como combinar múltiplas condições usando operadores lógicos para controlar o fluxo de acesso a uma conta. Ele demonstra:

Verificação de senha por meio da comparação direta.

Uso do operador not para inverter uma condição (verificar se o dispositivo não é confiável).

Combinação de condições com operadores and e or para definir regras de acesso.

Processamento condicional (usando if/else) para solicitar informações extras quando necessário.



---

Análise Linha por Linha

1. Definição da Senha Correta e Coleta da Senha Digitada

# Definição da senha correta
senha_correta = "Python123"

# Pergunta ao usuário a senha
senha_digitada = input("Digite sua senha: ")

# Verifica se a senha está correta
senha_valida = senha_digitada == senha_correta

senha_correta: Armazena a senha correta, que neste exemplo é a string "Python123".

Entrada do Usuário:

A função input() coleta a senha digitada pelo usuário.

Em seguida, o código compara a senha digitada com a senha correta, definindo a variável senha_valida como True se forem iguais, ou False caso contrário.




---

2. Verificação do Dispositivo Confiável

# Pergunta se está em um dispositivo confiável
dispositivo_confiavel = input("Este é um dispositivo confiável? (s/n): ").strip().lower() == "s"

O programa pergunta se o dispositivo utilizado é confiável.

Processamento da Resposta:

O método strip() remove espaços em branco adicionais.

lower() converte a resposta para minúsculas, padronizando a entrada.

A comparação == "s" transforma a resposta em um valor booleano:

Se o usuário responder "s", dispositivo_confiavel será True.

Se responder "n", será False.





---

3. Solicitação do Código de Verificação (quando necessário)

# Pergunta o código de verificação caso o dispositivo NÃO seja confiável
if not dispositivo_confiavel:
    codigo_verificacao = input("Digite o código de verificação enviado ao seu e-mail: ")
    codigo_correto = "4321"  # Código fictício para simulação
    codigo_valido = codigo_verificacao == codigo_correto
else:
    codigo_valido = True  # Se o dispositivo for confiável, o código é automaticamente válido

Condição if not dispositivo_confiavel:

Se o dispositivo não for confiável (ou seja, dispositivo_confiavel é False), o sistema solicita um código de verificação.

O código digitado é comparado com o código correto (neste caso, "4321").

A variável codigo_valido recebe True se o código estiver correto e False caso contrário.


Caso o Dispositivo Seja Confiável (else):

Se o dispositivo for confiável (dispositivo_confiavel for True), a variável codigo_valido é definida como True automaticamente, pois o código não é necessário.




---

4. Verificação Final do Acesso

# Verifica se o usuário pode acessar a conta
acesso_permitido = senha_valida and (dispositivo_confiavel or codigo_valido)

Condição de Acesso:

O usuário só pode acessar a conta se:

A senha for válida e

Ou o dispositivo for confiável ou o código de verificação for válido.



Operadores Utilizados:

and: Garante que ambas as partes da condição principal sejam verdadeiras.

or: Dentro do parênteses, permite que o acesso seja liberado se pelo menos uma das condições (dispositivo confiável ou código válido) for satisfeita.




---

5. Exibição da Mensagem ao Usuário

# Exibe a mensagem correspondente
if acesso_permitido:
    print("Acesso permitido: Bem-vindo à sua conta!")
else:
    print("Acesso negado: Senha ou código de verificação incorretos.")

Estrutura Condicional:

Se acesso_permitido for True, o usuário vê a mensagem que indica acesso permitido.

Caso contrário, é exibida uma mensagem de acesso negado, alertando que a senha ou o código de verificação estão incorretos.




---

Resumo do Funcionamento

1. Verificação da Senha:

O usuário digita a senha e o sistema verifica se ela corresponde à senha correta.



2. Confirmação do Dispositivo:

O sistema pergunta se o dispositivo é confiável.

Se não for, solicita um código de verificação.



3. Validação do Código:

Se o dispositivo não for confiável, a verificação do código é necessária para validar o acesso.

Se o dispositivo for confiável, essa etapa é ignorada (o código é considerado válido).



4. Decisão Final:

O acesso é permitido somente se a senha for válida e o usuário estiver em um dispositivo confiável ou tiver fornecido um código válido.





---

Considerações Finais

Este exemplo ilustra como combinar múltiplas condições usando operadores lógicos em Python para criar regras de acesso sofisticadas. Ele ensina:

Coleta e Processamento de Dados: Uso de input(), strip(), lower() e conversões para tipos apropriados.

Uso de Operadores Lógicos: Combinação de condições com and, or e not.

Estruturas Condicionais: Como usar if/else para solicitar informações adicionais e tomar decisões baseadas em condições complexas.

# ---------------------------------------------------------------------
# Arquivo: exercicio_escopo.py
# Localização: variaveis/exercicios/
#
# Este exercício tem como objetivo desafiar o aluno a compreender o
# conceito de escopo de variáveis em Python.
#
# Desafio:
# 1. Crie uma variável global chamada 'saudacao' e atribua a ela o valor 
#    "Olá, estudante!".
# 2. Crie uma função chamada 'mostrar_saudacao' que:
#    - Declare uma variável local chamada 'mensagem_local' com o valor "Bem-vindo(a) ao curso de Python!".
#    - Imprima a variável global 'saudacao' e a variável local 'mensagem_local'.
# 3. Chame a função 'mostrar_saudacao' para exibir as mensagens.
#
# Após realizar o exercício, compare com a solução comentada abaixo.
# ---------------------------------------------------------------------

# Declaração da variável global 'saudacao'
saudacao = "Olá, estudante!"  # Variável global, acessível em todo o módulo

def mostrar_saudacao():
    """
    Função para demonstrar o uso de variáveis globais e locais.
    """
    # Declaração de uma variável local dentro da função
    mensagem_local = "Bem-vindo(a) ao curso de Python!"  # Variável local, somente visível dentro da função

    # Exibição da variável global e da variável local
    print("Saudação global:", saudacao)       # Acessa a variável global
    print("Mensagem local:", mensagem_local)    # Acessa a variável local

# Chamada da função para exibir as mensagens
mostrar_saudacao()

# Explicação:
# - A variável 'saudacao' foi definida fora da função, tornando-se global.
# - Dentro da função 'mostrar_saudacao', é definida a variável 'mensagem_local', que só
#   existe no contexto da função.
# - Ao chamar a função, ambas as mensagens são exibidas, demonstrando a diferença de escopo.

#Resumo e Aplicação Prática

✅ Variáveis globais: São definidas fora de funções e podem ser acessadas de qualquer parte do código.
✅ Variáveis locais: São criadas dentro de funções e só existem durante a execução daquela função.

🚀 Dica: Para modificar uma variável global dentro de uma função, é necessário usar a palavra-chave global.

Exemplo:

def alterar_saudacao():
    global saudacao  # Permite modificar a variável global
    saudacao = "Olá, programador!" 

alterar_saudacao()
print(saudacao)  # Agora a variável global foi alterada


---

📝 Desafio extra:
🔹 Tente criar uma nova função que receba uma mensagem como parâmetro e altere saudacao globalmente.
🔹 Execute a função e veja o resultado!

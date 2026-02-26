numeros = range(1,20)
for n in numeros:
    if n % 2 == 0:
        print(n)


# ------------------------------
# BLOCO 1: fundamentos
# ------------------------------

vendas_semana = [1200, 980, 1430, 1100, 1600]

# Exercicio 1:
# Mostre:
# a) numero de dias vendidos
# b) total vendido na semana
# c) maior e menor venda diaria

# RESOLUCAO: complete aqui


# Exercicio 2:
# Acesse e mostre:
# a) primeira venda
# b) ultima venda
# c) vendas do meio (sem primeira e ultima)

# RESOLUCAO: complete aqui


# -----------------------------------
# BLOCO 2: alterar e limpar
# -----------------------------------

custos_marketing = [350, 420, 390, 410]

# Exercicio 3:
# a) Adicione um novo custo de 460 no final
# b) Insira 300 no inicio da lista
# c) Remova o valor 390
# d) Mostre a lista final

# RESOLUCAO: complete aqui


# Exercicio 4:
# A lista abaixo tem um lancamento duplicado por erro.
# Remova somente uma ocorrencia de 1200.

vendas_com_erro = [900, 1200, 1500, 1200, 1800]
# RESOLUCAO: complete aqui


# -----------------------------------------
# BLOCO 3: ordenacao e filtragem
# -----------------------------------------

ticket_medio_filiais = [85, 120, 73, 150, 99, 135]

# Exercicio 5:
# a) Crie uma nova lista em ordem crescente (sem perder a original)
# b) Crie outra em ordem decrescente
# c) Mostre as tres listas

# RESOLUCAO: complete aqui


# Exercicio 6:
# Gere uma lista apenas com tickets acima de 100.
# Dica: use for + if, ou list comprehension.

# RESOLUCAO: complete aqui


# ---------------------------------------
# BLOCO 4: agregacao e tomada
# ---------------------------------------

faturamento_diario = [2100, 1800, 2500, 1950, 2300]

# Exercicio 7:
# a) Calcule a media de faturamento diario
# b) Conte quantos dias ficaram acima da media
# c) Mostre os valores desses dias

# RESOLUCAO: complete aqui


# ---------------------------------------
# BLOCO 5: desafio final guiado
# ---------------------------------------

# Cenário:
# Sua empresa registrou vendas por vendedor na semana.
vendas_vendedor = [450, 520, 610, 480, 700, 530, 620]

# Exercicio 8 (desafio):
# 1) Calcule total e media semanal
# 2) Crie uma lista com vendas acima de 550
# 3) Mostre os 3 maiores valores de venda
# 4) Informe quantos dias ficaram abaixo de 500

# RESOLUCAO: complete aqui


# ---------------------
# CHECKLIST DE REVISAO
# ---------------------
#
# [ ] Sei criar listas e acessar por indice
# [ ] Sei usar len, sum, min, max
# [ ] Sei adicionar/remover itens
# [ ] Sei ordenar sem perder dados originais
# [ ] Sei filtrar listas com condicoes
# [ ] Sei aplicar listas em cenarios de negocio
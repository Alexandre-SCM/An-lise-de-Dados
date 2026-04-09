import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------
# BLOCO 1: fundamentos
# ------------------------------

vendas_semana = [1200, 980, 1430, 1100, 1600]

# Exercicio 1:
# Mostre:
# a) numero de dias vendidos
print(len(vendas_semana))
# b) total vendido na semana
print(sum(vendas_semana))
# c) maior e menor venda diaria
print(max(vendas_semana))
print(min(vendas_semana))

# RESOLUCAO: complete aqui


# Exercicio 2:
# Acesse e mostre:
# a) primeira venda
print(vendas_semana[0])

# b) ultima venda
print(vendas_semana[-1])

# c) vendas do meio (sem primeira e ultima)
print(vendas_semana[1:-1])

# RESOLUCAO: complete aqui


# -----------------------------------
# BLOCO 2: alterar e limpar
# -----------------------------------

custos_marketing = [350, 420, 390, 410]

# Exercicio 3:
# a) Adicione um novo custo de 460 no final
custos_marketing.append(460)

# b) Insira 300 no inicio da lista
custos_marketing.insert(0, 300)

# c) Remova o valor 390
custos_marketing.remove(390)

# d) Mostre a lista final
print(custos_marketing)

# RESOLUCAO: complete aqui


# Exercicio 4:
# A lista abaixo tem um lancamento duplicado por erro.
# Remova somente uma ocorrencia de 1200.


vendas_com_erro = [900, 1200, 1500, 1200, 1800]

# RESOLUCAO: complete aqui
vendas_com_erro.remove(1200)

# -----------------------------------------
# BLOCO 3: ordenacao e filtragem
# -----------------------------------------

ticket_medio_filiais = [85, 120, 73, 150, 99, 135]

# Exercicio 5:
# a) Crie uma nova lista em ordem crescente (sem perder a original)
ticket_medio_ordenado = sorted(ticket_medio_filiais)

# b) Crie outra em ordem decrescente
ticket_medio_decrescente = sorted(ticket_medio_filiais, reverse=True)

# c) Mostre as tres listas
print("Original:", ticket_medio_filiais)
print("Crescente:", ticket_medio_ordenado)
print("Decrescente:", ticket_medio_decrescente)

# RESOLUCAO: complete aqui


# Exercicio 6:
# Gere uma lista apenas com tickets acima de 100.
# Dica: use for + if, ou list comprehension.

tickets_acima_100 = [ticket for ticket in ticket_medio_filiais if ticket > 100]

# RESOLUCAO: complete aqui


# ---------------------------------------
# BLOCO 4: agregacao e tomada
# ---------------------------------------

faturamento_diario = [2100, 1800, 2500, 1950, 2300]

# Exercicio 7:
# a) Calcule a media de faturamento diario
media_faturamento = sum(faturamento_diario) / len(faturamento_diario)

# b) Conte quantos dias ficaram acima da media
dias_acima_media = sum(1 for valor in faturamento_diario if valor > media_faturamento)

# c) Mostre os valores desses dias
valores_acima_media = [valor for valor in faturamento_diario if valor > media_faturamento]

# RESOLUCAO: complete aqui


# ---------------------------------------
# BLOCO 5: desafio final guiado
# ---------------------------------------

# Cenário:
# Sua empresa registrou vendas por vendedor na semana.
vendas_vendedor = [450, 520, 610, 480, 700, 530, 620]

# Exercicio 8 (desafio):
# 1) Calcule total e media semanal
total = sum(vendas_vendedor)
media = total / len(vendas_vendedor)

# 2) Crie uma lista com vendas acima de 550
vendas_acima_550 = [venda for venda in vendas_vendedor if venda > 550]

# 3) Mostre os 3 maiores valores de venda
vendas_ordenadas = sorted(vendas_vendedor, reverse=True)
tres_maiores = vendas_ordenadas[:3]

# 4) Informe quantos dias ficaram abaixo de 500
dias_abaixo_500 = sum(1 for venda in vendas_vendedor if venda < 500)

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
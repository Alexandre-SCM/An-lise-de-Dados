# -----------------------------------------
# BLOCO 1: criar e acessar chaves
# -----------------------------------------

faturamento_mensal = {"Jan": 12000, "Fev": 15000, "Mar": 9000}

# Exercicio 1:
# a) Mostre o faturamento de Fev
# b) Mostre todas as chaves
# c) Mostre todos os valores

# RESOLUCAO: complete aqui


# Exercicio 2:
# O valor de Mar estava errado. Atualize para 9800.
# Depois, adicione Abr com valor 13200.

# RESOLUCAO: complete aqui


# -----------------------------------------
# BLOCO 2: metodos e seguranca
# -----------------------------------------

estoque = {"caneta": 120, "caderno": 80, "lapis": 200}

# Exercicio 3:
# a) Verifique se a chave "borracha" existe
# b) Se nao existir, retorne 0 usando get
# c) Mostre o estoque de "lapis" com get

# RESOLUCAO: complete aqui


# Exercicio 4:
# Remova "caneta" do estoque e mostre o dicionario final.
# Dica: use pop.

# RESOLUCAO: complete aqui


# -----------------------------------------
# BLOCO 3: percorrer e agregar
# -----------------------------------------

vendas_por_regiao = {
    "Norte": 18000,
    "Nordeste": 22000,
    "Centro-Oeste": 17000,
    "Sudeste": 30000,
    "Sul": 21000,
}

# Exercicio 5:
# a) Calcule o total vendido no pais
# b) Encontre a regiao com maior valor de vendas
# c) Encontre a regiao com menor valor de vendas

# RESOLUCAO: complete aqui


# Exercicio 6:
# Percorra o dicionario e mostre somente regioes com vendas acima de 20000.

# RESOLUCAO: complete aqui


# -------------------------------------------------
# BLOCO 4: dicionario como acumulador
# -------------------------------------------------

vendas_produtos = [
    ("Notebook", 1),
    ("Mouse", 2),
    ("Notebook", 1),
    ("Teclado", 1),
    ("Mouse", 1),
]

# Exercicio 7:
# Construa um dicionario de contagem no formato:
# {"Notebook": 2, "Mouse": 3, "Teclado": 1}
#
# Dica:
# - Se a chave nao existir, comeca em 0
# - Depois soma a quantidade

# RESOLUCAO: complete aqui


# ---------------------------------------------------
# BLOCO 5: desafio final de negocio
# ---------------------------------------------------

# Lista de vendas (registro por transacao)
transacoes = [
    {"mes": "Jan", "valor": 1200},
    {"mes": "Jan", "valor": 800},
    {"mes": "Fev", "valor": 1500},
    {"mes": "Fev", "valor": 700},
    {"mes": "Mar", "valor": 1300},
]

# Exercicio 8 (desafio):
# 1) Crie um dicionario total_por_mes e acumule os valores
# 2) Mostre o mes com maior faturamento
# 3) Mostre o total geral do trimestre
# 4) Mostre a media mensal (total/numero de meses no dicionario)

# RESOLUCAO: complete aqui


# ---------------------
# CHECKLIST DE REVISAO
# ---------------------
#
# [ ] Sei criar e atualizar dicionarios
# [ ] Sei acessar chaves com seguranca (get, in)
# [ ] Sei percorrer com keys, values, items
# [ ] Sei usar dicionario para acumulacao
# [ ] Sei aplicar dicionarios em cenarios de negocio
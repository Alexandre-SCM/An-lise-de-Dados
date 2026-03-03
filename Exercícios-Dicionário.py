# -----------------------------------------
# BLOCO 1: criar e acessar chaves
# -----------------------------------------

faturamento_mensal = {"Jan": 12000, "Fev": 15000, "Mar": 9000}

# Exercicio 1:
# a) Mostre o faturamento de Fev
print(faturamento_mensal["Fev"])

# b) Mostre todas as chaves
print(list(faturamento_mensal.keys()))

# c) Mostre todos os valores
print(list(faturamento_mensal.values()))

# RESOLUCAO: complete aqui


# Exercicio 2:
# O valor de Mar estava errado. Atualize para 9800.
faturamento_mensal["Mar"] = 9800

# Depois, adicione Abr com valor 13200.
faturamento_mensal["Abr"] = 13200

# RESOLUCAO: complete aqui


# -----------------------------------------
# BLOCO 2: metodos e seguranca
# -----------------------------------------

estoque = {"caneta": 120, "caderno": 80, "lapis": 200}

# Exercicio 3:
# a) Verifique se a chave "borracha" existe
if "borracha" in estoque:
    print("Borracha existe no estoque.")

# b) Se nao existir, retorne 0 usando get
borracha_estoque = estoque.get("borracha", 0)
print("Estoque de borracha:", borracha_estoque)

# c) Mostre o estoque de "lapis" com get
lapis_estoque = estoque.get("lapis", 0)
print("Estoque de lapis:", lapis_estoque)

# RESOLUCAO: complete aqui


# Exercicio 4:
# Remova "caneta" do estoque e mostre o dicionario final.

# Dica: use pop.

estoque.pop("caneta", None)
print("Estoque final:", estoque)

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
total_vendas = sum(vendas_por_regiao.values())
print("Total vendido no pais:", total_vendas)

# b) Encontre a regiao com maior valor de vendas
regiao_mais_vendas = max(vendas_por_regiao, key=vendas_por_regiao.get)
print("Regiao com maior valor de vendas:", regiao_mais_vendas)

# c) Encontre a regiao com menor valor de vendas
regiao_menos_vendas = min(vendas_por_regiao, key=vendas_por_regiao.get)
print("Regiao com menor valor de vendas:", regiao_menos_vendas)

# RESOLUCAO: complete aqui


# Exercicio 6:
# Percorra o dicionario e mostre somente regioes com vendas acima de 20000.
for regiao, vendas in vendas_por_regiao.items():
    if vendas > 20000:
        print(f"Regiao: {regiao}, Vendas: {vendas}")

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

contagem_produtos = {}
for produto, quantidade in vendas_produtos:
    contagem_produtos[produto] = contagem_produtos.get(produto, 0) + quantidade

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
total_por_mes = {}
for transacao in transacoes:
    mes = transacao["mes"]
    valor = transacao["valor"]
    total_por_mes[mes] = total_por_mes.get(mes, 0) + valor

# 2) Mostre o mes com maior faturamento
mes_mais_faturamento = max(total_por_mes, key=total_por_mes.get)
print("Mes com maior faturamento:", mes_mais_faturamento)

# 3) Mostre o total geral do trimestre
total_trimestre = sum(total_por_mes.values())
print("Total geral do trimestre:", total_trimestre)

# 4) Mostre a media mensal (total/numero de meses no dicionario)
media_mensal = total_trimestre / len(total_por_mes)
print("Media mensal:", media_mensal)

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
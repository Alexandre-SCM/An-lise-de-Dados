"""
Aula - Exercicios de Pandas DataFrame
Como usar:
1) Leia o enunciado de cada bloco.
2) Complete o codigo onde estiver RESOLUCAO.
3) Rode o arquivo e valide os resultados.

Requisito:
- Instalar pandas: pip install pandas

Regra da aula:
- Pense no DataFrame como uma planilha.
- Resolva um exercicio por vez.
"""
# -------------------------------------------------
# BLOCO 1: criar DataFrame e inspecionar estrutura
# -------------------------------------------------
import pandas as pd
dados_vendas = {
    "mes": ["Jan", "Jan", "Fev", "Fev", "Mar", "Mar"],
    "filial": ["Centro", "Norte", "Centro", "Norte", "Centro", "Norte"],
    "vendas": [12000, 9500, 13500, 10200, 14100, 11000],
    "clientes": [210, 180, 225, 190, 235, 205],
}

# Exercicio 1:
# a) Crie o DataFrame df_vendas usando dados_vendas
df_vendas = pd.DataFrame(dados_vendas)

# b) Mostre as 5 primeiras linhas
print(df_vendas.head())

# c) Mostre o formato (linhas, colunas)
print(df_vendas.shape)

# d) Mostre os tipos de dados das colunas
print(df_vendas.dtypes)

# RESOLUCAO: complete aqui

# -------------------------------------------------
# BLOCO 2: selecionar colunas e linhas
# -------------------------------------------------

# Exercicio 2:
# a) Mostre apenas as colunas "mes" e "vendas"
print(df_vendas[["mes", "vendas"]])

# b) Mostre somente a primeira linha
print(df_vendas.iloc[0])

# c) Mostre as linhas de indice 2 ate 4
print(df_vendas.iloc[2:5])


# -------------------------------------------------
# BLOCO 3: filtros com condicoes de negocio
# -------------------------------------------------

# Exercicio 3:
# a) Filtre vendas acima de 12000
df_filtro = df_vendas[df_vendas["vendas"] > 12000]

# b) Filtre apenas a filial "Centro"
df_centro = df_vendas[df_vendas["filial"] == "Centro"]

# c) Filtre vendas acima de 11000 na filial "Norte"
df_norte = df_vendas[(df_vendas["filial"] == "Norte") & (df_vendas["vendas"] > 11000)]


# -------------------------------------------------
# BLOCO 4: novas colunas e metricas
# -------------------------------------------------

# Exercicio 4:
# a) Crie a coluna "ticket_medio" = vendas / clientes
df_vendas["ticket_medio"] = df_vendas["vendas"] / df_vendas["clientes"]

# b) Crie a coluna "meta_batida" com True para vendas >= 13000
df_vendas["meta_batida"] = df_vendas["vendas"] >= 13000

# c) Mostre apenas "filial", "mes", "ticket_medio", "meta_batida"
print(df_vendas[["filial", "mes", "ticket_medio", "meta_batida"]])

# -------------------------------------------------
# BLOCO 5: agregacao com groupby
# -------------------------------------------------

# Exercicio 5:
# a) Calcule total de vendas por filial
df_total_vendas = df_vendas.groupby("filial")["vendas"].sum()
print(df_total_vendas)

# b) Calcule media de clientes por mes
df_media_clientes = df_vendas.groupby("mes")["clientes"].mean()
print(df_media_clientes)

# c) Descubra a filial com maior total de vendas
filial_maior_vendas = df_total_vendas.idxmax()
print(f"Filial com maior total de vendas: {filial_maior_vendas}")


# -------------------------------------------------
# BLOCO 6: ordenacao e ranking
# -------------------------------------------------

# Exercicio 6:
# a) Ordene df_vendas por "vendas" em ordem decrescente
df_vendas_ordenado = df_vendas.sort_values(by="vendas", ascending=False)
print(df_vendas_ordenado)

# b) Pegue os 3 maiores resultados de vendas
df_top3 = df_vendas_ordenado.head(3)
print(df_top3)

# c) Mostre um ranking com "filial", "mes", "vendas"
df_vendas_ordenado["ranking"] = df_vendas_ordenado["vendas"].rank(ascending=False)
print(df_vendas_ordenado[["filial", "mes", "vendas", "ranking"]])


# -------------------------------------------------
# BLOCO 7: desafio final de analise
# -------------------------------------------------

# Exercicio 7 (desafio):
# 1) Gere um resumo por filial com: total_vendas , media_ticket_medio e total_clientes


# 2) Ordene o resumo por total_vendas (desc)
df_resumo = df_vendas.groupby("filial").agg({
    "vendas": "sum",
    "ticket_medio": "mean",
    "clientes": "sum"
})
df_resumo = df_resumo.sort_values(by="vendas", ascending=False)
print(df_resumo)

# 3) Exiba qual filial teve melhor desempenho geral
filial_melhor_desempenho = df_resumo["vendas"].idxmax()
print(f"Filial com melhor desempenho geral: {filial_melhor_desempenho}")


# ===========================================================
# PARTE 1 – Estrutura lista + dicionário
# ===========================================================

dados_list_dict = [{
    "Column A":[1, 2, 3],
    "Column B":[4, 5, 6],
    "Column C":[7, 8, 9]
}]


# -----------------------------------------------------------
# EXERCÍCIO 1 – Explorando a estrutura
# -----------------------------------------------------------

# 1. Qual é o tipo de dados_list_dict?
print(type(dados_list_dict))

# 2. Qual é o tipo do primeiro elemento?
print(type(dados_list_dict[0]))

# 3. Como acessar a lista da "Column A"?
print(dados_list_dict[0]["Column A"])

# 4. Como acessar o segundo elemento da "Column C"?
print(dados_list_dict[0]["Column C"][1])

# -----------------------------------------------------------
# EXERCÍCIO 2 – Convertendo para DataFrame
# -----------------------------------------------------------

# 1. Converta dados_list_dict[0] em um DataFrame chamado df1
df1 = pd.DataFrame(dados_list_dict[0])

# 2. Mostre:
#    - shape
#    - tipos das colunas
print("Shape:", df1.shape)
print("Tipos das colunas:")
print(df1.dtypes)

# 3. Calcule:
#    - soma de cada coluna
#    - média de cada coluna
print("Soma de cada coluna:")
print(df1.sum(numeric_only=True))
print("Média de cada coluna:")
print(df1.mean(numeric_only=True))

# -----------------------------------------------------------
# EXERCÍCIO 3 – Criando novas colunas
# -----------------------------------------------------------

# No df1:
# 1. Crie coluna "Total" = soma das colunas
df1["Total"] = df1.sum(axis=1)

# 2. Crie coluna "Media" = média por linha
df1["Media"] = df1.mean(axis=1)

# 3. Filtre linhas onde Total > 10
df1_filtrado = df1[df1["Total"] > 10]
print(df1_filtrado)


# -----------------------------------------------------------
# EXERCÍCIO 4 – Conversões estruturais
# -----------------------------------------------------------

# 1. Converta df1 para:
#    - lista de dicionários [ {linha1}, {linha2}, {linha3} ]
#    - dicionário de listas { coluna1: [valores], coluna2: [valores] }
# Dica:
# orient="records":
#   Cada elemento representa uma linha.
#   Estrutura ideal para APIs e JSON.

# orient="list":
#   Cada chave representa uma coluna.
#   Estrutura colunar, útil para reconstruir DataFrame.

lista_dict = df1.to_dict(orient="records")
dict_list = df1.to_dict(orient="list")

print("Lista de dicionários:")
print(lista_dict)
print("\nDicionário de listas:")
print(dict_list)

# -----------------------------------------------------------
# EXERCÍCIO 5 – Trabalhando com lista
# -----------------------------------------------------------

# 1. Transforme a coluna "Column A" em uma lista chamada lista_a.
lista_a = df1["Column A"].tolist()

# 2. Multiplique cada elemento da lista por 10.
lista_a_x10 = [x * 10 for x in lista_a]

# 3. Crie uma nova coluna chamada "Column A x10" com essa nova lista.
df1["Column A x10"] = lista_a_x10
print(df1)


# ===========================================================
# BASE DE DADOS
# ===========================================================
import pandas as pd
dados = [
    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-01", "valor": 5000},

    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 102, "descricao": "Produto B",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-01", "valor": 3000},

    {"id_pais": 1, "nome_pais": "Argentina", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-02", "valor": 4000},

    {"id_pais": 1, "nome_pais": "Argentina", "id_produto": 102, "descricao": "Produto B",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-02", "valor": 6000},

    {"id_pais": 0, "nome_pais": "Brasil", "id_produto": 101, "descricao": "Produto A",
     "tipo_operacao": "Exportação", "tipo_periodo": "Mensal", "periodo": "2023-03", "valor": 7000},
]


# ===========================================================
# PARTE 1 – EXPLORAÇÃO INICIAL
# ===========================================================

# Exercício 1
# 1. Qual o tipo da variável dados?
print(type(dados))

# 2. Quantos registros existem?
print(len(dados))

# 3. Quais são as chaves do primeiro dicionário?
print(dados[0].keys())

# 4. Liste todos os países existentes (sem repetição).
paises = set(dado["nome_pais"] for dado in dados)
print(paises)

# ===========================================================
# PARTE 2 – CONVERSÃO PARA DATAFRAME
# ===========================================================

# Exercício 2
# 1. Converta dados para DataFrame chamado df
df = pd.DataFrame(dados)

# 2. Mostre shape, tipos e primeiras linhas
print("Shape:", df.shape)
print("Tipos de dados:")
print(df.dtypes)
print("Primeiras linhas:")
print(df.head())

# 3. Converta a coluna periodo para datetime
df["periodo"] = pd.to_datetime(df["periodo"])

# ===========================================================
# PARTE 3 – FILTROS E ORDENAÇÃO
# ===========================================================

# Exercício 3 – Filtros
# 1. Filtre apenas Brasil
df_brasil = df[df["nome_pais"] == "Brasil"]

# 2. Filtre apenas Produto A
df_produto_a = df[df["descricao"] == "Produto A"]

# 3. Filtre valor > 4000
df_valor_maior_4000 = df[df["valor"] > 4000]

# 4. Combine Brasil + Produto A
df_brasil_produto_a = df[(df["nome_pais"] == "Brasil") & (df["descricao"] == "Produto A")]


# Exercício 4 – Ordenação
# 1. Ordene por valor crescente
df_ordenado_crescente = df.sort_values(by="valor", ascending=True)

# 2. Ordene por valor decrescente
df_ordenado_decrescente = df.sort_values(by="valor", ascending=False)

# 3. Ordene por periodo e depois por valor
df_ordenado_periodo_valor = df.sort_values(by=["periodo", "valor"], ascending=[True, True])

# ===========================================================
# PARTE 4 – AGREGAÇÕES
# ===========================================================

# Exercício 5 – GroupBy Simples
# 1. Total exportado por país
# 2. Total exportado por produto
# 3. Média por país
# 4. Quantidade de operações por país

df_groupby_pais = df.groupby("nome_pais").sum(numeric_only=True)
df_groupby_produto = df.groupby("descricao").sum(numeric_only=True)
df_groupby_media = df.groupby("nome_pais")["valor"].mean()
df_groupby_contagem = df.groupby("nome_pais").size()

# Exercício 6 – GroupBy Múltiplo
# Agrupe por nome_pais e descricao
# Calcule soma, média e contagem
# Explique em comentário o que essa tabela representa

df_groupby_multiplo = df.groupby(["nome_pais", "descricao"]).agg({
    "valor": ["sum", "mean", "count"]
})
print(df_groupby_multiplo)
# Essa tabela mostra, para cada combinação de país e produto, o total exportado (soma), média e contagem de operações.

# ===========================================================
# PARTE 5 – PIVOT TABLE
# ===========================================================

# Exercício 7 – Pivot por Produto
# Linhas: periodo
# Colunas: descricao
# Valores: soma de valor

# Responda:
# 1. Qual produto vendeu mais?
produto_mais_vendido = df_groupby_multiplo["valor"]["sum"].idxmax()
print("Produto mais vendido:", produto_mais_vendido)

# 2. Qual mês teve maior valor total?
df_pivot_produto = df.pivot_table(index="periodo", columns="descricao", values="valor", aggfunc="sum")
mes_maior_valor = df_pivot_produto.sum(axis=1).idxmax()
print("Mês com maior valor total:", mes_maior_valor)

# 3. Existe mês sem venda?
meses_com_venda = df_pivot_produto.sum(axis=1) > 0
meses_sem_venda = meses_com_venda[~meses_com_venda].index.tolist()
print("Meses sem venda:", meses_sem_venda)


# Exercício 8 – Pivot por País
# Linhas: periodo
# Colunas: nome_pais
# Valores: soma de valor
# Explique o que podemos interpretar dessa tabela

df_pivot_pais = df.pivot_table(index="periodo", columns="nome_pais", values="valor", aggfunc="sum")
print(df_pivot_pais)
# Essa tabela mostra o total exportado por país em cada período. Podemos comparar o desempenho de cada país ao longo do tempo e identificar tendências ou sazonalidades nas exportações.

# ===========================================================
# PARTE 6 – FEATURE ENGINEERING
# ===========================================================

# Exercício 9
# 1. Extraia ano e mês da coluna periodo
df["ano"] = df["periodo"].dt.year
df["mes"] = df["periodo"].dt.month

# 2. Crie coluna valor_mil (valor / 1000)
df["valor_mil"] = df["valor"] / 1000

# 3. Calcule crescimento percentual por produto mês a mês
df["crescimento_percentual"] = df.groupby("descricao")["valor"].pct_change() * 100


# ===========================================================
# PARTE 7 – QUALIDADE DE DADOS
# ===========================================================

# Exercício 10
# 1. Verifique valores nulos
print(df.isnull().sum())

# 2. Verifique valores negativos
valores_negativos = df[df["valor"] < 0]
print("Valores negativos:")
print(valores_negativos)

# 3. Verifique duplicatas
duplicatas = df[df.duplicated()]
print("Duplicatas:")
print(duplicatas)
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\alexm\OneDrive\Documentos\Analise de Dados\Exercícios-DataFrame\notas.csv")

# ============================================================
# EXPLORAÇÃO INICIAL (EDA BÁSICA)
# ============================================================

# Exercício 1 – Conhecendo o Dataset 
# 1. Quantas linhas e colunas existem? 
df.shape
(2200,14)

# 2. Quais são os tipos de dados? 
df.dtypes

# 3. Existe coluna com valores ausentes?
df.isnull().sum()

# 4. Qual é o período de anos disponível? 
df.columns
df.loc[:,"year"].unique()

# 5. Quantos países diferentes existem?
df.loc[:,"country"].unique()

# Exercício 2 – Estatísticas Gerais 
# 1. Média do score 
df.columns
df.loc[:,"score"].mean()

# 2. Maior score 
df.loc[:,"score"].max()

# 3. Menor score 
df.loc[:,"score"].min()

# 4. Média do score por ano
df.groupby("year")["score"].mean()

# 5. Desvio padrão do score
df.loc[:,"score"].std()

# ============================================================
# FILTROS E SELEÇÕES
# ============================================================

# Exercício 3 – Top Universidades 
# 1. Mostre as 10 melhores universidades do mundo (menor world_rank)
df.columns
df.loc[0:9,["institution","world_rank","year"]].sort_values("world_rank")

# 2. Mostre as 5 melhores universidades do Brasil (se existirem)
df.columns
filtro = df["country"]=="Brazil"
df_brazil = df.loc[filtro , ["institution","national_rank","country","year"]].sort_values("national_rank")
df_brazil.iloc[0:5]

# 3. Mostre universidades com score maior que 90
filtro = df["score"]>90
df.loc[filtro, ["institution", "world_rank", "country", "score", "year"]].sort_values("score", ascending=False)

# 4. Mostre universidades dos EUA com score maior que 80
filtro = (df["country"]=="United States") & (df["score"]>80)
df.loc[filtro, ["institution", "world_rank", "country", "score", "year"]].sort_values("score", ascending=False)

# Exercício 4 – Seleção Avançada 
# 1. Mostre apenas as colunas: institution, country e score 
df.loc[:, ["institution", "country", "score"]]

# 2. Mostre universidades entre rank 50 e 100 
filtro = (df["world_rank"]>=50) & (df["world_rank"]<=100)
df.loc[filtro , ["institution", "world_rank", "country", "year"]].sort_values("world_rank")

# 3. Mostre universidades cujo país é “United Kingdom”
df.columns
filtro = df["country"]=="United Kingdom"
df.loc[filtro , ["institution","national_rank","country","year"]].sort_values("national_rank")

# ============================================================ PARTE 3 –
# MISSING VALUES
# ============================================================

# Exercício 5 – Valores Ausentes 
# 1. Quantos valores nulos existem na coluna broad_impact? 
df.loc[:,"broad_impact"].isnull().sum()

# 2. Qual percentual do dataset é nulo? 
(df.loc[:,"broad_impact"].isnull().sum() / len(df)) * 100

# 3. Remova linhas com broad_impact nulo 
df_limpo = df.dropna(subset=["broad_impact"])

# 4. Preencha valores nulos com a média 
media_broad_impact = df.loc[:,"broad_impact"].mean()
df_preenchido = df.copy()
df_preenchido.loc[:,"broad_impact"] = df_preenchido.loc[:,"broad_impact"].fillna(media_broad_impact)

# 5. Compare a média antes e depois do preenchimento
media_antes = df.loc[:,"broad_impact"].mean()
media_depois = df_preenchido.loc[:,"broad_impact"].mean()

# ============================================================ PARTE 4 –
# GROUPBY (ANÁLISE POR PAÍS E ANO)
# ============================================================

# Exercício 6 – Análise por País 
# 1. Média do score por país 
df.groupby("country")["score"].mean()

# 2. País com maior média de score 
df.groupby("country")["score"].mean().idxmax()

# 3. Quantidade de universidades por país 
df.groupby("country")["institution"].count()

# 4. Top 10 países com mais universidades
df.groupby("country")["institution"].count().sort_values(ascending=False).head(10)

# Exercício 7 – Análise por Ano 
# 1. Média do score por ano 
df.groupby("year")["score"].mean()

# 2. Qual ano teve maior média? 
df.groupby("year")["score"].mean().idxmax()

# 3. Faça um gráfico da evolução do score médio ao longo do tempo

media_por_ano = df.groupby("year")["score"].mean()
media_por_ano.plot(kind="line", title="Evolução do Score Médio ao Longo do Tempo")
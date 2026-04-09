#Programação para Análise de Dados - Exercício AC
# Alexandre de Sousa Campos Menezes

import pandas as pd
import requests

# ===========================================================

# Questão 1: Carregar o DataFrame
# LER arquivo titanic.csv em um DataFrame pandas chamado df?

df = pd.read_csv("titanic.csv")
print(df.head())

# Questão 2: Filtrar passageiros do sexo feminino
# Filtrar o DataFrame para mostrar apenas as Mulheres?
# (Dica: Filtar onde a coluna "Sex" é igual a "female")

df_female = df[df['Sex'] == 'female']
print(df_female.head())

# Questão 3: Contar sobreviventes
# Quantos passageiros Sobreviveram?
# (Dica: Sobreviventes têm o valor 1 na coluna "Survived")

survivors = df[df['Survived'] == 1]
num_survivors = survivors.shape[0]
print(f"Number of survivors: {num_survivors}")

# Questão 4: Quantos Homens Sobreviveram?

survived_men = df[(df['Survived'] == 1) & (df['Sex'] == 'male')]
num_survived_men = survived_men.shape[0]
print(f"Number of survived men: {num_survived_men}")

# Questão 5: Calcular Nome "John"
# Calcular quantos passageiros tem o nome "John"?
# (Dica: Usar a coluna "Name")

num_johns = df[df['Name'].str.contains('John', case=False)].shape[0]
print(f"Number of passengers named John: {num_johns}")

# Média idades
average_age = df['Age'].mean()
print(f"Média de idade dos passageiros: {average_age:.2f}")

# -------------------------------------------------
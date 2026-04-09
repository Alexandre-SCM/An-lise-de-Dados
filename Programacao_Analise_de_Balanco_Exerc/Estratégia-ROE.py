import pandas as pd
import requests

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyMDM2LCJpYXQiOjE3NzQzNTAwMzYsImp0aSI6ImU1NDAzNjRiOWI3NDRjMTU4ZDY1NWJjN2FmYThiNDU3IiwidXNlcl9pZCI6IjEwOCJ9.8cudFqtCuoWJWUdsI6mJ0hQhHpRwryRULmfUxxgoA4c"
resp = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2026-03-23"},
)
dados = resp.json()
df = pd.DataFrame(dados)
maximo = df["roe"].max()
filtro = df["roe"]==maximo
df[filtro]

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyMDM2LCJpYXQiOjE3NzQzNTAwMzYsImp0aSI6ImU1NDAzNjRiOWI3NDRjMTU4ZDY1NWJjN2FmYThiNDU3IiwidXNlcl9pZCI6IjEwOCJ9.8cudFqtCuoWJWUdsI6mJ0hQhHpRwryRULmfUxxgoA4c"
params = {"ticker": "MNPR3", "data_ini": "2025-03-21", "data_fim": "2026-03-23"}
resp = requests.get(
    f"{base_url}/preco/corrigido",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)
dados = resp.json()
df_preco = pd.DataFrame(dados)

# Rendimento do Papel
df_preco = pd.DataFrame(dados)

# corrigir tipo
df_preco["fechamento"] = pd.to_numeric(df_preco["fechamento"])

# garantir formato de data e ordenação
df_preco["data"] = pd.to_datetime(df_preco["data"])
df_preco = df_preco.sort_values("data")

# pegar extremos
preco_inicial = df_preco.iloc[0]["fechamento"]
preco_final = df_preco.iloc[-1]["fechamento"]

# cálculo
retorno = (preco_final / preco_inicial) - 1
print(f"Retorno total: {retorno:.2%}")

# API para pegar o IBov
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "SEU_JWT"
params = {"ticker": "ibov", "data_ini": "2025-03-21", "data_fim": "2026-03-23"}
resp = requests.get(
    f"{base_url}/preco/diversos",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
)
dados = resp.json()
df_ibov = pd.DataFrame(dados)

# corrigir tipo
df_ibov["fechamento"] = pd.to_numeric(df_ibov["fechamento"])

# garantir formato de data e ordenação
df_ibov["data"] = pd.to_datetime(df_ibov["data"])
df_ibov = df_ibov.sort_values("data")

# pegar extremos
preco_inicial = df_ibov.iloc[0]["fechamento"]
preco_final = df_ibov.iloc[-1]["fechamento"]

# cálculo
retorno_ibov = (preco_final / preco_inicial) - 1

print(f"Retorno IBOV: {retorno_ibov:.2%}")
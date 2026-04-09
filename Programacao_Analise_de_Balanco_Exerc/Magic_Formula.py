import pandas as pd
import requests

# Período -> 5 anos

base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyMDM2LCJpYXQiOjE3NzQzNTAwMzYsImp0aSI6ImU1NDAzNjRiOWI3NDRjMTU4ZDY1NWJjN2FmYThiNDU3IiwidXNlcl9pZCI6IjEwOCJ9.8cudFqtCuoWJWUdsI6mJ0hQhHpRwryRULmfUxxgoA4c"
resp = requests.get(
    f"{base_url}/bolsa/planilhao",
    headers={"Authorization": f"Bearer {token}"},
    params={"data_base": "2021-04-01"},
)
dados = resp.json()
df = pd.DataFrame(dados)

df2 = df[["ticker", "roic", "earning_yield"]]
df2['rank_roic'] = df2['roic'].rank(ascending=False)
df2['rank_p_ey'] = df2['earning_yield'].rank(ascending=False)
df2['rank_final'] = (df2['rank_roic'] + df2['rank_p_ey']) / 2
df2.sort_values('rank_final', ascending=False)['ticker'][:20]

# Resultado da Carteira:
base_url = "https://laboratoriodefinancas.com/api/v2"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc2OTQyMDM2LCJpYXQiOjE3NzQzNTAwMzYsImp0aSI6ImU1NDAzNjRiOWI3NDRjMTU4ZDY1NWJjN2FmYThiNDU3IiwidXNlcl9pZCI6IjEwOCJ9.8cudFqtCuoWJWUdsI6mJ0hQhHpRwryRULmfUxxgoA4c"

tickers = [
    "BRKM5","BRKM3","TEKA4","RNEW3","RNEW11","RIAA3","RNEW4","AALR3",
    "APER3","SBFG3","PRNR3","BRML3","TCNO3","TCNO4","SOMA3","MYPK3",
    "ENJU3","TECN3","CEAB3","OIBR4"
]

for ticker in tickers:

    params = {
        "ticker": ticker,
        "data_ini": "2021-04-01",
        "data_fim": "2026-03-31",
    }
    resp = requests.get(
    f"{base_url}/preco/corrigido",
    headers={"Authorization": f"Bearer {token}"},
    params=params,
    )
    dados = resp.json()
    df_preco = pd.DataFrame(dados)

    df_preco = pd.DataFrame(dados)

    df_preco["fechamento"] = pd.to_numeric(df_preco["fechamento"])

    df_preco["data"] = pd.to_datetime(df_preco["data"])
    df_preco = df_preco.sort_values("data")

    preco_inicial = df_preco.iloc[0]["fechamento"]
    preco_final = df_preco.iloc[-1]["fechamento"]

    retorno = (preco_final / preco_inicial) - 1
    print(f"Retorno total: {retorno:}")

# Aplicando um peso proporcional de 5% a cada ação.
peso = 0.05
retorno_total = 0
for ticker in tickers:
    params = {
        "ticker": ticker,
        "data_ini": "2021-04-01",
        "data_fim": "2026-03-31",
    }
    resp = requests.get(
        f"{base_url}/preco/corrigido",
        headers={"Authorization": f"Bearer {token}"},
        params=params,
    )
    dados = resp.json()
    df_preco = pd.DataFrame(dados)

    df_preco["fechamento"] = pd.to_numeric(df_preco["fechamento"])
    df_preco["data"] = pd.to_datetime(df_preco["data"])
    df_preco = df_preco.sort_values("data")

    preco_inicial = df_preco.iloc[0]["fechamento"]
    preco_final = df_preco.iloc[-1]["fechamento"]

    retorno = (preco_final / preco_inicial) - 1
    retorno_total += peso * retorno

print(f"Retorno total da carteira: {retorno_total}")

# API para pegar o IBov
import yfinance as yf

ibov = yf.download("^BVSP", start="2021-04-01", end="2026-03-31")

data_inicio = pd.to_datetime("2021-04-01")
data_fim = pd.to_datetime("2026-03-31")

ibov_inicial = ibov.loc[ibov.index >= data_inicio, "Close"].iloc[0].item()
ibov_fim = ibov.loc[ibov.index <= data_fim, "Close"].iloc[-1].item()

print(f"Retorno IBOV: {ibov_fim/ibov_inicial - 1:.2%}")
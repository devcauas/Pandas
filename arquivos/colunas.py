#%%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep=";")
df
# %%

df.shape
# %%

df.info(memory_usage='deep')
# %%

df.dtypes
# %%

renamed_columns = {
    "qtdePontos": "qtPontos",
    "descSistemaOrigem": "SistemaOrigem"
    }
# %%

df.rename(columns=renamed_columns, inplace=True)
# %%

df[["IdCliente", "QtdePontos"]].tail(5)
# %%

df
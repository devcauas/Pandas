# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv", sep=';')
df
# %%

df.to_csv("clientes.csv")

# %%

df.to_parquet("clientes.parquet", index=False)

# %%

df.to_parquet("clientes.csv", index=False)

# %%

df_2 = pd.read_parquet("clientes.parquet")
df_2

# %%

df.to_excel("clientes.xlsx", index=False)
# %%

df_3 = pd.read_excel("clientes.xlsx")
df_3
# %%

df_bobo = pd.read_csv("../data/bobo.csv", sep=";")
df_bobo
# %%

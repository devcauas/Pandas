#%%

import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv", sep=";")
df_clientes
# %%

df_clientes.head(n=10)
# %%

df_clientes.tail()
# %%

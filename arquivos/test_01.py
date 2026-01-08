# %%

import pandas as pd
df = pd.read_csv("../data/vendas.csv", sep=',')
df.head()
df.info()
df.describe()

# %%

df.rename(columns={"data": "datetime"})

# %%

df['valor_total'] = df['quantidade'] * df['preco_unitario']
df
# %%

dataframe_concluido = pd.DataFrame(data='status')
dataframe_concluido
# %%

df['faturamento_total'] = df['quantidade'] * df['preco_unitario']

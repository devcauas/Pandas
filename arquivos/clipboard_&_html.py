# %%

import pandas as pd
import requests

df = pd.read_clipboard(sep=";")
df

# %%

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
response.raise_for_status()  # para garantir que não houve erro HTTP

dfs = pd.read_html(response.text)
dfs

# %%

df_uf = dfs[1]
df_uf.to_csv("ufs.csv", sep=";", index=False)
# %%

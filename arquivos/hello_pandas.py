# %%

idades = [
    32,38,30,31,30,
    35,25,29,37,31,
    27,23,33,32,36,
]

media = sum(idades) / len(idades)
print("Media:",media)

diffs = 0
for i in idades:
    diffs += (i - media) ** 2

variancia = diffs / (len(idades)-1)

print("Variancia:",variancia)

# %%

import pandas as pd

idades = [
    32,38,30,31,30,
    35,25,29,37,31,
    27,23,33,32,36,
]

series_idades = pd.Series(idades)
series_idades

# %%

media_idade = series_idades.mean()
var_idade = series_idades.var()
sumary_idade = series_idades.describe()
sumary_idade

# %%


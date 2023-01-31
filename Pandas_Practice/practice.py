# %%
import pandas as pd
df = pd.read_csv('pokemon_data.csv')
print(df.head(3))

# %%
print(df.columns)

# %%
print(df[['Name', 'Type 1', 'HP']])
# %%
print(df.iloc[0, 0])

# %%
print(df.iloc[4:10])

# %%
for index, rows in df.iterrows():
    print(index, rows['Name'])
# %%
print(df.loc[0])

# %%
print(df.describe())

# %%
print(df.sort_values(['Type 1', 'HP'], ascending=[1, 1])[['Type 1', 'HP']])

# %%
print(df.iloc[:, 4:10].sum(axis=1))
# %%

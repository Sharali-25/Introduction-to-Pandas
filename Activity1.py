import pandas as pd
scores = [456,342,167,401,725]
players = pd.Series(scores, index = ["Shayna", "Shardul","Siddhartha","Sharol","Sharali"])
print(players)

print()
data = {
    'player' : ["Shayna","Shardul","Siddhartha","Sharol","Sharali"],
    'levels' : [42,38,35,30,25],
    'scores' : [456,342,167,401,725],
    'wins' : [210,185,162,140,250]
}
df = pd.DataFrame(data)
print(df)

print(df.loc[0])
print()
print(df.loc[2:3])

full_df = pd.read_csv("leaderboard.csv")
print(full_df.head())

print()

print(full_df.tail(3))

print()
print(full_df.info())

print()
x = full_df.dropna()
print(x.to_string())
print()
print(x)

print()
y = full_df.fillna(0)
print(y.to_string())
print(y)
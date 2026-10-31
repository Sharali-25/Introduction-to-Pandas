import pandas as pd
scores = [45,56,32,43,74]
players = pd.Series(scores, index = ["Aarav","Meera","Shubhangni","Neha","Kajal"])
print(players)

print()
data = {
    "players":  ["Aarav","Meera","Shubhangni","Neha","Kajal"],
    "levels" : [34,2,6,23,7],
    "scores" : [45,56,32,43,74],
    "wins" : [2,4,6,10,8]

}
df = pd.DataFrame(data)
print(df)
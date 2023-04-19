import pandas as pd

d ={"Name": ['Katja', 'Nina', 'Sven', 'Matthias','Katja', 'Nina', 'Sven', 'Matthias','Katja', 'Nina', 'Sven', 'Matthias'],
    "Alter": [32, 32, 36, 31,32, 32, 36, 31,32, 32, 36, 31],
    "Ort":['Berlin', 'München', 'Frankfurt', 'Köln','Berlin', 'München', 'Frankfurt', 'Köln','Berlin', 'München', 'Frankfurt', 'Köln']
}
df = pd.DataFrame(d)

print(df.head())  #zeigt erste 5
print(df.columns)
print(df[["Name","Alter"]])
df.iloc
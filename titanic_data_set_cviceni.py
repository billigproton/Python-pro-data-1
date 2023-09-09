import pandas
# 1 - načtení do Data Frame a do proměnné titanic 

titanic = pandas.read_csv('titanic.csv')

# 2 - zobrazení názvu sloupců

print(titanic.columns)

# 3 - kolik má dataset řádků?

print(titanic.shape)

# 4 - průměrný věk pasažérů?, 5 - nejstarší pasažér?

print(titanic.describe())






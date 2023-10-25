# Pokročilé úpravy

import pandas

#u202 = pandas.read_csv("https://kodim.cz/cms/assets/kurzy/python-data-1/python-pro-data-1/agregace-a-spojovani/u202.csv")
#u203 = pandas.read_csv("https://kodim.cz/cms/assets/kurzy/python-data-1/python-pro-data-1/agregace-a-spojovani/u203.csv")
#u302 = pandas.read_csv("https://kodim.cz/cms/assets/kurzy/python-data-1/python-pro-data-1/agregace-a-spojovani/u302.csv")


trida1 = pandas.read_csv('u202.csv')

#print(trida1['znamka'].isnull()) # vrátí pro každý řádek boolean, zda obsahuje prázdnou hodnotu

u202 = pandas.read_csv('u202.csv').dropna() # Vrátí dataset očištěn od chybějících dat
u203 = pandas.read_csv('u203.csv').dropna()
u302 = pandas.read_csv('u302.csv').dropna()

#u302 = pandas.read_csv('u302.csv').dropna(axis=1) # odstraní všechny sloupce, které obsahují chybějící data

#u302 = pandas.read_csv('u302.csv').fillna(x) # nahradí všechna chybějící data a hodnoty hodnotou x
u202['mistnost'] = 'u202' # nový sloupec 'místnost', abychom věděli, kdo maturoval v jaké místnosti
u203['mistnost'] = 'u203'
u302['mistnost'] = 'u302'
maturita = pandas.concat([u202, u203, u302], ignore_index=True) # spojení tabulek do jedné - UNION, ignore_index - přepočítání indexu

#maturita.to_csv('maturita.csv', index=False) # převod výsledného datasetu do CSV

# Propojení dat

studenti = pandas.read_csv('studenti.csv')
print(studenti.head())

propojeny_df = pandas.merge(u202, studenti)
print(propojeny_df.head())

print(u202.shape)
print(propojeny_df.shape)

preds = pandas.read_csv('https://kodim.cz/cms/assets/analyza-dat/python-data-1/python-pro-data-1/agregace-a-spojovani/propojeni-dat/predsedajici.csv')

novy_propojeny_df = pandas.merge(propojeny_df, preds, on=['den'], how="outer")
print(novy_propojeny_df.head())

print(novy_propojeny_df.shape)

print(novy_propojeny_df[novy_propojeny_df["datum"].isnull()])

preds["den"] = preds["den"].str.strip()
novy_propojeny_df = pandas.merge(propojeny_df, preds, on=['den'], how="outer")
print(novy_propojeny_df.shape)

novy_propojeny_df = novy_propojeny_df.rename(columns={'jmeno_x': 'jmeno', 'jmeno_y': 'predseda'})
print(novy_propojeny_df)


# Agregace

maturita.groupby('mistnost')

print(maturita.groupby('mistnost').count())

print(maturita.groupby('predmet')['znamka'].mean())


nakupy = pandas.read_csv('nakupy.csv')
nakupy_celkem = nakupy.groupby('jmeno')['cena'].sum() 
print(nakupy_celkem)


# Počítané sloupce

staty = pandas.read_json("staty.json")
staty = staty.set_index("name")

staty["population_density"] = staty["population"] / staty["area"] # Poznámka: pandas nás neupozorní, pokud sloupec již existuje, musíme si tedy dát pozor, abychom nepřepsali nějaký existující sloupec.

 # Řazení

staty.sort_values(by="population") # jako ORDER BY u SQL, defaultně se řadí vzestupně

staty.sort_values(by="population", ascending=False) # abych nastavil sestupné (descending) řazení






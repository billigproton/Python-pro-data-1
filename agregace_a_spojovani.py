import pandas

#u202 = pandas.read_csv("https://kodim.cz/cms/assets/kurzy/python-data-1/python-pro-data-1/agregace-a-spojovani/u202.csv")
#u203 = pandas.read_csv("https://kodim.cz/cms/assets/kurzy/python-data-1/python-pro-data-1/agregace-a-spojovani/u203.csv")
#u302 = pandas.read_csv("https://kodim.cz/cms/assets/kurzy/python-data-1/python-pro-data-1/agregace-a-spojovani/u302.csv")


trida1 = pandas.read_csv('u202.csv')

#print(trida1['znamka'].isnull()) # vrátí pro každý řádek boolean, zda obsahuje prázdnou hodnotu

u202 = pandas.read_csv('u202.csv').dropna() # Vrátí datase očištěn od chybějících dat
u203 = pandas.read_csv('u203.csv').dropna()
u302 = pandas.read_csv('u302.csv').dropna()

#u302 = pandas.read_csv('u302.csv').dropna(axis=1) # odstraní všechny sloupce, které obsahují chybějící data

#u302 = pandas.read_csv('u302.csv').fillna() # nahradí všechna chybějící data a hodnoty hodnotou x
u202['mistnost'] = 'u202' # nový sloupec 'místnost', abychom věděli, kdo maturoval v jaké místnosti
u203['mistnost'] = 'u203'
u302['mistnost'] = 'u302'
maturita = pandas.concat([u202, u203, u302], ignore_index=True) # spojení tabulek do jedné - UNION, ignore_index - přepočítání indexu

maturita.to_csv('maturita.csv', index=False) # převod výsledného datasetu do CSV



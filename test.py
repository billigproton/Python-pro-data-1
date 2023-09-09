import pandas
nakupy = pandas.read_csv('nakupy.csv')
print(nakupy)

nakupy.info() # Základní přehled o hodnotách a sloupcích
print(nakupy.describe()) # základní statistický přehled o Data Framu, obaleno do printu - z nějakého důvodu nefungovalo
print(nakupy.shape) # Počet řádků, sloupců 
print(nakupy.columns) # Názvy všech sloupců

print(nakupy.head()) # vypíše prvních několik řádků 
print(nakupy.tail()) # vypíše posledních několik řádků 

# Vyběr sloupců

print(nakupy['vec']) # vybere daný sloupec + indexový sloupec (výstupem datový typ Série (Series))
print(nakupy[['vec']]) # pokud chceme aby výstupem byl Data Frame a né Series

print(nakupy[['jmeno', 'cena']]) # výběr více sloupců (výstupem datový typ Data Frame)





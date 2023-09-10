import pandas
staty = pandas.read_json("staty.json")
staty.set_index("name", inplace=True)

#print(staty["population"])

populace = staty["population"]
print(populace.sum()) # k čemu je dobrá Série? Můžeme pomocí ní třeba dělat sum prvků, které obsahuje

print(staty["population"] < 1000) # podmíněný výběr pomocí query - nejmenší státy pod tisíc obyvatel

pidistaty = staty[staty["population"] < 1000] # podmínku ale nutno OBALIT DO HRANATÝCH ZÁVOREK
print(pidistaty[["population", "area"]])

 # Spojení více podmínek 
    
    # AND

lidnate_evropske_staty = staty[(staty["population"] > 20000000) & (staty["region"] == "Europe")] # státy s více než 20 miliony obyvatel A ZÁROVEŇ musí být v Evropě
print(lidnate_evropske_staty["population"])

    # OR

print(staty[(staty["population"] > 10_000_000_000) | (staty["area"] > 3_000_000)]) # státy s více než 10 miliardy obyvatel NEBO státy s rozlohou větší než 3 000 000 km2

    # zjednodušení spojování pomocí IN

print(staty[staty["subregion"].isin(["Western Europe", "Eastern Europe"])])

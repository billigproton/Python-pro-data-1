# Česká jména 2

import pandas

jmena = pandas.read_csv('jmena.csv')

# 1 - lidé starší 60 let

starsi_lide = jmena[jmena['věk'] > 60]

print(starsi_lide)

# 2 - četnost je mezi 80 000 a 100 000

cetnost_80_100_tisic = jmena[(jmena['četnost'] >= 80_000) & (jmena['četnost'] <= 100_000 )]

print(cetnost_80_100_tisic)

# 3 - jména se slovanským nebo hebrejským původem + kolik jich je?|

slovane_hebrejci1 = jmena[(jmena['původ'].isin(['hebrejský', 'slovanský']))]
    # nebo
slovane_hebrejci2 = jmena[(jmena['původ'] == 'hebrejský') | (jmena['původ'] == 'slovanský')]

print(slovane_hebrejci1)

    # Kolik takovách jmen je? - cesta přes count()

print(slovane_hebrejci1.count())

    # Kolik takových jmen je? - cesta přes len()

pocet_radku = len(slovane_hebrejci1)

print(pocet_radku)

# 4 - jména se svátkem první 3 dny v prosinci

svatek_prosinec = jmena[jmena['svátek'].isin(['1.12', '2.12', '3.12'])]

print(svatek_prosinec)
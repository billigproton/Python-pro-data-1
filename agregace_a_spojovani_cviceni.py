# Studenti

import pandas

jmena = pandas.read_csv("jmena.csv")
s1 = pandas.read_csv("studenti1.csv")
s2 = pandas.read_csv("studenti2.csv")

# 1 - spojení studentů do jednoho datasetu studenti

studenti = pandas.concat([s1, s2], ignore_index=True)

# 2 - kolik nestudentů, kolik dálkových?

nestudenti = studenti[studenti["ročník"].isnull()]
print(nestudenti.shape)

dalkari = studenti[studenti["kruh"].isnull()]
print(dalkari.shape)

# 3 - vyčištění datasetu studenti od dálkařů a nestujících

studenti = studenti.dropna()

# 4 - počet prezenčních studentů na každý obor

prezencni_studenti = studenti.groupby('obor')['jméno'].count()

print(prezencni_studenti)

# 5 - průměrný prospěch studentů v každém oboru

prumerny_prospech = studenti.groupby('obor')['prospěch'].mean()

print(prumerny_prospech)

# 6 - propojení datasetu se jmény a se studenty

pohlavi_studentu = pandas.merge(studenti, jmena, on=['jméno']) # bude to inner join přes sloupec 'jméno'

# 7 - Kolik na fakultě studuje mužů a žen?

pocet_muzu_zen = pohlavi_studentu.groupby('pohlaví').count()

print(pocet_muzu_zen)





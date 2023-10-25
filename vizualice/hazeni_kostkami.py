# Házení kostkami

import pandas
import matplotlib.pyplot as plt

kostky = pandas.read_csv("kostky.csv")

kostky.hist(bins=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
#kostky.hist(bins=11) zde lze stanovit přihrádky i takto
plt.show()
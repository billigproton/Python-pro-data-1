# Call centrum

import pandas
import  matplotlib.pyplot as plt

callcentrum = pandas.read_csv("https://kodim.cz/cms/assets/analyza-dat/python-data-1/python-pro-data-1/vizualizace/excs/call-centrum/callcentrum.csv")
callcentrum = callcentrum["hodnota"].str.split(':', expand=True).astype(int)

callcentrum["vteriny"] = callcentrum[0] * 60 + callcentrum[1]

callcentrum["vteriny"].hist()
plt.show()

# import global libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
class Plot:
    def __init__(self, data, path):
        self.data = data
        self.path = path
        self.hist_observation()
        self.heatmap()
    def hist_observation(self):
        fig, ax = plt.subplots()
        self.data[["Cost of Living Index", "Rent Index", "Restaurant Price Index"]].hist(bins=30, figsize=(1500,1000), ax=ax)
        fig.savefig("{}/historgram.png".format(self.path))
    def heatmap(self):
        fig, ax = plt.subplots()
        d = self.data[['Cost of Living Index', 'Rent Index',
       'Cost of Living Plus Rent Index', 'Groceries Index',
       'Restaurant Price Index', 'Local Purchasing Power Index',]]
        dataplot = sns.heatmap(d.corr(), annot=True, cmap="YlGnBu")
        fig.savefig("{}/heatmap.png".format(self.path))
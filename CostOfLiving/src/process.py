from preprocessing.dataloading import DataIngestion
from preprocessing.processing import Preprocessing
from preprocessing.plots import Plot
from modelbuilding.model import ModelBuilding 

#import the dataset
di = DataIngestion()
di.load_data(path="data/costofliving.csv")
processing = Preprocessing(di.df)
df = processing.encode_categorical()
Plot(df)
ModelBuilding(df)

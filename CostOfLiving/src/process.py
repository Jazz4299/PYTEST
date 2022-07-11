import argparse
from preprocessing.dataloading import DataIngestion
from preprocessing.processing import Preprocessing
from preprocessing.plots import Plot
from modelbuilding.model import ModelBuilding



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv")
    parser.add_argument("plot")
    parser.add_argument("comparision")
    args = parser.parse_args()
    #import the dataset
    di = DataIngestion()
    di.load_data(path=args.csv)
    processing = Preprocessing(di.df)
    df = processing.encode_categorical()
    m =ModelBuilding(df, path=args.plot)
    m.visualize(args.comparision)

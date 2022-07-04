#importing global libraries
import pandas as pd

class DataIngestion:
    """
    Class responsible for 
    loading the data
    """
    def load_data(self, path):
        """
        Function for loading the dataset
        """
        self.df = None
        try:

            self.df = pd.read_csv(path)
            return self.df
        except FileNotFoundError:
            raise FileNotFoundError("The data file does not exist.")
"""
Cleaning the data for visualization
"""
#import global libraries
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
class Preprocessing:
    """
    Class responsible for preprocessing
    """
    def __init__(self, data):
        self.data  = data
        self.check_remove_null()
        self.process_city()
        #self.description()


    def check_remove_null(self):
        """
        dropping the column if all 
        values are null
        """
        self.data = self.data.loc[:, self.data.isin([' ', np.nan]).mean() < .6]
        self.data.dropna()

    def process_city(self):
        """
        Converting city column into 
        two different columns
        """
        city_list = list()
        country_list = list()
        for city in self.data["City"]:
            city_list.append(city.split(", ")[0])
            country_list.append(city.split(", ")[-1])
        self.data.drop(["City"], axis=1)
        self.data['City'] = city_list
        self.data['Country'] =  country_list

    def description(self):
        print(self.data['City'].value_counts())
        print(self.data['Country'].value_counts())
        print(self.data)
    
    def encode_categorical(self):
        #which method to use for encoding: using Label encoding
        le_city = LabelEncoder()
        self.data['City'] = le_city.fit_transform(self.data['City'])
        le_country = LabelEncoder()
        self.data['Country'] = le_country.fit_transform(self.data['Country'])
        return self.data

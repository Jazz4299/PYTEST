import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score, KFold
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt 

class ModelBuilding:

    def __init__(self, df, X_train=None, X_test=None,
    y_train=None, y_test=None):
        self.data = df
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.y_pred = None
        self.split()
        self.train()
        self.predict()

    def split(self):
        X = self.data[['City', 'Cost of Living Index', 'Rent Index',
       'Cost of Living Plus Rent Index', 'Groceries Index',
       'Restaurant Price Index', 'Local Purchasing Power Index', 'Country']]
        y = self.data['Cost of Living Index']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y,
        test_size=0.3)
    
    def train(self):
        self.xgbr = xgb.XGBRegressor(verbosity=0)
        self.xgbr.fit(self.X_train, self.y_train)
        score = self.xgbr.score(self.X_train, self.y_train)
        print("Training score: ", score)
    
    def predict(self):
        self.y_pred = self.xgbr.predict(self.X_test)
        mse = mean_squared_error(self.y_test, self.y_pred)
        print(mse)

    def visualize(self, path):
        fig, ax = plt.subplots()
        x_ax = range(len(self.y_test))
        plt.plot(x_ax, self.y_test, label="original")
        plt.plot(x_ax, self.y_pred, label="predicted")
        plt.title("test and predicted data")
        plt.legend()
        plt.savefig(path)

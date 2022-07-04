import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score, KFold
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt 

class ModelBuilding:

    def __init__(self, df):
        self.data = df
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.split()
        self.train()
        self.predict()
        self.visualize()

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

    def visualize(self):
        fig, ax = plt.subplots()
        x_ax = range(len(self.y_test))
        plt.plot(x_ax, self.y_test, label="original")
        plt.plot(x_ax, self.y_pred, label="predicted")
        plt.title("test and predicted data")
        plt.legend()
        plt.savefig("data/comparison.png")
        plt.show()

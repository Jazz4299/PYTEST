"""
Unit Test cases for model.py file
"""
import pytest
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
import pandas as pd
import os
from src.modelbuilding.model import ModelBuilding
def test_split(mocker):
    mocker.patch("src.modelbuilding.model.ModelBuilding.train", return_value=None)
    mocker.patch("src.modelbuilding.model.ModelBuilding.predict", return_value=None)
    df = pd.read_csv("tests/unit_tests/test_data/sample.csv")
    df["Country"] = ["USA"] * len(df)
    df["City"] = ["New York City"] * len(df)
    m = ModelBuilding(df)
    assert isinstance(m.X_train, pd.DataFrame)
    assert isinstance(m.X_test, pd.DataFrame)
    assert isinstance(m.y_train, pd.Series)
    assert isinstance(m.y_test, pd.Series)

@pytest.fixture()
def sample_split():
    data = pd.read_csv("tests/unit_tests/test_data/sample.csv")
    data["Country"] = 0
    data["City"] = 0
    X = data[['City', 'Cost of Living Index', 'Rent Index',
       'Cost of Living Plus Rent Index', 'Groceries Index',
       'Restaurant Price Index', 'Local Purchasing Power Index', 'Country']]
    y = data['Cost of Living Index']
    X_train, X_test, y_train, y_test = train_test_split(X, y,
        test_size=0.2)
    return X_train, X_test, y_train, y_test

def test_train(mocker, sample_split):
    mocker.patch("src.modelbuilding.model.ModelBuilding.split", return_value=None)
    mocker.patch("src.modelbuilding.model.ModelBuilding.predict", return_value=None)
    df = pd.read_csv("tests/unit_tests/test_data/sample.csv")
    print("sample split")
    print(sample_split[0])
    m = ModelBuilding(df, X_train= sample_split[0], X_test=sample_split[1],
    y_train=sample_split[2], y_test=sample_split[3])
    assert m.xgbr is not None


def test_visualize(mocker, sample_split):
    mocker.patch("src.modelbuilding.model.ModelBuilding.split", return_value=None)
    mocker.patch("src.modelbuilding.model.ModelBuilding.predict", return_value=None)
    mocker.patch("src.modelbuilding.model.ModelBuilding.train", return_value=None)
    m = ModelBuilding(None, X_train= sample_split[0], X_test=sample_split[1],
    y_train=sample_split[2], y_test=[33, 34, 77])
    m.y_pred = [35, 22, 79]
    m.visualize("tests/unit_tests/test_data/comparison.png")
    assert os.path.isfile("tests/unit_tests/test_data/comparison.png")


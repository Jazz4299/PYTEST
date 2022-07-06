"""
Test Cases for plots
"""
import pytest
import os
import pandas as pd
from src.preprocessing.plots import Plot
def test_hist_observation(mocker):
    mocker.patch("src.preprocessing.plots.Plot.heatmap", return_value=None)
    path = "tests/unit_tests/test_data"
    data = pd.read_csv("tests/unit_tests/test_data/sample.csv")
    p = Plot(data, path)
    assert os.path.isfile("tests/unit_tests/test_data/historgram.png")

def test_hist(mocker):
    mocker.patch("src.preprocessing.plots.Plot.hist_observation", return_value=None)
    path = "tests/unit_tests/test_data"
    data = pd.read_csv("tests/unit_tests/test_data/sample.csv")
    p = Plot(data, path)
    assert os.path.isfile("tests/unit_tests/test_data/heatmap.png")
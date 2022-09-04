import unittest
import pytest
import pandas as pd
from unittest import mock
from sample import square, transform_square

@pytest.fixture()
def input_value():
    input =25
    return input

class TestSampleFeatures(unittest.TestCase):
    def test_square(self):
        x = 3
        result = square(x)
        self.assertEqual(result, 9)
    @mock.patch("sample.square", return_value=100)
    def test_transform_square(self, mock_square):
        x = 9
        df = transform_square(x)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn("sample_column", df.columns)
        self.assertEqual(df["sample_column"].values[0], 100)

def test_square():
    x = 10
    result = square(x)
    assert result == 100

def test_transform_square(mocker, input_value):
    mocker.patch("sample.square", 
    return_value=input_value)
    df = transform_square(2)
    assert isinstance(df, pd.DataFrame)
    assert "sample_column" in df.columns
    assert df["sample_column"].values[0] == 25
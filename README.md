
# Application of Pytest framework for Data Science Problems

Testing is an essential part of development of a product because it ensures that the application is as per the expectation and standards set by the customer. This repository demonstrates the testing of data sciene application using pytest.
## Built With

[![Python](https://img.shields.io/badge/python-3.9-blue)](https://www.python.org/)

[![Pytest](https://img.shields.io/badge/pytest-7.1.2-green)](https://docs.pytest.org/en/7.1.x/)




## Authors

- [@janesaldanha](https://www.github.com/Jazz4299)
- [@nilewilson](https://www.github.com/niwilso)


## Environment Setup

All Python packages necessary to run the code in this repository are listed in `CostOfLiving/requirements.txt`. To create a new Anaconda environment which includes these packages, enter the following command in your terminal:

```bash
conda create --name ds_unit_testing --file CostOfLiving/requirements.txt
conda activate ds_unit_testing
```
## Code Execution
To execute the data science problem execute the following command
```
cd CostOfLiving
python src/process.py
```

## Running unit tests

To run the unit tests, simply run pytest in the CostOfLiving directory.

```bash
cd CostOfLiving
pytest
```
## Project Tree
    ├── Cost of Living
      ├── data
            ├── costofliving.csv   
            ├── heatmap.png
            ├── histogram.png
            ├── comparision.png       
      ├── src
        ├── process.py
        ├── modelbuilding
          ├── model.py
          ├── __pycache__
        
        ├── preprocessing 
          ├── dataloading.py
          ├── plots.py
          ├── processing.py
          ├── __pycache__

      ├── tests
        ├── unit_tests
          ├── data
            ├── __pycache__
            ├── test_data
              ├── comparision.png
              ├── heatmap.png
              ├── historgram.png
              ├── sample.csv
            ├── __init__.py
            ├── test_data_loading.py
            ├── test_model.py
            ├── test_plots.py
            ├── test_preprocessing.py
      ├── requirements.txt
      ├── __init__.py
    ├── README.md

## Code Explanation
The data science problem selected for the demonstration is a regression problem which predicts the Cost of Living Index depending on the metrics like City, Rent Index, Groceries Index etc. The dataset which is used to train the model is attached in the ```CostOfLiving/data/costofliving.csv```.

The problem was split into modelbuilding and preprocessing. The former involved splitting the data, training and prediciting the model and the latter took care of loading the data in csv, exploratory data analysis, storing the png files and processing like removing null values, encoding etc. 
Let's begin with unit testing of the `preprocessing/dataloading.py`
There are two possible test cases for the function `load_data`

    1. Path passed as the input is correct and the output returned was a data frame. The code snippet for the test case is as follows:
    ```
    def test_load_data():
        path = "tests/unit_tests/test_data/sample.csv"
        di = DataIngestion()
        df = di.load_data(path)
        assert isinstance(df, pd.DataFrame)
    ```
    2.  Path passed was incorrect. The following snippet shows how to deal with functions that throw an exception. pytest.mark.parametrize() is used to pass different kind of sample input to the test case.
    ```
    @pytest.mark.parametrize("path,expected", [("path1", "The data file does not exist"),
    ("incorrect path", "The data file does not exist"), ("xyz.abc", "The data file does not exist")])
    def test_load_data_error(path, expected):
        with pytest.raises(FileNotFoundError) as F:
            df = DataIngestion().load_data(path)
            assert F.message == expected
    ```

In order to test the functions that store or save files os.path.isfile() could be used in assert as shown in the example below
```
def test_hist_observation(mocker):
    mocker.patch("src.preprocessing.plots.Plot.heatmap", return_value=None)
    path = "tests/unit_tests/test_data"
    data = pd.read_csv("tests/unit_tests/test_data/sample.csv")
    p = Plot(data, path)
    assert os.path.isfile("tests/unit_tests/test_data/historgram.png")
```

One important concept to keep in mind while writing unit test cases is mocking.
Mocking removes all the dependencies in the function and replace it with the implementation
or input that can be controlled. Example of mocking is shown below:
```
def test_split(mocker):
    mocker.patch("src.modelbuilding.model.ModelBuilding.train", return_value=None)
    mocker.patch("src.modelbuilding.model.ModelBuilding.predict", return_value=None)
    df = pd.read_csv("tests/unit_tests/test_data/sample.csv")
    class plot:
        def __init__(self, df, path):
            print("mock init")
        def hist_observation():
            print("mock hist")
        def heatmap():
            print("mock heatmap- no saving")
    mocker.patch.object(M, "Plot", plot)
    df["Country"] = ["USA"] * len(df)
    df["City"] = ["New York City"] * len(df)
    m = ModelBuilding(df, path="test_data")
    assert isinstance(m.X_train, pd.DataFrame)
    assert isinstance(m.X_test, pd.DataFrame)
    assert isinstance(m.y_train, pd.Series)
    assert isinstance(m.y_test, pd.Series)
```
mocker.patch() is used to mock the method called by the tested method which in this case is split. 
You might also notice that a class plot is defined with in the test function.

This is normally used to mock an import library or a class. We have used mocker.patch.object() function
where the first variable is the file which has the library, second variable is the import library and third 
is the class to be mocked in it.



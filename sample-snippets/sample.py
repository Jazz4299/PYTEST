import pandas as pd
def square(x):
    """
    Function that returns the
    square of the number passed
    """
    return x**2

def transform_square(x):
    """
    Function that adds a new column
    based on the square of the number
    passed
    """
    df = pd.read_csv("sample-snippets/data/feature_score_sort.csv")
    df['sample_column'] = square(x)
    return df
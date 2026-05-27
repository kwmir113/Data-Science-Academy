# Data-Science-Academy
# Code snippet 2
# Importing the Texas schools dataset
import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/nvamsimohan/DallasDSA/refs/heads/main/2023%20Texas%20High%20Schools%20Scores.csv')
# Code snippet 3
# Importing AutoGluon TabularPredictor for Regression
from autogluon.tabular import TabularPredictor
# Code snippet 4
# Displaying the dataset columns
data.columns

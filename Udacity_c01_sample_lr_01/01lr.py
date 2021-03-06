# Add import statements
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# Assign the dataframe to this variable.
# Load the data
bmi_life_data = pd.read_csv('bmi_and_life_expectancy.csv')


# Make and fit the linear regression model
# Fit the model and Assign it to bmi_life_model
bmi_life_model = LinearRegression()
bmi_life_model.fit(bmi_life_data[['BMI']].values, bmi_life_data[['Life expectancy']].values)

# Mak a prediction using the model
# Predict life expectancy for a BMI value of 21.07931
laos_life_exp = bmi_life_model.predict(21.07931)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Read the Excel file
# Make sure to use the correct path for your system
file_path = r'C:\Users\Owner\OneDrive\Data\Whitewater\Spring 2024\ITSCM 180\MovieFranchises.xlsx'
df = pd.read_excel(file_path)  # Reading the Excel file into a pandas DataFrame

# Histogram of Budget
budgets = df['Budget'].dropna()  # Assuming 'Budget' is the header for the budget column
bin_width = 50_000_000  # Each bin size is $50 million
bin_range = np.arange(0, budgets.max() + bin_width, bin_width)  # Bins from 0 to max budget in increments of $50 million
plt.figure(figsize=(10, 6))  # Set the size of the figure
plt.hist(budgets, bins=bin_range, color='skyblue', edgecolor='black')  # Plotting the histogram
plt.title('Histogram of Movie Budgets')  # Adding a title
plt.xlabel('Budget ($50 million bins)')  # X-axis label
plt.ylabel('Frequency')  # Y-axis label
plt.xticks(bin_range)  # Setting the x-ticks to match the bin range for clarity
plt.show()  # Display the histogram

# Linear Regression between Budget and Lifetime Gross
budget = df['Budget'].values  # Independent variable, assuming 'Budget' is the header
lifetime_gross = df['Lifetime Gross'].values  # Dependent variable, assuming 'Lifetime Gross' is the header
slope, intercept, r_value, p_value, std_err = linregress(budget, lifetime_gross)  # Performing linear regression
plt.figure(figsize=(10, 6))  # Set the size of the figure
plt.scatter(budget, lifetime_gross, color='blue', label='Data Points')  # Plotting the data points
regression_line = slope * budget + intercept  # Calculating the regression line
plt.plot(budget, regression_line, color='red', label='Regression Line')  # Plotting the regression line
plt.title('Linear Regression of Lifetime Gross on Budget')  # Adding a title
plt.xlabel('Budget ($)')  # X-axis label
plt.ylabel('Lifetime Gross ($)')  # Y-axis label
plt.legend()  # Adding a legend to distinguish data points from the regression line
plt.text(max(budget) * 0.5, max(lifetime_gross), f'R-squared = {r_value**2:.2f}', fontsize=12)  # Displaying the R-squared value
plt.show()  # Display the scatter plot with regression line

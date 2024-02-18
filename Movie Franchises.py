# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Step 1: Read the Excel file
# Define the path to the Excel file. Ensure this path is correct for your environment.
file_path = r'C:\Users\Owner\OneDrive\Data\Whitewater\Spring 2024\ITSCM 180\MovieFranchises.xlsx'

# Use pandas to read the Excel file. The result is stored in a DataFrame, which is a 2-dimensional labeled data structure.
df = pd.read_excel(file_path)

# Step 2: Create a histogram of movie budgets
# Access the 'Budget' column from the DataFrame. Assume 'Budget' is the header for Column H.
budgets = df['Budget'].dropna()  # Remove any NaN values to avoid errors during plotting.

# Define the bin width for the histogram and calculate the bin range.
bin_width = 50_000_000  # Each bin represents $50 million.
bin_range = np.arange(0, budgets.max() + bin_width, bin_width)  # Create bins from 0 to the maximum budget.

# Plot the histogram using matplotlib.
plt.figure(figsize=(10, 6))  # Set the figure size for better readability.
plt.hist(budgets, bins=bin_range, color='skyblue', edgecolor='black')  # Plot the histogram with specified bins and colors.
plt.title('Histogram of Movie Budgets')  # Add a title to the histogram.
plt.xlabel('Budget ($50 million bins)')  # Label the x-axis.
plt.ylabel('Frequency')  # Label the y-axis.
plt.xticks(bin_range)  # Set the x-axis ticks to match the bin range for clarity.
plt.show()  # Display the histogram.

# Step 3: Perform linear regression between Budget and Lifetime Gross
# Access the 'Budget' and 'Lifetime Gross' columns as independent and dependent variables, respectively.
# Assume 'Lifetime Gross' is the header for Column C.
budget = df['Budget'].values  # Independent variable.
lifetime_gross = df['Lifetime Gross'].values  # Dependent variable.

# Use scipy's linregress function to perform linear regression.
slope, intercept, r_value, _, _ = linregress(budget, lifetime_gross)

# Calculate the regression line values.
regression_line = slope * budget + intercept

# Plot the scatter plot and regression line using matplotlib.
plt.figure(figsize=(10, 6))  # Set the figure size.
plt.scatter(budget, lifetime_gross, color='blue', label='Data Points')  # Plot the data points in blue.
plt.plot(budget, regression_line, color='green', label='Regression Line')  # Plot the regression line in red.
plt.title('Linear Regression of Lifetime Gross on Budget')  # Add a title.
plt.xlabel('Budget ($)')  # Label the x-axis.
plt.ylabel('Lifetime Gross ($)')  # Label the y-axis.
plt.legend()  # Add a legend to distinguish between data points and the regression line.
plt.text(max(budget) * 0.5, max(lifetime_gross), f'R-squared = {r_value**2:.2f}', fontsize=12)  # Display the R-squared value on the plot.
plt.show()  # Display the scatter plot with regression line.

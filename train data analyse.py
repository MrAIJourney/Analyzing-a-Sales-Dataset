import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

train_sales_file = pd.read_csv('train.csv')

# check the first 5 rows
# print(train_sales_file.head())

# check if there is a null row in data
# print(train_sales_file.isnull().sum())

# get all columns
# print(train_sales_file.columns)

#summary statistics for sales based on sales
category_sales = train_sales_file.groupby('Category')['Sales'].sum()
# print(train_sales_file.groupby('Category')['Sales'].describe())

# Sort file data
data_sorted_by_sales = train_sales_file.sort_values(by='Sales', ascending=False)
# print(data_sorted_by_sales.head(10))

# Showing data on a plot
# category_sales.plot(kind='bar', title='Total sales by each category')
# plt.xlabel('Category')
# plt.ylabel('Sales')
# plt.show()

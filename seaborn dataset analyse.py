import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(sns.get_dataset_names())
tips_dataset = sns.load_dataset('tips')
titanic_dataset = sns.load_dataset('titanic')
print(titanic_dataset)

# ***** Showing the tips based on total bill colered based on day of order and size of each circle based of size of meal
# sns.scatterplot(x='tip', y='total_bill',data=tips_dataset, hue='day', size='size')
# plt.show()

# ****** histogram plot using tip column, draw line, use 15 bins in chart
# sns.histplot(tips_dataset['tip'], kde=True, bins=15)
# plt.show()

# ****** barplot showing amount of tips based on time and comparing two gender
# sns.barplot(x='time', y= 'tip', data= tips_dataset, hue='sex')
# plt.show()

# ***** Boxplot: showing amount of bills based on 
# sns.boxplot(x='day', y='tip', data=tips_dataset, hue='sex')
# plt.show()

# ***** JointPlot: combination of scatterplot and distributionPlot, you can chage type of plot in kind section
# sns.jointplot(x='tip', y='total_bill', data=tips_dataset, kind='scatter')
# plt.show()

# ***** Correlation in titanic dataset
print(titanic_dataset.corr(numeric_only=True))
sns.heatmap(titanic_dataset.corr(numeric_only=True), annot= True, cmap='coolwarm')
plt.show()
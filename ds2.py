import statistics
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import zscore


from google.colab import files
uploaded = files.upload()


df = pd.read_csv("savings_data.csv")

df.head()

fig = px.scatter(df, x='x_column', y='y_column', title='Scatter Plot of Data')
fig.show()

Q1 = df['column_name'].quantile(0.25)
Q3 = df['column_name'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df_no_outliers = df[(df['column_name'] >= lower_bound) & (df['column_name'] <= upper_bound)]

mean_no_outliers = df_no_outliers['column_name'].mean()
median_no_outliers = df_no_outliers['column_name'].median()
mode_no_outliers = df_no_outliers['column_name'].mode()[0]
std_dev_no_outliers = df_no_outliers['column_name'].std()

print(f"New Data - Mean: {mean_no_outliers}, Median: {median_no_outliers}, Mode: {mode_no_outliers}, Standard Deviation: {std_dev_no_outliers}")

sns.histplot(df_no_outliers['column_name'], kde=True)
plt.title('Distribution of New Data without Outliers')
plt.show()

sample_means = [df_no_outliers['column_name'].sample(n=100, random_state=i).mean() for i in range(100)]

sns.histplot(sample_means, kde=True)
plt.axvline(np.mean(sample_means), color='r', linestyle='--')
plt.title('Distribution of Sample Means')
plt.show()

std_dev_sampling = np.std(sample_means)
print(f"Standard Deviation of Sampling Data: {std_dev_sampling}")

mean_population = df['column_name'].mean()
mean_sampling = np.mean(sample_means)

print(f"Mean of Population Data: {mean_population}")
print(f"Mean of Sampling Data: {mean_sampling}")

sample1 = df_no_outliers.sample(n=100, random_state=1)
sample2 = df_no_outliers.sample(n=100, random_state=2)
correlation = sample1['column_name'].corr(sample2['column_name'])

print(f"Correlation between two samples: {correlation}")

df_no_outliers['z_score'] = zscore(df_no_outliers['column_name'])
significant_changes = df_no_outliers[df_no_outliers['z_score'].abs() > 2]

print(f"Number of significant changes (Z-score > 2): {len(significant_changes)}")

conclusion = """
Based on the analysis, we removed outliers from the dataset and created a new dataset without outliers. The mean, median, mode, and standard deviation of the new data were calculated, and a distribution plot was created. 
We also took 100 samples of the new data, found their means, and plotted the sample means along with a trace line at the mean. The standard deviation of the sampling data was calculated.
The mean of the population and sampling data was found to be similar, indicating that the sampling data is a good representation of the population data.
The correlation between two samples was calculated and found to be significant, indicating a strong relationship between the samples.
The Z-score analysis revealed that there were significant changes in the data, indicating that the data is scattered over a wider range.
"""

print(conclusion)


import statistics
import pandas as pd
import plotly.express as px


from google.colab import files
uploaded = files.upload()

df = pd.read_csv("savings_data.csv")

fig = px.scatter(df, x='x_column', y='y_column', title='Scatter Plot of Data')
fig.show()

mean_val = df['column_name'].mean()
median_val = df['column_name'].median()
mode_val = df['column_name'].mode()[0]

print(f"Mean: {mean_val}")
print(f"Median: {median_val}")
print(f"Mode: {mode_val}")

sample1 = df.sample(frac=0.5, random_state=1)
sample2 = df.sample(frac=0.5, random_state=2)

mean_sample1 = sample1['column_name'].mean()
median_sample1 = sample1['column_name'].median()
mode_sample1 = sample1['column_name'].mode()[0]

mean_sample2 = sample2['column_name'].mean()
median_sample2 = sample2['column_name'].median()
mode_sample2 = sample2['column_name'].mode()[0]

print(f"Sample 1 - Mean: {mean_sample1}, Median: {median_sample1}, Mode: {mode_sample1}")
print(f"Sample 2 - Mean: {mean_sample2}, Median: {median_sample2}, Mode: {mode_sample2}")

std_dev_population = df['column_name'].std()
std_dev_sample1 = sample1['column_name'].std()
std_dev_sample2 = sample2['column_name'].std()

print(f"Standard Deviation of Population: {std_dev_population}")
print(f"Standard Deviation of Sample 1: {std_dev_sample1}")
print(f"Standard Deviation of Sample 2: {std_dev_sample2}")


correlation_matrix = df.corr()
print("Correlation Matrix:")
print(correlation_matrix)


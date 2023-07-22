import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
# Load sample dataset
df = sns.load_dataset('Iris')

# 1. Scatter Plot
plt.scatter(df['sepal_length'],df['sepal_width'])
plt.xlabel('Sepal Length (cm)',c="blue")
plt.ylabel('Sepal Width (cm)',c="blue")
plt.title('Scatter Plot',c="red")
plt.show()

# 2. Line Plot
plt.plot(df['sepal_length'],c="green")
plt.plot(df['sepal_width'],c="orange")
plt.xlabel('X-axis', c="red")
plt.ylabel('Y-axis', c="red")
plt.title('Line Plot',c="blue")
plt.legend(["Sepal Length","Sepal Width"])
plt.show()

# 3. Bar Plot
sns.barplot(x='species', y='sepal_length', data=df)
plt.xlabel('Different types of Species', c="blue")
plt.ylabel('Sepal Length (cm)',c="blue")
plt.title('Bar Plot',c="red")
plt.show()

# 4. Histograms
plt.hist(df['sepal_length'])
plt.xlabel('Sepal Length',c="red")
plt.ylabel('Frequency',c="red")
plt.title('Histogram',c="green")
plt.show()

# 5. Box Plot
sns.boxplot(x='species', y='sepal_width', data=df)
plt.xlabel('Species',c="red")
plt.ylabel('Sepal Width',c="red")
plt.title('Box Plot',c="green")
plt.show()

# 6. Violin Plot
sns.violinplot(x='species', y='sepal_width', data=df)
plt.xlabel('Species',c="red")
plt.ylabel('Sepal Width',c="red")
plt.title('Violin Plot',c="green")
plt.show()

# 7. Swarm Plot
sns.swarmplot(x='species', y='sepal_length', data=df)
plt.xlabel('Species',c="blue")
plt.ylabel('Sepal length',c="blue")
plt.title('Box Plot',c="green")
plt.show()

# 8. Point Plot
sns.pointplot(x='sepal_width', y='sepal_length', data=df)
plt.xlabel('Sepal Width',c="green")
plt.ylabel('Sepal Length',c="green")
plt.title('Point Plot',c="red")
plt.show()

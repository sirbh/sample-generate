import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets
real = pd.read_csv('dataset.csv', sep=';')
synthetic = pd.read_csv('synthetic_dataset.csv', sep=';')

# Add source column for easy distinction
real['Source'] = 'Real'
synthetic['Source'] = 'Synthetic'

# Combine for plotting
combined = pd.concat([real, synthetic])

# Setup plot style
sns.set(style="whitegrid")

# Create a 2x3 grid of plots
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# Plot 1: Category1 distribution (bar plot)
sns.histplot(data=combined, x='Category1', hue='Source', multiple='dodge', discrete=True, stat='probability', ax=axes[0, 0])
axes[0, 0].set_title('Category1 Distribution')

# Plot 2: Value1 distribution (KDE)
sns.kdeplot(data=combined, x='Value1', hue='Source', fill=True, common_norm=False, ax=axes[0, 1])
axes[0, 1].set_title('Value1 KDE Distribution')

# Plot 3: Value2 distribution (KDE)
sns.kdeplot(data=combined, x='Value2', hue='Source', fill=True, common_norm=False, ax=axes[0, 2])
axes[0, 2].set_title('Value2 KDE Distribution')

# Plot 4: Value2 vs Category1 (boxplot)
sns.boxplot(data=combined, x='Category1', y='Value2', hue='Source', ax=axes[1, 0])
axes[1, 0].set_title('Value2 vs Category1')

# Plot 5: Value1 vs Category1 (boxplot)
sns.boxplot(data=combined, x='Category1', y='Value1', hue='Source', ax=axes[1, 1])
axes[1, 1].set_title('Value1 vs Category1')

# Plot 6: Value2 vs Value1 (scatter)
sns.scatterplot(data=combined, x='Value1', y='Value2', hue='Source', style='Source', ax=axes[1, 2])
axes[1, 2].set_title('Value2 vs Value1')

# Improve layout
plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Read the data
file_path = 'data.txt'
df = pd.read_csv(file_path)

# Remove the 'Total' column for visualization
if 'Total' in df.columns:
    df = df.drop(columns=['Total'])

# Set 'Type' as index
df.set_index('Type', inplace=True)

# Calculate 'No Response' for each location
df.loc['No Response'] = df.loc['Applications'] - df.loc['Rejections'] - df.loc['Did Not Accept'] - df.loc['Jobs']

# Reorder index to make 'No Response' the second bar
new_order = ['Applications', 'No Response', 'Rejections', 'Did Not Accept', 'Interview']
df = df.reindex(new_order)

# Add a 'Sum' column for each row and move it to the first position
df['Sum'] = df.sum(axis=1)
cols = list(df.columns)
cols.insert(0, cols.pop(cols.index('Sum')))
df = df[cols]

# Define colors for each category
colors = {
    'Applications': '#1f77b4',
    'No Response': '#ffd700',  # yellow
    'Rejections': '#d62728',
    'Did Not Accept': '#ff7f0e',
    'Interview': '#2ca02c'
}

# Plot grouped bar chart with custom colors
ax = df.T.plot(kind='bar', figsize=(10,6), color=[colors[t] for t in df.index])
plt.title('Job Application Data by Location')
plt.ylabel('Count')
plt.xlabel('Location')
plt.legend(title='Category')

# Add value labels to each bar
for container in ax.containers:
    ax.bar_label(container, label_type='edge', fontsize=10)

plt.tight_layout()
plt.savefig('plot.png')
print('Plot saved as plot.png')

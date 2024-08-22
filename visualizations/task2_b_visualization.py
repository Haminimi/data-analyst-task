""" import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset from the CSV file
df = pd.read_csv('shop_performance.csv')

# Initialize an empty list to store the top shops
top_shops = []

# Loop through each unique month in the dataset
for month in df['month'].unique():
    # Filter the dataframe for the current month and take the top 5 rows based on shop_clicks
    top_5 = df[df['month'] == month].nlargest(5, 'shop_clicks')
    
    # Append the shop_id to the list
    top_shops.extend(top_5[['shop_id']].values.tolist())

# Remove duplicates to get unique shops across all months
unique_top_shops = pd.DataFrame(top_shops, columns=['shop_id']).drop_duplicates()

# Merge this back with the original dataframe to get the data for these shops across all months
top_shop_trends = pd.merge(unique_top_shops, df, on='shop_id', how='left')

# Set up the plotting environment
plt.figure(figsize=(14, 8))

# Increase font sizes using rcParams
plt.rcParams.update({
    'font.size': 14,          # Global font size
    'axes.titleweight': 'bold',
    'axes.titlesize': 18,     # Title font size
    'axes.labelsize': 16,     # Axes labels font size
    'legend.fontsize': 12,    # Legend font size
    'xtick.labelsize': 12,    # X-axis tick label font size
    'ytick.labelsize': 12     # Y-axis tick label font size
})

# Plot each unique shop
for _, row in unique_top_shops.iterrows():
    subset = top_shop_trends[top_shop_trends['shop_id'] == row['shop_id']]
    sns.lineplot(data=subset, x='month', y='shop_clicks', label=f"Shop {row['shop_id']}")

# Add title and labels
plt.title('Trend of Shop Clicks for Most Successful Shops by Month', fontsize=14)
plt.xlabel('Month', fontsize=15, labelpad=15)
plt.ylabel('Shop Clicks', fontsize=15, labelpad=10)

# Adjust the legend to fit within the plot
plt.legend(title='Shop ID', bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.grid(True)
plt.tight_layout()  # Ensures the plot fits within the figure area

# Save the plot as an image (optional)
plt.savefig('shop_clicks_trend.png', dpi=300)

# Display the plot
plt.show() """

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load the dataset from the CSV file
df = pd.read_csv('shop_performance.csv')

# Convert the 'month' column to datetime format
df['month'] = pd.to_datetime(df['month'])

# Initialize an empty list to store the top shops
top_shops = []

# Loop through each unique month in the dataset
for month in df['month'].unique():
    # Filter the dataframe for the current month and take the top 5 rows based on shop_clicks
    top_5 = df[df['month'] == month].nlargest(5, 'shop_clicks')
    
    # Append the shop_id to the list
    top_shops.extend(top_5[['shop_id']].values.tolist())

# Remove duplicates to get unique shops across all months
unique_top_shops = pd.DataFrame(top_shops, columns=['shop_id']).drop_duplicates()

# Merge this back with the original dataframe to get the data for these shops across all months
top_shop_trends = pd.merge(unique_top_shops, df, on='shop_id', how='left')

# Set up the plotting environment
plt.figure(figsize=(14, 8))

# Increase font sizes using rcParams
plt.rcParams.update({
    'font.size': 14,          # Global font size
    'axes.titleweight': 'bold',
    'axes.titlesize': 18,     # Title font size
    'axes.labelsize': 16,     # Axes labels font size
    'legend.fontsize': 12,    # Legend font size
    'xtick.labelsize': 12,    # X-axis tick label font size
    'ytick.labelsize': 12     # Y-axis tick label font size
})

# Plot each unique shop
for _, row in unique_top_shops.iterrows():
    subset = top_shop_trends[top_shop_trends['shop_id'] == row['shop_id']]
    sns.lineplot(data=subset, x='month', y='shop_clicks', label=f"Shop {row['shop_id']}")

# Format the x-axis labels to show only 'YYYY-MM'
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# Add title and labels
plt.title('Trend of Shop Clicks for Most Successful Shops by Month', fontsize=14)
plt.xlabel('Month', fontsize=15, labelpad=15)
plt.ylabel('Shop Clicks', fontsize=15, labelpad=10)

# Adjust the legend to fit within the plot
plt.legend(title='Shop ID', bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.grid(True)
plt.tight_layout()  # Ensures the plot fits within the figure area

# Save the plot as an image (optional)
plt.savefig('shop_clicks_trend.png', dpi=300)

# Display the plot
plt.show()
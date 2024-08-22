import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.dates as mdates

# Load the dataset from the CSV file
df = pd.read_csv('market_share.csv')

# Replace NaN values in the subcategory_name column with 'Other'
df['subcategory_name'].fillna('Other', inplace=True)

# Convert the 'month' column to datetime format
df['month'] = pd.to_datetime(df['month'])

# Initialize an empty list to store the top categories and subcategories
top_categories = []

# Loop through each unique month in the dataset
for month in df['month'].unique():
    # Filter the dataframe for the current month and take the top 5 rows based on market_share_clicks
    top_5 = df[df['month'] == month].nlargest(5, 'market_share_clicks')
    
    # Append the category and subcategory combinations to the list
    top_categories.extend(top_5[['category_name', 'subcategory_name']].values.tolist())

# Remove duplicates to get unique category/subcategory combinations across all months
unique_top_categories = pd.DataFrame(top_categories, columns=['category_name', 'subcategory_name']).drop_duplicates()

# Merge this back with the original dataframe to get the data for these categories across all months
top_category_trends = pd.merge(unique_top_categories, df, on=['category_name', 'subcategory_name'], how='left')

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

# Plot each unique category/subcategory combination
for _, row in unique_top_categories.iterrows():
    subset = top_category_trends[(top_category_trends['category_name'] == row['category_name']) & 
                                 (top_category_trends['subcategory_name'] == row['subcategory_name'])]
    sns.lineplot(data=subset, x='month', y='market_share_clicks', label=f"{row['category_name']} / {row['subcategory_name']}")

# Format the x-axis labels to show only 'YYYY-MM'
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

# Add title and labels
plt.title('Trend of Market Share Clicks for Most Popular Categories/Subcategories (April - September 2020)', fontsize=14)
plt.xlabel('Month', fontsize=15, labelpad=15)
plt.ylabel('Market Share Clicks (%)', fontsize=15, labelpad=10)

# Adjust the legend to fit within the plot
plt.legend(title='Category / Subcategory', bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

plt.grid(True)
plt.tight_layout()  # Ensures the plot fits within the figure area

# Save the plot as an image (optional)
plt.savefig('market_share_trend.png', dpi=300)

# Display the plot
plt.show()
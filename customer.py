import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\HP8CG\OneDrive\Documents\PROJECTS\cognifz\Dataset.csv'
df = pd.read_csv(r'C:\Users\HP8CG\OneDrive\Documents\PROJECTS\cognifz\dataset.csv')

# Data Preparation
df['Cuisines'] = df['Cuisines'].astype(str)  # Convert to string if not already
df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')

# Handle missing values
df['Cuisines'] = df['Cuisines'].fillna('Unknown')
df['Aggregate rating'] = df['Aggregate rating'].fillna(df['Aggregate rating'].mean())

# Split 'Cuisines' into individual cuisines if there are multiple cuisines in one cell
df['Cuisines'] = df['Cuisines'].str.split(', ')

# Explode the 'Cuisines' column to have one cuisine per row
df_exploded = df.explode('Cuisines')

# Analyze the relationship between cuisine type and rating
cuisine_rating = df_exploded.groupby('Cuisines')['Aggregate rating'].agg(['mean', 'count']).reset_index()
cuisine_rating.columns = ['Cuisine', 'Average Rating', 'Number of Votes']

# Determine the most popular cuisines based on the number of votes
most_popular_cuisines = cuisine_rating.sort_values(by='Number of Votes', ascending=False)

# Determine if specific cuisines tend to receive higher ratings
high_rated_cuisines = cuisine_rating.sort_values(by='Average Rating', ascending=False)

# Visualization
plt.figure(figsize=(20, 16)) # Increased figure size for better readability

# Plot Average Rating by Cuisine
plt.subplot(1, 2, 1)
sns.barplot(x='Average Rating', y='Cuisine', data=high_rated_cuisines)
plt.title('Average Rating by Cuisine', fontsize=4)
plt.xlabel('Average Rating', fontsize=4)
plt.ylabel('Cuisine', fontsize=4)
plt.yticks(fontsize=4)  # Increased font size for y-axis labels

# Plot Number of Votes by Cuisine
plt.subplot(1, 2, 2)
sns.barplot(x='Number of Votes', y='Cuisine', data=most_popular_cuisines)
plt.title('Number of Votes by Cuisine', fontsize=4)
plt.xlabel('Number of Votes', fontsize=4)
plt.ylabel('Cuisine', fontsize=4)
plt.yticks(fontsize=4)  # Increased font size for y-axis labels

plt.tight_layout(pad=4)  # Adjusted padding to prevent overlap
plt.show()

# Display results
print("Most Popular Cuisines:")
print(most_popular_cuisines)

print("\nHigh Rated Cuisines:")
print(high_rated_cuisines)

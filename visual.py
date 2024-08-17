import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load and prepare the dataset
file_path = r'C:\Users\HP8CG\OneDrive\Documents\PROJECTS\cognifz\Dataset.csv'
df = pd.read_csv(file_path)

# Convert to numeric and handle missing values
df['Aggregate rating'] = pd.to_numeric(df['Aggregate rating'], errors='coerce')
df['Cuisines'] = df['Cuisines'].astype(str).fillna('Unknown')
df['City'] = df['City'].astype(str).fillna('Unknown')
df['Number of Votes'] = pd.to_numeric(df['Votes'], errors='coerce')

# Drop rows where 'Aggregate rating' or 'Number of Votes' is NaN
df = df.dropna(subset=['Aggregate rating', 'Number of Votes'])

# Average Ratings by Cuisine
avg_rating_by_cuisine = df.groupby('Cuisines')['Aggregate rating'].mean().reset_index()
avg_rating_by_cuisine = avg_rating_by_cuisine.sort_values(by='Aggregate rating', ascending=False).head(20)  # Get top 20

plt.figure(figsize=(40, 40))
ax = sns.barplot(x='Aggregate rating', y='Cuisines', data=avg_rating_by_cuisine)
plt.title('Average Rating by Cuisine (Top 20)', fontsize=12)
plt.xlabel('Average Rating', fontsize=14)
plt.ylabel('Cuisine', fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=10)
plt.show()

# Average Ratings by City (Bar Plot)
plt.figure(figsize=(12, 8))
avg_rating_by_city = df.groupby('City')['Aggregate rating'].mean().reset_index()
avg_rating_by_city = avg_rating_by_city.sort_values(by='Aggregate rating', ascending=False)
ax = sns.barplot(x='Aggregate rating', y='City', data=avg_rating_by_city)
plt.title('Average Rating by City', fontsize=8)
plt.xlabel('Average Rating', fontsize=8)
plt.ylabel('City', fontsize=4)
plt.xticks(fontsize=8)
plt.yticks(fontsize=4)
plt.show()

# Scatter Plot of Ratings vs. Number of Votes
plt.figure(figsize=(12, 6))
ax = sns.scatterplot(x='Number of Votes', y='Aggregate rating', data=df, alpha=0.6)
plt.title('Ratings vs. Number of Votes', fontsize=12)
plt.xlabel('Number of Votes', fontsize=10)
plt.ylabel('Rating', fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.show()

# Box Plot for Ratings by Table Booking Availability
plt.figure(figsize=(12, 6))
ax = sns.boxplot(x='Has Table booking', y='Aggregate rating', data=df)
plt.title('Ratings by Table Booking Availability', fontsize=12)
plt.xlabel('Has Table Booking', fontsize=10)
plt.ylabel('Rating', fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.show()

# Box Plot for Ratings by Online Delivery Availability
plt.figure(figsize=(12, 6))
ax = sns.boxplot(x='Has Online delivery', y='Aggregate rating', data=df)
plt.title('Ratings by Online Delivery Availability', fontsize=12)
plt.xlabel('Has Online Delivery', fontsize=10)
plt.ylabel('Rating', fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.show()

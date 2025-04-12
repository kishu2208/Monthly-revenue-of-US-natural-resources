import pandas as pd

# Load the dataset
file_path = "C:\\Users\ASUS\Downloads\Kishan Dataset.csv"
df = pd.read_csv(file_path)

# Display the first few rows and the column names to understand the structure
print(df.head())
print(df.info())

import matplotlib.pyplot as plt

# Group by 'Mineral Lease Type' and sum the revenue
revenue_by_lease_type = df.groupby('Mineral Lease Type')['Revenue'].sum().sort_values(ascending=False)

# Plotting
plt.figure(figsize=(10, 6))
revenue_by_lease_type.plot(kind='bar', color='skyblue')
plt.title('Revenue by Mineral Lease Type')
plt.xlabel('Mineral Lease Type')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y')
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset
file_path = "C:\\Users\ASUS\Downloads\Kishan Dataset.csv"
df = pd.read_csv(file_path)
Revenue=df.groupby("Mineral Lease Type")['Revenue'].max()


# Aggregate revenue by state
state_revenue = df.groupby('State')['Revenue'].sum().sort_values(ascending=False)

# Plotting
plt.figure(figsize=(12, 6))
sns.barplot(x=state_revenue.index, y=state_revenue.values, palette="viridis")
plt.title('Total Revenue by State')
plt.xlabel('State')
plt.ylabel('Total Revenue (USD)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset
file_path = "C:\\Users\ASUS\Downloads\Kishan Dataset.csv"
df = pd.read_csv(file_path)
Revenue=df.groupby("Mineral Lease Type")['Revenue'].max()


# Aggregate revenue by state
import matplotlib.pyplot as plt
import seaborn as sns

# Drop missing states
state_revenue = df.dropna(subset=['State']).groupby('State')['Revenue'].sum().sort_values(ascending=False)

# Plot as a heatmap using seaborn (showing top 20 for clarity)
plt.figure(figsize=(10, 12))
sns.heatmap(state_revenue.head(20).to_frame(), annot=True, fmt=".0f", cmap="YlOrRd", linewidths=.5)
plt.title("Top 20 States by Total Revenue")
plt.xlabel("Revenue")
plt.ylabel("State")
plt.tight_layout()
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset
file_path = "C:\\Users\ASUS\Downloads\Kishan Dataset.csv"
df = pd.read_csv(file_path)
Revenue=df.groupby("Mineral Lease Type")['Revenue'].max()




# Filter for entries where Mineral Lease Type is related to Coal
coal_data = df[(df['Mineral Lease Type'].str.contains("Coal", case=False, na=False)) &
               (df['Revenue'].notna()) &
               (df['State'].notna())]

# Group by country/state and sum revenue
revenue_by_state = coal_data.groupby('State')['Revenue'].sum().sort_values(ascending=False)

# Plot the top 10 states with highest coal revenue
plt.figure(figsize=(12, 6))
sns.barplot(x=revenue_by_state.head(10).values, y=revenue_by_state.head(10).index, palette='Blues_d')
plt.title("Top 10 States by Revenue from Coal (Mineral Lease Type)")
plt.xlabel("Total Revenue")
plt.ylabel("State")
plt.tight_layout()
plt.show()

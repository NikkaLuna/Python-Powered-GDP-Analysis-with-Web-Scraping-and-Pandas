import numpy as np
import pandas as pd

# URL of the webpage containing the GDP data
URL = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

# Extract tables from the webpage using Pandas. Retain table number 3 as the required DataFrame.
tables = pd.read_html(URL)
df = tables[3]

# Replace the column headers with column numbers for easier access
df.columns = range(df.shape[1])

# Retain only the columns with index 0 and 2 (name of the country and value of GDP quoted by IMF)
df = df[[0, 2]]

# Retain the rows with index 1 to 10, which correspond to the top 10 economies of the world.
df = df.iloc[1:11, :]

# Assign column names as "Country" and "GDP (Million USD)"
df.columns = ['Country', 'GDP (Million USD)']

# Convert the 'GDP (Million USD)' column to integer for consistent data types
df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int)

# Convert the GDP values from Million USD to Billion USD
df['GDP (Million USD)'] = df['GDP (Million USD)'] / 1000

# Use numpy's round() method to round the GDP values to 2 decimal places
df['GDP (Million USD)'] = np.round(df['GDP (Million USD)'], 2)

# Rename the column header from 'GDP (Million USD)' to 'GDP (Billion USD)'
df.rename(columns={'GDP (Million USD)': 'GDP (Billion USD)'}, inplace=True)

# Save the DataFrame to a CSV file named "Largest_economies.csv"
df.to_csv('Largest_economies.csv', index=False)

# Python-based Web-Scraping Data Processing for GDP Analysis

This project is a Python-based data extraction and processing script developed to extract, process, and analyze data on the top 10 largest economies in the world by GDP (in Billion USD), as reported by the International Monetary Fund (IMF). The script utilizes web scraping, data processing using Pandas, and mathematical operations with NumPy to achieve this.

## Project Scenario

I have been recruited by an international firm looking to expand its business in various countries worldwide. As a Junior Data Engineer, my task is to create a script that extracts the top 10 largest economies globally, processes the data, and saves it to a CSV file.

## Objectives

By completing this project, I will:

* Extract the required information from a website using web scraping.
* Load and process tabular data into a Pandas DataFrame.
* Use NumPy to manipulate the data contained within the DataFrame.
* Save the processed data to a CSV file.

## Tools and Libraries Used

The project makes use of the following Python libraries:

* Pandas: For managing and processing tabular data.
* NumPy: For performing mathematical operations and rounding values.
* Requests: For making HTTP requests to fetch the webpage (if required).

## Setup

### Prerequisites

Ensure you have the following Python libraries installed in your environment:

```bash
pip install pandas numpy requests
```

## Importing Required Libraries
It is recommended to import all required libraries in one place. Here’s the code snippet to do so:

```bash
import numpy as np
import pandas as pd
```

## 1: Extract GDP Data
Extract the required GDP data from the given URL using web scraping. The data is stored in the third table on the webpage.

```bash
URL = "[https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29](https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29)"
tables = pd.read_html(URL)
df = tables[3]
```

## 2: Modify GDP Data
Modify the GDP column of the DataFrame, converting values from Million USD to Billion USD. Use NumPy’s round() method to round the values to 2 decimal places. Modify the column header to "GDP (Billion USD)".

# Convert GDP from Million USD to Billion USD

```bash
df['GDP (Million USD)'] = df['GDP (Million USD)'] / 1000
df['GDP (Billion USD)'] = np.round(df['GDP (Million USD)'], 2)
```

# Retain only the required columns

```bash
df = df[['Country', 'GDP (Billion USD)']]
```

## 3: Save Data to CSV
Save the processed DataFrame to a CSV file named "Largest_economies.csv".

```bash
df.to_csv("Largest_economies.csv", index=False)
Use code with caution.
```

# Conclusion
This project demonstrates the process of extracting and processing GDP data for the top 10 largest economies. It highlights the use of Pandas for data management, NumPy for mathematical operations, and web scraping techniques to gather data from the web.
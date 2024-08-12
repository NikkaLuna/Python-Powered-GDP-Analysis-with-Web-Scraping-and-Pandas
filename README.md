# Python-Powered GDP Analysis with Web Scraping and Pandas

This project is a Python-based data extraction and processing script developed to extract, process, and analyze data on the top 10 largest economies in the world by GDP (in Billion USD), as reported by the International Monetary Fund (IMF). The script utilizes web scraping, data processing using Pandas, and mathematical operations with NumPy to achieve this.

## Objectives

* Extract the required information from a website using web scraping.
* Load and process tabular data into a Pandas DataFrame.
* Use NumPy to manipulate the data contained within the DataFrame.
* Save the processed data to a CSV file.

## Tools and Libraries Used

* Pandas: For managing and processing tabular data.
* NumPy: For performing mathematical operations and rounding values.
* Requests: For making HTTP requests to fetch the webpage (if required).

## Setup

### Prerequisites

Ensure you have the following Python libraries installed in your environment:

```bash
pip install pandas numpy requests
```

## Import Required Libraries
Here’s the code snippet to do so:

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

Convert GDP from Million USD to Billion USD:

```bash
df['GDP (Million USD)'] = df['GDP (Million USD)'] / 1000
df['GDP (Billion USD)'] = np.round(df['GDP (Million USD)'], 2)
```

Retain only the required columns:

```bash
df = df[['Country', 'GDP (Billion USD)']]
```

## 3: Save Data to CSV
Save the processed DataFrame to a CSV file named "Largest_economies.csv".

```bash
df.to_csv("Largest_economies.csv", index=False)
Use code with caution.
```

## Challenges and Solutions

### SSL Certificate Verification Issue

**Challenge:**  
While running the script on macOS with Python 3.12.1, an SSL certificate verification error was encountered. This error was due to an outdated or missing SSL certificate chain, causing the script to fail when attempting to access HTTPS resources.

**Solution:**  
To resolve this issue, I needed to update the SSL certificate manually. The following command was executed in the terminal to update the SSL certificates for Python 3.12:

```bash
/Applications/Python\ 3.12/Install\ Certificates.command
```

After updating the certificates, the script was able to access the required web resources without encountering SSL errors.

# Conclusion
This project demonstrates the process of extracting and processing GDP data for the top 10 largest economies. It highlights the use of Pandas for data management, NumPy for mathematical operations, and web scraping techniques to gather data from the web.

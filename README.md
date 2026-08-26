# Retail-sales
# RETAIL SALES ANALYZER

## 1. Introduction

Retail Sales Analyzer is a Python-based data analysis project developed to analyze and understand retail sales data. The project reads sales information from a CSV file, cleans and processes the data, calculates important sales metrics, filters data based on categories, generates a summary report, and visualizes the sales information using different charts.

The main purpose of this project is to make retail sales analysis simple, efficient, and understandable. Instead of performing calculations manually, the program automatically processes the data and provides useful information such as total sales, average sales, total quantity sold, the most popular product, and the best-performing category.

The project uses important Python libraries such as Pandas, NumPy, Matplotlib, and Seaborn. It also uses the built-in OS module for checking the existence and format of the input file.

---

# 2. Objectives of the Project

The main objectives of the Retail Sales Analyzer are:

1. To load retail sales data from a CSV file.
2. To validate the input file.
3. To clean and preprocess the sales data.
4. To handle missing and invalid values.
5. To calculate total sales and average sales.
6. To calculate the total quantity of products sold.
7. To identify the most popular product.
8. To identify the best-performing category.
9. To filter sales data according to the selected category.
10. To generate a summary sales report.
11. To visualize sales data using different charts.
12. To understand relationships between numerical variables using correlation analysis.

---

# 3. Technologies Used

The following technologies and libraries are used in this project:

| Technology / Library | Purpose                        |
| -------------------- | ------------------------------ |
| Python               | Main programming language      |
| Pandas               | Data manipulation and analysis |
| NumPy                | Numerical calculations         |
| Matplotlib           | Creating charts and graphs     |
| Seaborn              | Statistical data visualization |
| OS                   | File and path operations       |
| CSV                  | Data storage format            |

---

# 4. Modules and Packages Used

## 4.1 Pandas

```python
import pandas as pd
```

Pandas is a powerful Python library used for data manipulation and data analysis.

In this project, Pandas is used to:

* Read the CSV file.
* Create and manage the DataFrame.
* Clean the data.
* Handle missing values.
* Remove duplicate records.
* Group data.
* Filter data.
* Calculate sums and averages.

Example:

```python
self.df = pd.read_csv(file_path)
```

The `read_csv()` function reads the CSV file and stores the data in a Pandas DataFrame.

---

## 4.2 NumPy

```python
import numpy as np
```

NumPy is a Python library used for numerical and mathematical operations.

In this project, NumPy is used to convert the Total Sales column into an array and perform numerical calculations.

Example:

```python
sales = np.array(self.df["Total Sales"])
```

The following functions are used:

```python
sales.sum()
sales.mean()
```

`sum()` calculates the total sales, while `mean()` calculates the average sales.

---

## 4.3 Matplotlib

```python
import matplotlib.pyplot as plt
```

Matplotlib is a Python library used for creating graphs and charts.

In this project, Matplotlib is used to create:

* Bar Chart
* Line Chart
* Pie Chart

Example:

```python
product_sales.plot(kind="bar")
```

---

## 4.4 Seaborn

```python
import seaborn as sns
```

Seaborn is a Python data visualization library built on top of Matplotlib.

It is mainly used in this project to create a correlation heatmap.

Example:

```python
sns.heatmap(data, annot=True)
```

---

## 4.5 OS Module

```python
import os
```

The OS module is a built-in Python module used for interacting with the operating system.

In this project, it is used to check whether the entered file path exists.

Example:

```python
os.path.exists(file_path)
```

---

# 5. Object-Oriented Programming

This project uses the concept of Object-Oriented Programming (OOP).

A class named `RetailAnalyzer` is created:

```python
class RetailAnalyzer:
```

The class contains different methods for performing various operations on retail sales data.

The main methods are:

* `__init__()`
* `load_data()`
* `clean_data()`
* `calculate_metrics()`
* `filter_data()`
* `display_summary()`
* `charts()`

---

# 6. Class

A class is a blueprint for creating objects.

In this project:

```python
class RetailAnalyzer:
```

`RetailAnalyzer` is the class that contains all the functionality required for analyzing retail sales data.

---

# 7. Object

An object is an instance of a class.

The object is created using:

```python
analyzer = RetailAnalyzer()
```

The `analyzer` object is used to call the methods of the `RetailAnalyzer` class.

Example:

```python
analyzer.load_data(file_path)
analyzer.clean_data()
analyzer.calculate_metrics()
```

---

# 8. Constructor – **init**()

The `__init__()` method is called a constructor in Python.

It is automatically executed when an object is created.

Code:

```python
def __init__(self):
    self.df = None
```

Here, `self.df` is initialized with `None`.

Later, the CSV data is stored in `self.df`.

---

# 9. load_data() Function

The `load_data()` method is used to load the CSV file.

```python
def load_data(self, file_path):
```

First, the program checks whether the file exists:

```python
if not os.path.exists(file_path):
    print("File not found")
    return False
```

Then it checks whether the file is a CSV file:

```python
if not file_path.lower().endswith(".csv"):
    print("Please select a CSV file")
    return False
```

Finally, the CSV file is loaded using Pandas:

```python
self.df = pd.read_csv(file_path)
```

If the file is successfully loaded, the function returns:

```python
return True
```

---

# 10. clean_data() Function

The `clean_data()` method is used to clean and prepare the data for analysis.

## Date Conversion

```python
self.df["Date"] = pd.to_datetime(self.df["Date"])
```

This converts the Date column into a proper datetime format.

## Price Conversion

```python
self.df["Price"] = pd.to_numeric(
    self.df["Price"], errors="coerce"
)
```

This converts the Price column into numeric values.

## Quantity Conversion

```python
self.df["Quantity Sold"] = pd.to_numeric(
    self.df["Quantity Sold"], errors="coerce"
)
```

This converts the Quantity Sold column into numeric values.

## Missing Values

Missing values in Price and Quantity Sold are replaced with zero:

```python
self.df["Price"] = self.df["Price"].fillna(0)
```

```python
self.df["Quantity Sold"] = self.df["Quantity Sold"].fillna(0)
```

## Calculate Total Sales

Total Sales is calculated using:

```python
self.df["Total Sales"] = (
    self.df["Price"] * self.df["Quantity Sold"]
)
```

The formula is:

**Total Sales = Price × Quantity Sold**

For example, if the price is ₹500 and the quantity sold is 4:

**Total Sales = 500 × 4 = ₹2000**

## Remove Duplicate Records

```python
self.df = self.df.drop_duplicates()
```

This removes duplicate rows from the DataFrame.

---

# 11. calculate_metrics() Function

The `calculate_metrics()` method calculates important sales metrics.

First, the Total Sales column is converted into a NumPy array:

```python
sales = np.array(self.df["Total Sales"])
```

## Total Sales

```python
sales.sum()
```

This calculates the total sales amount.

## Average Sales

```python
sales.mean()
```

This calculates the average sales value.

## Total Quantity

```python
self.df["Quantity Sold"].sum()
```

This calculates the total quantity of products sold.

---

# 12. GroupBy Function

The `groupby()` function is used to group data based on a particular column.

Example:

```python
self.df.groupby("Product")["Quantity Sold"].sum()
```

This groups the data according to Product and calculates the total quantity sold for each product.

For example:

| Product | Total Quantity |
| ------- | -------------: |
| Laptop  |              2 |
| Shirt   |              8 |
| Rice    |             25 |

---

# 13. idxmax() Function

The `idxmax()` function returns the index or label corresponding to the maximum value.

Example:

```python
product = (
    self.df.groupby("Product")["Quantity Sold"]
    .sum()
    .idxmax()
)
```

This identifies the product with the highest total quantity sold.

This product is displayed as the **Most Popular Product**.

---

# 14. filter_data() Function

The `filter_data()` method is used to filter the sales data according to a category entered by the user.

The available categories are displayed using:

```python
self.df["Category"].unique()
```

The user enters a category:

```python
category = input("Enter category: ").strip()
```

The data is then filtered according to the selected category.

The following methods are used:

### `astype(str)`

Converts the values into strings.

### `strip()`

Removes unnecessary spaces from the beginning and end of a string.

### `casefold()`

Allows case-insensitive comparison.

For example:

`Electronics`, `electronics`, and `ELECTRONICS` can be treated as the same category.

---

# 15. DataFrame Filtering

The following code filters the DataFrame:

```python
result = self.df[
    self.df["Category"].astype(str).str.strip().str.casefold()
    == category.casefold()
]
```

If matching data is found, it is displayed.

If no matching data is found:

```python
print("No data found")
```

---

# 16. display_summary() Function

The `display_summary()` method displays an overall sales report.

The report contains:

* Total Activities
* Total Sales
* Average Sales
* Total Quantity
* Best Product
* Best Category

Example output:

```text
========== SALES REPORT ==========

Total Activities: 12
Total Sales: 231200
Average Sales: 19266.67
Total Quantity: 54
Best Product: Laptop
Best Category: Electronics
```

---

# 17. Finding the Best Category

The following code identifies the category with the highest total sales:

```python
category = (
    self.df.groupby("Category")["Total Sales"]
    .sum()
    .idxmax()
)
```

The category having the highest total sales is displayed as the **Best Category**.

---

# 18. charts() Function

The `charts()` method is used for data visualization.

This method creates four different visualizations:

1. Bar Chart
2. Line Chart
3. Pie Chart
4. Correlation Heatmap

---

# 19. Bar Chart

The Bar Chart displays total sales for each product.

```python
product_sales.plot(kind="bar")
```

### Purpose

The Bar Chart makes it easy to compare the sales performance of different products.

* X-axis represents Products.
* Y-axis represents Total Sales.

---

# 20. Line Chart

The Line Chart displays the sales trend over different dates.

```python
daily_sales.plot(kind="line", marker="o")
```

### Purpose

It helps to understand whether sales are increasing, decreasing, or remaining stable over time.

---

# 21. Pie Chart

The Pie Chart represents sales distribution among different categories.

```python
plt.pie(
    category_sales,
    labels=category_sales.index,
    autopct="%1.1f%%"
)
```

### Purpose

It shows the percentage contribution of each category to total sales.

---

# 22. Correlation

Correlation measures the relationship between numerical variables.

The following code calculates correlation:

```python
data = self.df[
    ["Price", "Quantity Sold", "Total Sales"]
].corr()
```

Correlation values generally range from **-1 to +1**.

* `+1` = Strong positive relationship
* `0` = No linear relationship
* `-1` = Strong negative relationship

---

# 23. Heatmap

A heatmap is used to represent correlation values visually.

```python
sns.heatmap(data, annot=True)
```

The heatmap shows the relationship between:

* Price
* Quantity Sold
* Total Sales

The `annot=True` parameter displays the numerical correlation values inside the heatmap.

---

# 24. User Input

The program takes input from the user using the `input()` function.

Example:

```python
choice = input("\nEnter your choice: ")
```

The program provides four options:

```text
1. Analyze Sales
2. Filter Data
3. Show Summary
4. Show Charts
```

The user selects an option according to the required operation.

---

# 25. Conditional Statements

The project uses `if`, `elif`, and `else` statements to execute different operations based on the user's choice.

```python
if choice == "1":
    analyzer.calculate_metrics()

elif choice == "2":
    analyzer.filter_data()

elif choice == "3":
    analyzer.display_summary()

elif choice == "4":
    analyzer.charts()

else:
    print("Invalid choice")
```

If the user enters an invalid option, the program displays `"Invalid choice"`.

---

# 26. CSV File Structure

The CSV file used by this project contains the following columns:

| Column        | Description                       |
| ------------- | --------------------------------- |
| Date          | Date of the sale                  |
| Product       | Name of the product               |
| Category      | Category of the product           |
| Price         | Price of one product              |
| Quantity Sold | Number of products sold           |
| Total Sales   | Price multiplied by Quantity Sold |

Example:

```text
Date,Product,Category,Price,Quantity Sold,Total Sales
2026-01-01,Laptop,Electronics,50000,1,50000
2026-01-01,Shirt,Clothing,1200,3,3600
2026-01-02,Phone,Electronics,25000,2,50000
```

---

# 27. Python Concepts Used

The following Python concepts are used in this project:

### 1. Class

```python
class RetailAnalyzer:
```

### 2. Object

```python
analyzer = RetailAnalyzer()
```

### 3. Constructor

```python
def __init__(self):
```

### 4. Methods

```python
load_data()
clean_data()
calculate_metrics()
filter_data()
display_summary()
charts()
```

### 5. Conditional Statements

```python
if
elif
else
```

### 6. User Input

```python
input()
```

### 7. String Methods

```python
strip()
casefold()
lower()
endswith()
```

### 8. DataFrame

```python
self.df
```

### 9. Grouping

```python
groupby()
```

### 10. Aggregation

```python
sum()
mean()
```

### 11. Data Cleaning

```python
fillna()
drop_duplicates()
pd.to_numeric()
pd.to_datetime()
```

### 12. Data Visualization

```text
Bar Chart
Line Chart
Pie Chart
Heatmap
```

---

# 28. Important Pandas Functions Used

| Function            | Purpose                             |
| ------------------- | ----------------------------------- |
| `pd.read_csv()`     | Reads CSV data                      |
| `pd.to_datetime()`  | Converts data into datetime format  |
| `pd.to_numeric()`   | Converts values into numeric format |
| `fillna()`          | Fills missing values                |
| `drop_duplicates()` | Removes duplicate rows              |
| `groupby()`         | Groups data                         |
| `sum()`             | Calculates total                    |
| `mean()`            | Calculates average                  |
| `idxmax()`          | Finds maximum value's index         |
| `unique()`          | Finds unique values                 |
| `astype()`          | Changes data type                   |

---

# 29. Important NumPy Functions Used

| Function     | Purpose                        |
| ------------ | ------------------------------ |
| `np.array()` | Converts data into NumPy array |
| `sum()`      | Calculates total               |
| `mean()`     | Calculates average             |

---

# 30. Important Matplotlib Functions Used

| Function             | Purpose                     |
| -------------------- | --------------------------- |
| `plt.figure()`       | Creates a figure            |
| `plt.title()`        | Adds chart title            |
| `plt.xlabel()`       | Adds X-axis label           |
| `plt.ylabel()`       | Adds Y-axis label           |
| `plt.tight_layout()` | Adjusts chart layout        |
| `plt.show()`         | Displays the chart          |
| `plt.pie()`          | Creates a pie chart         |
| `plt.xticks()`       | Controls X-axis tick labels |

---

# 31. Important Seaborn Function Used

```python
sns.heatmap()
```

It is used to create the correlation heatmap.

---

# 32. Advantages of the Project

The major advantages of the Retail Sales Analyzer are:

1. It reduces manual calculations.
2. It provides quick sales analysis.
3. It can handle CSV-based sales data.
4. It helps identify the best-selling product.
5. It helps identify the best-performing category.
6. It provides useful summary information.
7. It supports category-based filtering.
8. It provides graphical visualization.
9. It makes sales trends easier to understand.
10. It helps in making better business decisions.

---

# 33. Applications of the Project

The Retail Sales Analyzer can be used in:

* Retail Shops
* Supermarkets
* Online Stores
* Small Businesses
* Inventory Management Systems
* Sales Management Systems
* Business Data Analysis
* Product Performance Analysis

---

# 34. Project Workflow

The complete workflow of the project is:

```text
Start
   ↓
Display Menu
   ↓
User Selects an Option
   ↓
Enter CSV File Path
   ↓
Check File Exists
   ↓
Check CSV Format
   ↓
Load CSV Data
   ↓
Clean Data
   ↓
Perform Selected Operation
   ↓
Calculate Metrics / Filter / Summary / Charts
   ↓
Display Result
   ↓
End
```

---


1.input image:<img width="667" height="930" alt="image" src="https://github.com/user-attachments/assets/fd39f24d-3267-4b49-a2ba-6d52046baf2a" />

2.output image:<img width="1533" height="1026" alt="output image" src="https://github.com/user-attachments/assets/23ed6991-672b-4187-a58b-22708dacf24e" />


1.structer image:<img width="1024" height="1536" alt="ChatGPT Image Aug 26, 2026, 10_45_17 AM" src="https://github.com/user-attachments/assets/167e4ebd-e22d-4f2f-acec-cfc807a3a595" />

2.csv image:<img width="1400" height="1765" alt="image1" src="https://github.com/user-attachments/assets/7ae81a91-d617-4b5f-96c9-9713ec525706" />

3.image 2:<img width="1697" height="716" alt="image2" src="https://github.com/user-attachments/assets/430ddfc0-499b-483b-bd38-ff035f842170" />

4.image4:<img width="700" height="391" alt="image3" src="https://github.com/user-attachments/assets/c232cad6-e3e8-41fe-8578-2470d771c66e" />

5.image5:<img width="800" height="533" alt="image4" src="https://github.com/user-attachments/assets/a7589f6b-8e38-4447-816e-00dc97a71783" />

6.image6:<img width="900" height="720" alt="image6" src="https://github.com/user-attachments/assets/e37c1b6f-6bd3-4818-816b-2a0bbc8b572c" />

7.image7:<img width="983" height="931" alt="image7" src="https://github.com/user-attachments/assets/f0729342-ee05-4562-9134-5e6924740009" />

3.video link:https://drive.google.com/file/d/1zl94jOZn5vVk_Tzr82yjWg7Ys5dAjY4z/view?usp=drive_link

# 35. Project Conclusion

The Retail Sales Analyzer is a Python-based data analysis project that demonstrates the practical use of Python, Pandas, NumPy, Matplotlib, Seaborn, and Object-Oriented Programming.

The project loads retail sales data from a CSV file and performs important data cleaning and analysis operations. It calculates total sales, average sales, total quantity sold, identifies the most popular product, and determines the best-performing category.

The project also provides data filtering and visualization features. Bar charts, line charts, pie charts, and correlation heatmaps help users understand sales information in a simple and visual manner.

Overall, this project provides practical knowledge of **Python programming, OOP, Pandas, NumPy, data cleaning, data filtering, grouping, aggregation, and data visualization**. It can be further improved by adding features such as monthly sales analysis, profit calculation, inventory tracking, user authentication, and an interactive dashboard.

---

# 36. Key Viva Points

For viva, the most important points to remember are:

**Pandas:** Used for data manipulation and analysis.

**NumPy:** Used for numerical calculations.

**Matplotlib:** Used for creating charts.

**Seaborn:** Used for statistical visualization and heatmaps.

**OS:** Used for file and path checking.

**Class:** `RetailAnalyzer`

**Object:** `analyzer`

**Constructor:** `__init__()`

**Data Structure:** Pandas DataFrame

**Input File:** CSV

**Main Columns:** Date, Product, Category, Price, Quantity Sold, Total Sales

**Formula:**

```text
Total Sales = Price × Quantity Sold
```

**Most Popular Product:** Product with the highest total quantity sold.

**Best Category:** Category with the highest total sales.

**GroupBy:** Used to group data according to a column.

**idxmax():** Used to find the label/index of the maximum value.

**fillna():** Used to handle missing values.

**drop_duplicates():** Used to remove duplicate rows.

**corr():** Used to calculate correlation.

**Heatmap:** Used to visualize correlation values.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


class RetailAnalyzer:

    def __init__(self):
        self.df = None

    def load_data(self, file_path):

        if not os.path.exists(file_path):
            print("File not found")
            return False

        if not file_path.lower().endswith(".csv"):
            print("Please select a CSV file")
            return False

        self.df = pd.read_csv(file_path)

        print("\nData loaded successfully!")
        return True

    def clean_data(self):

        self.df["Date"] = pd.to_datetime(
            self.df["Date"],
            errors="coerce"
        )

        self.df["Price"] = pd.to_numeric(
            self.df["Price"],
            errors="coerce"
        )

        self.df["Quantity Sold"] = pd.to_numeric(
            self.df["Quantity Sold"],
            errors="coerce"
        )

        self.df["Total Sales"] = pd.to_numeric(
            self.df["Total Sales"],
            errors="coerce"
        )

        self.df["Price"] = self.df["Price"].fillna(0)

        self.df["Quantity Sold"] = (
            self.df["Quantity Sold"].fillna(0)
        )

        # Calculate Total Sales again
        self.df["Total Sales"] = (
            self.df["Price"] *
            self.df["Quantity Sold"]
        )

        self.df = self.df.drop_duplicates()

    def calculate_metrics(self):

        sales = np.array(
            self.df["Total Sales"]
        )

        print("\n--- Sales Metrics ---")

        print("Total Sales:", sales.sum())

        print("Average Sales:", sales.mean())

        print(
            "Total Quantity:",
            self.df["Quantity Sold"].sum()
        )

        product = (
            self.df.groupby("Product")["Quantity Sold"]
            .sum()
            .idxmax()
        )

        print(
            "Most Popular Product:",
            product
        )

    def filter_data(self):

        print("\nAvailable Categories:")

        print(
            self.df["Category"].unique()
        )

        category = input(
            "Enter category: "
        ).strip()

        result = self.df[
            self.df["Category"]
            .astype(str)
            .str.strip()
            .str.casefold()
            == category.casefold()
        ]

        print("\n--- Filtered Data ---")

        if len(result) == 0:
            print("No data found")

        else:
            print(
                result.to_string(index=False)
            )

    def display_summary(self):

        product = (
            self.df.groupby("Product")["Quantity Sold"]
            .sum()
            .idxmax()
        )

        category = (
            self.df.groupby("Category")["Total Sales"]
            .sum()
            .idxmax()
        )

        print("\n========== SALES REPORT ==========")

        print(
            "Total Activities:",
            len(self.df)
        )

        print(
            "Total Sales:",
            self.df["Total Sales"].sum()
        )

        print(
            "Average Sales:",
            self.df["Total Sales"].mean()
        )

        print(
            "Total Quantity:",
            self.df["Quantity Sold"].sum()
        )

        print(
            "Best Product:",
            product
        )

        print(
            "Best Category:",
            category
        )

    def charts(self):

        product_sales = (
            self.df.groupby("Product")["Total Sales"]
            .sum()
        )

        plt.figure(figsize=(8, 5))

        product_sales.plot(kind="bar")

        plt.title("Sales by Product")
        plt.xlabel("Product")
        plt.ylabel("Total Sales")

        plt.tight_layout()

        plt.show()

        daily_sales = (
            self.df.groupby("Date")["Total Sales"]
            .sum()
        )

        plt.figure(figsize=(8, 5))

        daily_sales.plot(
            kind="line",
            marker="o"
        )

        plt.title("Sales Trend")
        plt.xlabel("Date")
        plt.ylabel("Total Sales")

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.show()

        category_sales = (
            self.df.groupby("Category")["Total Sales"]
            .sum()
        )

        plt.figure(figsize=(7, 7))

        plt.pie(
            category_sales,
            labels=category_sales.index,
            autopct="%1.1f%%"
        )

        plt.title("Sales by Category")

        plt.show()

        data = self.df[
            [
                "Price",
                "Quantity Sold",
                "Total Sales"
            ]
        ].corr()

        plt.figure(figsize=(7, 5))

        sns.heatmap(
            data,
            annot=True
        )

        plt.title("Sales Correlation")

        plt.tight_layout()

        plt.show()


# ==========================================
# MAIN PROGRAM
# ==========================================

print("====================================")
print("       RETAIL SALES ANALYZER")
print("====================================")

print("1. Analyze Sales")
print("2. Filter Data")
print("3. Show Summary")
print("4. Show Charts")

choice = input(
    "\nEnter your choice: "
)

file_path = input(
    "Enter CSV file path: "
)

analyzer = RetailAnalyzer()


if analyzer.load_data(file_path):

    analyzer.clean_data()

    print("\n--- Retail Sales Data ---")

    print(analyzer.df)

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
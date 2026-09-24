```python
import streamlit as st
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
            return False

        if not file_path.lower().endswith(".csv"):
            return False

        self.df = pd.read_csv(file_path)
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

        self.df["Total Sales"] = (
            self.df["Price"] *
            self.df["Quantity Sold"]
        )

        self.df = self.df.drop_duplicates()

    def calculate_metrics(self):

        sales = np.array(
            self.df["Total Sales"]
        )

        total_sales = sales.sum()
        average_sales = sales.mean()
        total_quantity = self.df["Quantity Sold"].sum()

        product = (
            self.df.groupby("Product")["Quantity Sold"]
            .sum()
            .idxmax()
        )

        return (
            total_sales,
            average_sales,
            total_quantity,
            product
        )

    def filter_data(self, category):

        result = self.df[
            self.df["Category"]
            .astype(str)
            .str.strip()
            .str.casefold()
            == category.casefold()
        ]

        return result

    def display_summary(self):

        product = (
            self.df.groupby("Product")["Quantity Sold"]
            .sum()
            .idxmax()
        )

        category = (
            self.df.groupby("Category")["Total Sales"]
```


import pandas as pd
#it lets your code work with folders and files and create filders automatically
import os

#Read WooCommerce CSV and understand that columns in csv are semi colon separated
website_df = pd.read_csv("ab_nov_dec_sales2025.csv", sep=";")

#Creates a folder called data/bronze
os.makedirs("data/bronze", exist_ok=True)

# Read raw WooCommerce export (bronze)
bronze_df = pd.read_csv(
    "ab_nov_dec_sales2025.csv", sep=";")

# Save bronze layer (raw, untouched)
bronze_df.to_csv(
    "data/bronze/ab_nov_dec_sales2025_raw.csv",
    index=False
)
print("Bronze dataset saved")


#Print first 5 rows
print(website_df.head())

#Checking column names
print("COLUMNS IN DATSET:")
print(website_df.columns)

# Rename product-related columns
website_df = website_df.rename(columns={
    "Item Name": "Product_Name",
    "Phone (Billing)": "Phone Number",
    "First Name (Billing)": "Customer Name",
    "City (Shipping)": "Customer City",
    "Order Shipping Amount": "Delivery Fee",
    "Total products": "Total Product Ordered",
    "Order Date": "Order Date"
})

#Check renamed columns
print("COLUMNS AFTER RENAME:")
print(website_df.columns)

# Convert order_date to real dates
website_df["Order Date"] = pd.to_datetime(website_df["Order Date"])

#Convert Order number to an object
website_df["Order Number"] = website_df["Order Number"].astype(str)


#Print data types
print("\nDATA TYPES:")
print(website_df.dtypes)

# Clean phone numbers to digits-only format
website_df["Phone Number"] = (
    website_df["Phone Number"]
    .astype(str)
    .str.replace(r"\D", "", regex=True)   # remove anything not a digit
    .str.replace(r"^27", "", regex=True)  # remove country code 27 if it starts the number
)

# Keep only reasonable phone lengths (9 or 10 digits)
website_df = website_df[
    website_df["Phone Number"].str.len().isin([9, 10])
]

#show the top 5 numbers 
print(website_df["Phone Number"].head())

#Creates a folder called data/silver
os.makedirs("data/silver", exist_ok=True)

#Save Cleaned Data to Silver Layer
website_df.to_csv(
    "data/silver/ab_nov_dec_sales2025_silver.csv",
    index=False
)

print("Silver dataset created successfully")

#Read the Silver dataset 
silver_df = pd.read_csv("data/silver/ab_nov_dec_sales2025_silver.csv")

#Preview Silver Dataset (First 5 Rows)
print("\nFIRST 5 ROWS OF SILVER DATASET:")
print(silver_df.head())


import pandas as pd

#Read WooCommerce CSV and understand that columns in csv are semi colon separated
website_df = pd.read_csv("NovDec_Sales_v2.csv", sep=";")


#Print first 5 rows
print(website_df.head())

#Checking column names
print("COLUMNS IN DATSET:")
print(website_df.columns)
# Rename product-related columns
website_df = website_df.rename(columns={
    "Item Name": "Product_Name",
    "Item #": "Quantity",
    "Phone (Billing)": "Phone Number",
    "First Name (Shipping)": "Customer Name",
    "City (Shipping)": "Customer City",
    "Order Shipping Amount": "Delivery Fee",
    "Item Cost": "Product Cost"
})

#Check renamed columns
print("COLUMNS AFTER RENAME:")
print(website_df.columns)

# Convert order_date to real dates
website_df["Order Date"] = pd.to_datetime(website_df["Order Date"])

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

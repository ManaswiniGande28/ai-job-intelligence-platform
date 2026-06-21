import pandas as pd
import sqlite3

# Read CSV
df = pd.read_csv("users.csv")

# Create database
conn = sqlite3.connect("users.db")

# Load data into table
df.to_sql(
    "users",
    conn,
    if_exists="replace",
    index=False
)

print("Data loaded successfully")

conn.close()
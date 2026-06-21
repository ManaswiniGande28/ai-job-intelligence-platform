import pandas as pd
import sqlite3

df = pd.read_csv("jobs.csv")

conn = sqlite3.connect("jobs.db")

df.to_sql(
    "jobs",
    conn,
    if_exists="replace",
    index=False
)

print("Jobs loaded successfully")

conn.close()
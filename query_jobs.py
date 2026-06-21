import sqlite3
import pandas as pd

conn = sqlite3.connect("jobs.db")

query = """
SELECT title,
       company,
       updated
FROM jobs
WHERE updated LIKE '2026-06-20%'
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()
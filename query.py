import sqlite3
import pandas as pd

conn = sqlite3.connect("users.db")

query = """
SELECT *
FROM users
WHERE id > 5
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()
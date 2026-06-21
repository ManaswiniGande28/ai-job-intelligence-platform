import sqlite3
import pandas as pd

conn = sqlite3.connect("jobs.db")

query = """
SELECT location,
       COUNT(*) AS total_jobs
FROM jobs
GROUP BY location
ORDER BY total_jobs DESC
LIMIT 10
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()
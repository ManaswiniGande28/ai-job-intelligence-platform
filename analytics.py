import sqlite3
import pandas as pd

conn = sqlite3.connect("jobs.db")

query = """
SELECT company,
       COUNT(*) AS total_jobs
FROM jobs
GROUP BY company
HAVING total_jobs > 1
ORDER BY total_jobs DESC
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()
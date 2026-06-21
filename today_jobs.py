import pandas as pd
from datetime import datetime

df = pd.read_csv("jobs.csv")

today = datetime.today().strftime("%Y-%m-%d")

today_jobs = df[
    df["updated"].str.startswith(today, na=False)
]

print(today_jobs)
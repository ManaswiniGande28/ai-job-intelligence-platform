import pandas as pd

df = pd.read_csv("jobs.csv")

skills = [
    "Python",
    "SQL",
    "AWS",
    "Azure",
    "GCP",
    "Snowflake",
    "Databricks",
    "Airflow",
    "Spark",
    "Kafka"
]

for skill in skills:
    count = df["snippet"].str.contains(
        skill,
        case=False,
        na=False
    ).sum()

    print(f"{skill}: {count}")
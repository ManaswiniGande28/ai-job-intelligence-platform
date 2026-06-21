my_skills = [
    "Python",
    "SQL",
    "AWS",
    "Azure",
    "GCP",
    "Snowflake",
    "Databricks",
    "Airflow"
]

job_skills = [
    "Python",
    "SQL",
    "AWS",
    "Databricks"
]

matched = set(my_skills) & set(job_skills)

score = (len(matched) / len(job_skills)) * 100

print("Matched Skills:", matched)
print("Match Score:", score)
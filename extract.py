import requests
import pandas as pd

api_key = "2221d351-a89f-43dd-bbcc-cdb86eb1f8ae"

url = f"https://jooble.org/api/{api_key}"

payload = {
    "keywords": "Data Engineer",
    "location": "United States"
}

response = requests.post(url, json=payload)

data = response.json()

records = []

for job in data["jobs"]:

   records.append({
    "title": job.get("title"),
    "company": job.get("company"),
    "location": job.get("location"),
    "salary": job.get("salary"),
    "updated": job.get("updated"),
    "snippet": job.get("snippet"),
    "link": job.get("link")

    })

df = pd.DataFrame(records)

print(df.head())

df.to_csv("jobs.csv", index=False)

print("Jobs saved successfully")
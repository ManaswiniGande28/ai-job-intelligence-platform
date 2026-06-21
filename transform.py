import pandas as pd

df = pd.read_csv("users.csv")

df["email_domain"] = df["email"].str.split("@").str[1]

print(df[["name", "email_domain"]])
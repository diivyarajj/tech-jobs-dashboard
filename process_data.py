import pandas as pd

# Kaggle dataset load karo (Row 0 is actual questions, Row 1+ is data)
df = pd.read_csv("uk_jobs.csv", skiprows=[1], low_memory=False)

# Relevant columns pick karo
# Q5 = Job Title, Q25 = Salary Range, Q3 = Country, Q7_Part_1 = Python
clean_df = df[["Q5", "Q25", "Q3", "Q7_Part_1"]].dropna().copy()

# Rename columns to user-friendly names
clean_df.columns = ["JobTitle", "Salary", "Location", "TechStack"]

# Blank values clean karo
clean_df = clean_df[
    (clean_df["JobTitle"] != "Other") & (clean_df["JobTitle"] != "Student")
]

# Top 100 rows save kar lo clean data.csv me
clean_df.head(100).to_csv("data.csv", index=False)
print(
    "Data successfully cleaned and saved to data.csv! Total rows:",
    len(clean_df.head(100)),
)
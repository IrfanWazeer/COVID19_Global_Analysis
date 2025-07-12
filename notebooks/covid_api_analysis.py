# covid_api_analysis.py
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# API endpoint
url = "https://disease.sh/v3/covid-19/countries"

# Get data from API
response = requests.get(url)
data = response.json()

# Convert to DataFrame
df = pd.json_normalize(data)

# Show top 5 rows
print(df.head())

# Save to CSV for backup
df.to_csv("../data/covid_country_data.csv", index=False)

# Set plot style
sns.set(style="whitegrid")

# Top 10 countries by total cases
top_10 = df.sort_values(by="cases", ascending=False).head(10)

# Plot
plt.figure(figsize=(12, 6))
sns.barplot(x="country", y="cases", data=top_10, palette="Reds_r")
plt.title("Top 10 Countries by COVID-19 Cases")
plt.ylabel("Total Cases")
plt.xlabel("Country")
plt.xticks(rotation=45)
plt.tight_layout()

# Save to file
plt.savefig("../visuals/top_10_countries_cases.png")


# Show the plot
plt.show()

# Select useful columns only for dashboard
cols = [
    "country", "cases", "todayCases", "deaths", "todayDeaths",
    "recovered", "todayRecovered", "active", "critical", "casesPerOneMillion"
]

df_dashboard = df[cols]

# Export cleaned data for Power BI or Excel
df_dashboard.to_csv("../data/covid_dashboard_cleaned.csv", index=False)

print("✅ Power BI export CSV saved successfully.")

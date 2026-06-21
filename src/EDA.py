import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter
import statsmodels.api as sm
import seaborn as sns 
from data_loader import load_covid_records, get_total_by_month, get_grouped_by_country_cases, get_grouped_by_country_deaths, get_grouped_by_country_and_pop, get_grouped_by_country_top_death_to_case

df = load_covid_records()

print(df.head(5))
print(df.tail(5))

print(df.columns)
print(df.shape)
print(df.dtypes)
print(df.isnull().sum())

print(df[[
    "cases",
    "deaths",
    "popData2019",
    "Cumulative_number_for_14_days_of_COVID-19_cases_per_100000"
]].describe())

print(df[["countriesAndTerritories", "continentExp"]].describe(include="object"))

print(df["continentExp"].value_counts())
print(df["countriesAndTerritories"].value_counts())


df_grouped_by_country_cases = get_grouped_by_country_cases(df)

df_grouped_by_country_deaths = get_grouped_by_country_deaths(df)

df_grouped_by_country_and_pop = get_grouped_by_country_and_pop(df)

df_grouped_by_country_top_death_to_case = (
    get_grouped_by_country_top_death_to_case(df)
)

df_total_by_month = get_total_by_month(df)

df_top_cases = df_grouped_by_country_cases.head(15)

df_top_deaths = df_grouped_by_country_deaths.head(15)

plt.figure(figsize=(6,4))
plt.bar(
    df_top_cases["countriesAndTerritories"],
    df_top_cases["cases"] / 1_000_000,
    label="Cases", color="blue"
)

plt.ylabel("Total (Millions)")
plt.title("Top 15 Countries - Total COVID Cases")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(6,4))
plt.bar(
    df_top_deaths["countriesAndTerritories"],
    df_top_deaths["deaths"] / 1000,
    label="deaths", color="red"
)
plt.ylabel('Total')
plt.title('Top 15 Countries in total COVID Deaths - Thousands')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(df_total_by_month.index, df_total_by_month["cases"], label="Cases")

plt.legend()
plt.title("Monthly COVID Cases")
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(10, 6))
plt.boxplot(df["cases"])

plt.title("Box Plot - Cases")
plt.show()


plt.figure(figsize=(10, 6))
sm.qqplot(df["cases"], line="45")

plt.title("QQ Plot - Cases")
plt.show()

df["cases_rolling"] = df["cases"].rolling(window=7).mean()

plt.figure(figsize=(10, 6))
plt.plot(df.index, df["cases"], alpha=0.4, label="Daily Cases")
plt.plot(df.index, df["cases_rolling"], color="red", label="7-day Avg")

plt.legend()
plt.title("Cases Trend with Rolling Average")
plt.xticks(rotation=45)
plt.show()


plt.figure(figsize=(8, 6))
plt.scatter(df["cases"], df["deaths"])

plt.title("Cases vs Deaths Correlation")
plt.xlabel("Cases")
plt.ylabel("Deaths")
plt.show()


plt.figure(figsize=(10, 6))
plt.plot(df.index, df["cases"], label="Cases", alpha=0.5)
plt.plot(df.index, df["deaths"], label="Deaths")

plt.title("Cases vs Deaths Trend")
plt.legend()
plt.show()

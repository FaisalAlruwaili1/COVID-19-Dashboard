import pandas as pd

def load_covid_records():
    data1 = pd.read_json("json")
    df1 = pd.json_normalize(data1["records"])

    data2 = pd.read_json("json_1")
    df2 = pd.json_normalize(data2["records"])

    df = pd.concat([df1, df2], axis=0)

    df["countriesAndTerritories"] = df["countriesAndTerritories"].replace(
    "United_States_of_America",
    "United_States"
    )

    df = df[(df["cases"] >= 0) & (df["deaths"] >= 0)]

    df = df.reset_index(drop=True)

    df["dateRep"] = pd.to_datetime(df["dateRep"], format="%d/%m/%Y")
    df = df.sort_values("dateRep")
    df = df.set_index("dateRep")
    return df

def load_vaccination_data():
    total_vaccinated = pd.read_csv(
        "number-of-people-who-completed-the-initial-covid-19-vaccination-protocol.csv"
    )

    total_vaccinated["Day"] = pd.to_datetime(total_vaccinated["Day"])
    total_vaccinated = total_vaccinated.sort_values("Day")
    total_vaccinated = total_vaccinated.set_index("Day")
    total_vaccinated.index.name = "Date"

    return total_vaccinated

def get_total_by_month(df):
    df = df

    df_total_by_month = (
        df[["cases", "deaths"]]
        .resample("ME")
        .sum()
    )

    return df_total_by_month

def get_grouped_by_country_cases(df):
    df = df

    df["countriesAndTerritories"] = df["countriesAndTerritories"].replace(
        "United_States_of_America",
        "United_States"
    )

    df_grouped_by_country_cases = (
        df.groupby(
            ["countriesAndTerritories", "countryterritoryCode"]
        )[["cases"]]
        .sum()
        .sort_values("cases", ascending=False)
        .reset_index()
    )

    return df_grouped_by_country_cases

def get_grouped_by_country_deaths(df):
    df = df

    df["countriesAndTerritories"] = df["countriesAndTerritories"].replace(
        "United_States_of_America",
        "United_States"
    )

    df_grouped_by_country_deaths = (
        df.groupby(
            ["countriesAndTerritories", "countryterritoryCode"]
        )[["deaths"]]
        .sum()
        .sort_values("deaths", ascending=False)
        .reset_index()
    )

    return df_grouped_by_country_deaths

def get_grouped_by_country_and_pop(df):
    
    df["popData2020"] = (
    df["popData2020"]
    .replace(0, pd.NA)
    .fillna(df["popData2019"])
)
    df.drop(columns={"popData2019"}, inplace=True)

    df_grouped = df.groupby(["countriesAndTerritories", "popData2020"])[["cases", "deaths"]].sum().reset_index()
    
    return df_grouped

def get_grouped_by_country_top_death_to_case(df):
    df = df

    df_grouped_by_country_top_death_to_case = (
        df.groupby(
            ["countriesAndTerritories"]
        )[["cases", "deaths"]]
        .sum()
        .reset_index()
    )

    df_grouped_by_country_top_death_to_case["death_to_case_ratio"] = (
        df_grouped_by_country_top_death_to_case["deaths"]
        / df_grouped_by_country_top_death_to_case["cases"]
    ) * 1000

    df_grouped_by_country_top_death_to_case = (
        df_grouped_by_country_top_death_to_case
        .sort_values("death_to_case_ratio", ascending=False)
    )

    return df_grouped_by_country_top_death_to_case.head(15)

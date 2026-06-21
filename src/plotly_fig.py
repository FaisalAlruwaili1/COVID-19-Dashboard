import pandas as pd 
import plotly.express as px 
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px 

def fig1(df_grouped_by_country_cases):
    fig = px.choropleth(
        df_grouped_by_country_cases,
        locations="countryterritoryCode",
        locationmode="ISO-3",
        color="cases",
        hover_name="countriesAndTerritories",
        color_continuous_scale=px.colors.sequential.RdBu,
        title="Total Cases per Country",
        template="plotly_dark"
    )

    fig.update_layout(
        title_x=0.5,
        title_font=dict(color="white", size=30)
    )

    return fig


def fig2(df_grouped_by_country_and_pop):
    fig = px.scatter(
        df_grouped_by_country_and_pop,
        x="popData2020",
        y="cases",
        size="deaths",
        color="countriesAndTerritories",
        color_discrete_sequence=px.colors.qualitative.Bold,
        size_max=60,
        title="COVID-19 Cases, Deaths, and Population by Country",
        template="plotly_dark"
    )

    fig.update_layout(
        title_font=dict(color="white", size=30)
    )

    return fig


def fig_bar(df_grouped_by_country_top_death_to_case):
    fig = px.bar(
        df_grouped_by_country_top_death_to_case,
        x="countriesAndTerritories",
        y="death_to_case_ratio",
        color="countriesAndTerritories",
        color_discrete_sequence=px.colors.qualitative.Prism,
        title="Top 15 Countries: Deaths per 1000 Cases",
        template="plotly_dark"
    )

    fig.update_layout(
        title_font=dict(color="white", size=30)
    )

    return fig


def fig_cases(df_total_by_month):
    fig = px.line(
        df_total_by_month,
        x=df_total_by_month.index,
        y="cases",
        title="Total Cases Worldwide by Month",
        color_discrete_sequence=[px.colors.qualitative.Bold[3]],
        template="plotly_dark"
    )

    fig.update_layout(
        title_font=dict(color="white", size=23)
    )

    fig.update_xaxes(
        type="date",
        dtick="M3",
        tickformat="%b %Y",
        tickangle=40
    )

    return fig


def fig_deaths(df_total_by_month):
    fig = px.line(
        df_total_by_month,
        x=df_total_by_month.index,
        y="deaths",
        title="Total Deaths Worldwide by Month",
        color_discrete_sequence=[px.colors.qualitative.Prism[7]],
        template="plotly_dark"
    )

    fig.update_layout(
        title_font=dict(color="white", size=23)
    )

    fig.update_xaxes(
        type="date",
        dtick="M3",
        tickformat="%b %Y",
        tickangle=40
    )

    return fig


def fig_vac(df, total_vaccinated):
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(
            x=df.index,
            y=df["cases"],
            name="Daily Cases",
            mode="lines",
            line=dict(
                color=px.colors.qualitative.Bold[7],
                width=2
            )
        ),
        secondary_y=False
    )

    fig.add_trace(
        go.Scatter(
            x=total_vaccinated.index,
            y=total_vaccinated["People fully vaccinated (cumulative)"],
            name="Fully Vaccinated (Cumulative)",
            mode="lines",
            line=dict(
                color=px.colors.qualitative.Bold[6],
                width=2
            )
        ),
        secondary_y=True
    )

    fig.update_layout(
        template="plotly_dark",
        title=dict(
            text="Daily Cases vs Vaccination Progress",
            font=dict(color="white", size=30)
        ),
        hovermode="x unified",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    fig.update_xaxes(
        type="date",
        dtick="M2",
        tickformat="%b %Y",
        tickangle=40
    )

    fig.update_yaxes(title_text="Daily Cases", secondary_y=False)
    fig.update_yaxes(title_text="Fully Vaccinated (Cumulative)", secondary_y=True)

    return fig


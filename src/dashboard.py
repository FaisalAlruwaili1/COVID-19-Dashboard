from data_loader import (
    load_covid_records,
    load_vaccination_data,
    get_total_by_month,
    get_grouped_by_country_cases,
    get_grouped_by_country_and_pop,
    get_grouped_by_country_top_death_to_case
)

from plotly_fig import fig1, fig2, fig_bar, fig_cases, fig_deaths, fig_vac


df = load_covid_records()
total_vaccinated = load_vaccination_data()

df_total_by_month = get_total_by_month(df)
df_grouped_by_country_cases = get_grouped_by_country_cases(df)
df_grouped_by_country_and_pop = get_grouped_by_country_and_pop(df)
df_grouped_by_country_top_death_to_case = get_grouped_by_country_top_death_to_case(df)


# figures
choropleth = fig1(df_grouped_by_country_cases)
scatter = fig2(df_grouped_by_country_and_pop)
ratio = fig_bar(df_grouped_by_country_top_death_to_case)
cases = fig_cases(df_total_by_month)
deaths = fig_deaths(df_total_by_month)
vac = fig_vac(df, total_vaccinated)


# HTML
with open("covid_dashboard.html", "w", encoding="utf-8") as f:

    f.write("""

    <html>

    <head>

        <style>

            body {

                background-color: #1e1e1e;

                color: white;

                font-family: Arial, sans-serif;

                margin: 0;

                padding: 20px;

            }

            h1, h2 { color: white; }

            .container {

                display: flex;

                flex-wrap: wrap;

                gap: 10px;           /* reduced gap between charts */

                justify-content: center;

                margin-top: 20px;    /* space from previous figure */

            }

            .chart {

                flex: 1 1 500px;

                max-width: 700px;

                min-width: 300px;

            }

        </style>

    </head>

    <body>

    """)



    f.write('<img src="image.png">')

    f.write("<h1>COVID-19 Analysis Dashboard (2020 - 2022)</h1>")

    f.write('<p style="font-size: 18px;">Interactive exploration of global COVID-19 trends from 2020–2022, including cases, deaths, vaccinations, and country-level comparisons.</p>')

    f.write("<h2>Interactive Charts</h2>")



    # First figures

    f.write(choropleth.to_html(include_plotlyjs="cdn", full_html=False))

    f.write(scatter.to_html(include_plotlyjs=False, full_html=False))

    f.write(ratio.to_html(include_plotlyjs=False, full_html=False))

    f.write(vac.to_html(include_plotlyjs=False, full_html=False))



    # Side-by-side charts

    f.write('<div class="container">')

    f.write('<div class="chart">')

    f.write(cases.to_html(include_plotlyjs=False, full_html=False))

    f.write('</div>')

    f.write('<div class="chart">')

    f.write(deaths.to_html(include_plotlyjs=False, full_html=False))

    f.write('</div>')

    f.write('</div>')  # end container



    f.write("""

    </body>

    </html>

    """)

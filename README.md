# COVID-19 Dashboard

This project documents a complete data analysis workflow, starting from raw data and culminating in a forecasting model. The goal is to process and understand COVID-19 case data to build a tool that can provide future projections. The journey begins with data ingestion and cleaning, moves through detailed exploration and visualization, and concludes with the application of a neural network to predict future trends.

## Tools & Libraries

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge)

![Seaborn](https://img.shields.io/badge/Seaborn-2E8B57?style=for-the-badge)

![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)

![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

## License 

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Data Sources

**Kaggle COVID-19 Stream Dataset**
  * Source: [https://www.kaggle.com/datasets/hgultekin/covid19-stream-data](https://www.kaggle.com/datasets/hgultekin/covid19-stream-data)
  * License: Open Database License (ODbL) [https://opendatacommons.org/licenses/odbl/](https://opendatacommons.org/licenses/odbl/)
  * Used files: `json`, `json_1`

**Our World in Data – COVID-19 Vaccinations**
  * Source: [https://archive.ourworldindata.org/20260616-064428/covid-vaccinations.html](https://archive.ourworldindata.org/20260616-064428/covid-vaccinations.html)
  * Authors: Edouard Mathieu, Hannah Ritchie, Lucas Rodés-Guirao, Cameron Appel, Daniel Gavrilov, Charlie Giattino, Joe Hasell, Bobbie Macdonald, Saloni Dattani, Diana Beltekian, Esteban Ortiz-Ospina, Max Roser
  * License: Creative Commons Attribution 4.0 International (CC BY 4.0) [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)
  * Used metric: `cumulative` vaccination data



## Requirements & Usage

```bash
pip install pandas seaborn numpy matplotlib statsmodels scikit-learn tensorflow

# Usage
python covid_analysis.py

```
## File Structure

The project contains the following files:

- `README.md` — This file, containing project overview and instructions  
- `Python-Script` — Main Python script for data analysis and forecasting  
- `Data` — COVID19 Dataset 

## Contributing

This is a community project! You are welcome to:  

- Fork the repository  
- Add new features  
- Improve the existing code  

If you find any issues or have suggestions, please open an issue — I’d love to hear from you.

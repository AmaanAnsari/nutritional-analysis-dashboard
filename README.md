# Nutritional Analysis Dashboard
## Overview

This repository hosts the code for a university project aimed at developing an interactive dashboard for nutritional analysis. Conducted as part of a course introducing visualization with Plotly in Python, this project forms a component of my Bachelor of Science studies in Business Informatics at Baden-Württemberg Cooperative State University. The primary focus of the project is the analysis of Body Mass Index (BMI) and sugar consumption patterns, utilizing a range of data visualization techniques.

## Application Structure

The application is structured into different pages, each representing a specific aspect of nutritional analysis. It's built using the Dash framework with Plotly for interactive visualizations.

### Pages

- **bmi_analysis.py**: This page presents an analysis of BMI data. It displays interactive charts showing average BMI for men and women across various regions.
- **data_explaination.py**: This page details the data preprocessing steps used in the project. It outlines how the data was cleaned and prepared for the subsequent analysis.
- **home.py**: The application's homepage. It introduces the project's objectives, highlighting the significance of sugar in Iight gain and its health consequences.
- **sugar_analysis.py**: Focuses on the analysis of sugar consumption. This page visualizes average sugar intake per person over different years and compares these trends across regions.

## Dataset Creation and Preprocessing

### Data Sources

For this project, I utilized the following datasets from Open Numbers:  
- [Gapminder BP Energy](https://github.com/open-numbers/ddf--gapminder--bp_energy)
- [Gapminder CO2 Emission](https://github.com/open-numbers/ddf--gapminder--co2_emission)
- [Gapminder Fastrack](https://github.com/open-numbers/ddf--gapminder--fasttrack)
- [Gapminder World](https://github.com/open-numbers/ddf--gapminder--gapminder_world)
- [Gapminder Life Expectancy](https://github.com/open-numbers/ddf--gapminder--life_expectancy)

### Preprocessing Steps

Each dataset consisted of multiple CSV files. I initially merged these files individually into separate dataframes and saved them. Following this, I combined these individual dataframes into one large dataframe.

This comprehensive dataframe includes over 700 features (columns) representing various countries, with some data going back as far as the year 1800. This alloId us to create an extensive correlation matrix to easily investigate interesting data relationships.

### Analysis and Visualization

Using Plotly, I visualized selected intriguing correlations in line or scatter plots. The most fascinating correlation was found betIen daily sugar intake and Body Mass Index (BMI). This relationship is showcased in our dashboard through static visualizations.

## Grading
Grade: 1.0
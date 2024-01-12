
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Reading the dataset
covid_data_path = 'COVID-19 Coronavirus.csv'
covid_data = pd.read_csv(covid_data_path)

# Setting the style for the plots
sns.set(style="whitegrid")

# Creating a figure for the dashboard
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# Dashboard Title
fig.suptitle('COVID-19 Data Analysis - Hamza Bashir Qureshi 22084845', fontsize=16)

# Plot 1: Top 10 Countries by Total Cases and Deaths
top_countries = covid_data.nlargest(10, 'Total Cases')
sns.barplot(x='Total Cases', y='Country', data=top_countries, ax=axes[0, 0], color='blue', label='Total Cases')
sns.barplot(x='Total Deaths', y='Country', data=top_countries, ax=axes[0, 0], color='red', label='Total Deaths')
axes[0, 0].set_title('Top 10 Countries by COVID-19 Cases and Deaths')
axes[0, 0].set_xlabel('Number of Cases/Deaths')
axes[0, 0].set_ylabel('Country')
axes[0, 0].legend()

# Plot 2: Average Death Rate by Continent
avg_death_rate = covid_data.groupby('Continent')['Death percentage'].mean().sort_values()
sns.barplot(x=avg_death_rate.values, y=avg_death_rate.index, ax=axes[0, 1], palette="viridis")
axes[0, 1].set_title('Average COVID-19 Death Rate by Continent')
axes[0, 1].set_xlabel('Average Death Rate (%)')
axes[0, 1].set_ylabel('Continent')

# Plot 3: Cases and Deaths per Million by Continent
cases_per_million = covid_data.groupby('Continent')['Tot Cases//1M pop'].mean().sort_values()
deaths_per_million = covid_data.groupby('Continent')['Tot Deaths/1M pop'].mean().sort_values()
sns.barplot(x=cases_per_million.values, y=cases_per_million.index, ax=axes[1, 0], color='lightblue', label='Cases per Million')
sns.barplot(x=deaths_per_million.values, y=deaths_per_million.index, ax=axes[1, 0], color='salmon', label='Deaths per Million')
axes[1, 0].set_title('COVID-19 Cases and Deaths per Million by Continent')
axes[1, 0].set_xlabel('Number per Million')
axes[1, 0].set_ylabel('Continent')
axes[1, 0].legend()

# Plot 4: COVID-19 Global Overview
sns.scatterplot(x='Total Cases', y='Total Deaths', data=covid_data, ax=axes[1, 1], hue='Continent', palette="deep", legend=False)
axes[1, 1].set_title('COVID-19 Global Overview')
axes[1, 1].set(xscale="log", yscale="log")
axes[1, 1].set_xlabel('Total Cases (log scale)')
axes[1, 1].set_ylabel('Total Deaths (log scale)')

# Dashboard Description
description = """
This dashboard provides a multi-faceted view of the COVID-19 pandemic:
1. The first plot shows the countries most affected in terms of cases and deaths.
2. The second plot highlights the varying death rates across continents, indicating the differential impact of the virus.
3. The third plot compares the burden of COVID-19 cases and deaths relative to population sizes across continents.
4. The final plot gives a global overview, illustrating the correlation between total cases and deaths worldwide.
"""
plt.figtext(0.5, 0.03, description, wrap=True, horizontalalignment='center', fontsize=12)

# Adjust layout
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Save the plot
plt.savefig('covid19_data_analysis_dashboard.png')

import pandas as pd
import matplotlib.pyplot as plt

# Read the file. We can read it with read_csv because it is UTF-8 and comma delimited.
co2_data = pd.read_csv("ex3_co2.dat")

# Get the data from 1950 onwards.
data_after_1950 = co2_data.loc[(co2_data["Year"] >= 1950)]

# Get the total CO2 of all countries and save it to the list total_co2.
country_list = sorted(list(set(co2_data["Entity"])))
total_co2 = []
for country in country_list:
    country_data = data_after_1950.loc[(data_after_1950["Entity"] == country)]
    co2_of_country = country_data["Annual CO₂ emissions (tonnes )"]
    total_co2.append(sum(co2_of_country))

# Get a dataframe of all countries and their total CO2 after 1950.
country_by_co2 = list(zip(country_list, total_co2))
country_by_co2 = pd.DataFrame(country_by_co2, columns=["Entity", "Total Emissions"])

# Compare some countries with a barplot. Note that only applicable country names will be displayed.
countries = country_by_co2.loc[country_by_co2["Entity"].isin(["China", "Malaysia", "Jamaica", "Finland", "Japan"])]
ax = countries.plot.bar(x="Entity", y="Total Emissions", rot=0)
ax.set_ylabel("Total Emissions")
ax.get_legend().remove()

# Get a list of the top five biggest countries/regions.
countries_ordered = country_by_co2.sort_values(by="Total Emissions", ascending=False)
top_five = countries_ordered[1:6]
top_five = list(top_five["Entity"])

# Get the data from 1950 onwards for the top ten countries/regions.
top_five_country_data = data_after_1950.loc[data_after_1950["Entity"].isin(top_five)]

# Time series for each country.
for country in top_five:
    data = top_five_country_data.loc[top_five_country_data["Entity"] == country]
    top_plot = data.plot.line(x="Year", y="Annual CO₂ emissions (tonnes )")
    top_plot.set_ylabel("Annual CO₂ emissions (tonnes )")
    top_plot.set_title(country)
    top_plot.get_legend().remove()

if __name__ == "__main__":
    plt.show()

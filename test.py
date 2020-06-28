import pandas as pd
from matplotlib import pyplot as plt 
import seaborn as sns
# set the background colour of the plot to white
sns.set(style="whitegrid", color_codes=True)
# setting the plot size for all plots
sns.set(rc={'figure.figsize':(11.7,8.27)})

from filenames import *
from functions import *
from test_file_functions import *

df_population_total = pd.read_excel(filename_population_total + excel_extension)
df_life_expectancy_years = pd.read_excel(filename_life_expectancy_years + excel_extension)
df_income_per_person_gdppercapita_ppp_inflation_adjusted = pd.read_excel(filename_income_per_person_gdppercapita_ppp_inflation_adjusted + excel_extension)
df_Country_continent_by_Gapminder = pd.read_excel(filename_Country_continent_by_Gapminder + excel_extension)


	
def main():
	
	(df_pop_total, df_life_expec_years, df_gdp, df_country_continent) = match_dfs_reset_index(df_population_total, df_life_expectancy_years, df_income_per_person_gdppercapita_ppp_inflation_adjusted, df_Country_continent_by_Gapminder)
	print_shape(df_pop_total, df_life_expec_years, df_country_continent, df_country_continent)

	# Initialize figure and ax
	fig, ax = plt.subplots()
	# Set the scale of the x-and y-axes
	ax.set(xscale="log")
	#sns.scatterplot( x = 'Albania', y = 'Afghanistan', data= df_pop_total.set_index('country').reset_index().transpose(), ax=ax)
	df_plt = df_pop_total.set_index('country').transpose()
	
	print(type(df_plt))
	print(df_plt.info(),'\n')
	#print(*list(df_plt.keys()))
	df_plt.insert(0, 'years', list(df_plt.index.values))
	print(df_plt.info(),'\n')
	keys = df_plt.keys()
	x = df_plt.keys()[0]
	y = df_plt.keys()[1]

	print_head(df_pop_total, df_life_expec_years, df_gdp, df_country_continent)

	print(len(list(set(df_pop_total.keys()) - set(df_gdp.keys()))))
	#sns.kdeplot(df_plt[keys[2]], ax=ax)
	#sns.lmplot(x=x, y=y, data=df_plt, fit_reg=False)
	#plt.show()

if __name__ == '__main__':
	main()
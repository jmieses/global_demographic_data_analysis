import pandas as pd
from matplotlib import pyplot as plt 
import seaborn as sns
sns.set()

from filenames import *
from functions import *
from test_file_functions import *

df_population_total = pd.read_excel(filename_population_total + excel_extension)
df_life_expectancy_years = pd.read_excel(filename_life_expectancy_years + excel_extension)
df_income_per_person_gdppercapita_ppp_inflation_adjusted = pd.read_excel(filename_income_per_person_gdppercapita_ppp_inflation_adjusted + excel_extension)
df_Country_continent_by_Gapminder = pd.read_excel(filename_Country_continent_by_Gapminder + excel_extension)


	
def main():
	print_shape(df_population_total, df_life_expectancy_years, df_income_per_person_gdppercapita_ppp_inflation_adjusted)
	print_if_nan(df_population_total, df_life_expectancy_years, df_income_per_person_gdppercapita_ppp_inflation_adjusted)
	
	df_pop_total, df_life_expec_years = match_df_pair_idx_reset(df_population_total, df_life_expectancy_years)
	df_life_expec_years, df_gdp = match_df_pair_idx_reset(df_life_expectancy_years, df_income_per_person_gdppercapita_ppp_inflation_adjusted) 
	
	print_shape(df_pop_total, df_life_expec_years, df_gdp)

	(df1, df2, df3, df4) = drop_dfs_nan(df_pop_total, df_life_expec_years, df_gdp, df_Country_continent_by_Gapminder)
	print_shape(df1, df2, df4)
	(df1, df2, df3, df4) = match_dfs_reset_index(df1, df2, df3, df4)
	print_shape(df1, df2, df4)

	


if __name__ == '__main__':
	main()
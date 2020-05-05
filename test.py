import pandas as pd

from filenames import *
from functions import *
from test_file_functions import *

df_population_total = pd.read_excel(filename_population_total + excel_extension)
df_life_expectancy_years = pd.read_excel(filename_life_expectancy_years + excel_extension)
df_income_per_person_gdppercapita_ppp_inflation_adjusted = pd.read_excel(filename_income_per_person_gdppercapita_ppp_inflation_adjusted + excel_extension)



	
def main():
	print_shape(df_population_total, df_life_expectancy_years, df_income_per_person_gdppercapita_ppp_inflation_adjusted)
	print_if_nan(df_population_total, df_life_expectancy_years, df_income_per_person_gdppercapita_ppp_inflation_adjusted)
	
	df_population_total, 

if __name__ == '__main__':
	main()
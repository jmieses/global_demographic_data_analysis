from test import *
from filenames import *
from functions import *


def get_df_name(df):
    name =[x for x in globals() if globals()[x] is df][0]
    return name
    
def print_shape(a, b, c):
	print(filename_population_total +      ' shape:                                           ', a.shape)
	print(filename_life_expectancy_years + ' shape:                                      ', b.shape)
	print(filename_income_per_person_gdppercapita_ppp_inflation_adjusted + ' shape:      ', c.shape)
	print()

def print_if_nan(a, b, c):
	print(filename_population_total +      ' NaN:                                             ', a.isnull().values.any())
	print(filename_life_expectancy_years + ' NaN:                                        ', b.isnull().values.any())
	print(filename_income_per_person_gdppercapita_ppp_inflation_adjusted + ' NaN:        ', c.isnull().values.any())
	print()



if __name__ == '__main__':
	main()
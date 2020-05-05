data1 = {'col1': ['abc', 'def'], 'col2': ['ghi', 'jkl']}
data2 = {'col1': ['abc', 'de', 'hjg'], 'col2': ['ghi', 'jkl', 'you']}
import pandas as pd
# data1.sort()
# data2.sort()
def match_list(data1, data2):
	if len(data1) > len(data2):
		data1 = [item for item in data1 if item in data2]
		return data1
	else:
		data2 = [item for item in data2 if item in data1]
		return data2

def unmtach_list(data1, data2):
	retVal = []
	if len(data1) > len(data2):
		for item in data1:
			if item not in data2:
				retVal.append()
	else:
		for item in data2:
			if item not in data1:
				retVal.append()
	return retVal

def unmatch_df(df1, df2):
	ulist = unmtach_list(list(df1.iloc[:, 0]), list(df2.iloc[:, 0]))
	
	if len(df1.columns) > len(df2.columns):
		return df1.drop(df1.loc[ulist]), df2
	else:
		return df1, df2.drop(df2.loc[ulist])

def match_df(df1, df2):
	"""
	Arguments: two dataframes
	Description: this function drops value keys that are not present in
	both data frames.
	Return: DataFrame
	"""
	match_values = match_list(list(df1.iloc[:, 0]), list(df2.iloc[:,0]))
	
	if len(df1.columns) > len(df2.columns):
		key = df1.keys()[0]
		return df1[df1[key].isin(match_values)]
	else:
		key = df2.keys()[0]
		return df2[df2[key].isin(match_values)]

def match_df_pair(df1, df2):
	"""
	Arguments: two dataframes
	Description: this function drops value keys that are not present in
	both data frames.
	Return: DataFrame
	"""
	match_values = match_list(list(df1.iloc[:, 0]), list(df2.iloc[:,0]))
	
	if len(df1.index) > len(df2.index):
		key = df1.keys()[0]
		df1 = df1[df1[key].isin(match_values)]
		return df1, df2
	else:
		key = df2.keys()[0]
		df2 = df2[df2[key].isin(match_values)]
		return df1, df2

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(type(df1))
print(type(df1.isna()))

# print(type(df1))
# help(match_df)


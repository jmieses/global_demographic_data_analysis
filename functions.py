from filenames import *

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


def match_df_pair_idx_reset(df1, df2):
	if df1.isnull().values.any():
		df1.dropna(inplace = True)
		df1.reset_index(drop=True, inplace = True)

	if df2.isnull().values.any():
		df2.dropna(inplace = True)
		df2.reset_index(drop=True, inplace = True)

	new_df1, new_df2 = match_df_pair(df1, df2)
	return new_df1, new_df2


def common_elements(*list_of_elements):
	"""
	Arguments: an iterable containing iterables.
	Returns: a list containing the intersection of all iterables.
	Description: This function looks for the common elements across
				 all iterables and returns a list with all common 
				 elements. 
	"""
	return list(set.intersection(*map(set, list_of_elements)))


def drop_dfs_nan(*dfs_series):
	"""
	Arguments: an iterable containing data frames list.
	Returns: iterable of data frames.
	Description: This functions looks for nan values across
				 the multiple data frames and removes those
				 rows. 
	"""
	for df in dfs_series:
		if df.isnull().values.any():
			df.dropna(inplace = True)
			df.reset_index(drop = True, inplace = True)
			
	return dfs_series


def match_dfs_reset_index(*dfs_series):
	common = common_elements(*[df[df.keys()[0]] for df in dfs_series])
	print(*common)
	print("Was called")

	for df in dfs_series:
		yield df[df[df.keys()[0]].isin(common)]


def main():
	pass

if __name__ == '__main__':
	main()


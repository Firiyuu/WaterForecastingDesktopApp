from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.model_selection import GridSearchCV
from sklearn import svm, datasets
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np
from scipy.stats import spearmanr
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from math import sqrt



from season import get_rainy, get_dry
from analyze import analyze, train, predict, train_ui
from dateandtime import get_date_time_after
#NORMALIZATION





def represent(series):
	series_ = series['TIME']
	series_list = series_.tolist()

	new_list = []

	counter = 0

	while counter != len(series_list):
			for i in range(1,49):
				counter+=1
				new_list.append(i)
	
	new_series = pd.Series(new_list)






	series = series.drop(columns=['TIME'])
	print("-----------------------")


	series['TIME'] = new_series
	print(len(series))

	return series




def run_nt(file_):

	series = pd.read_csv(file_)

	series = series.fillna(0)





	#12 to 5
	print("GETTING RAINY")
	series_rainy = get_rainy(series)

	print("ANALYZING")
	rainy = analyze(series_rainy)
	#rainy = represent(rainy)

	print("TRAINUI")
	df = train_ui(rainy)

	return df


	# predictions = predict(rainy, button_, cons, eps, p, gam)
	# ser = pd.Series(predictions)


	# date_time = get_date_time_after()

	# i_1 = ser.iloc[:48]
	# i_2 = ser.iloc[49:97]
	# i_3 = ser.iloc[98:146]

	# print(i_1)
	# print("Length: " + str(len(i_1)))

	# print(i_2)
	# print("Length: " + str(len(i_2)))

	# print(i_3)
	# print("Length: " + str(len(i_3)))

	# print(rainy)


	# rainy = pd.DataFrame(rainy, columns=['DATETIME','WATERLVEL','RF_DIGKILAAN','RF_ROGONGON','i-1','i-2','i-3'])
	# rainy = rainy.fillna(0)
	# print("---------RAINY DF--------------")

	# date_time_ = rainy['DATETIME']
	# first_ = rainy['i-1']
	# second_ = rainy['i-2']
	# third_ = rainy['i-3']

	# print(len(date_time_))
	# print(len(date_time))
	# print(len(first_))
	# print(len(i_1))


	# date = pd.Series(date_time)

	# first_ = i_1
	# second_ = i_2
	# third_ = i_3
	# date_time_ = date[:48]
	# print(rainy)





	# print(len(first_))
	# print(len(second_))
	# print(len(third_))
	# print(len(date_time_))
	# print(date_time_)


	# new_df =  pd.DataFrame({'DATETIME': date_time_.values,
	# 			'i-1': first_.values,
	# 			'i-2': second_.values,
	# 			'i-3': third_.values,
	# })

	# new_df = new_df.fillna(0)

	# print(new_df)

	# rainy.update(new_df)
	# rainy.fillna(0)




	# print("---------PREDICTION DF--------------")

	# print(rainy)

	# return rainy


	# ser.to_csv('prediction_series_nt.csv')
	# print("Length: " + str(len(predictions)))
	# prediction = pd.DataFrame(predictions, columns=['predictions']).to_csv('prediction_day1_rogongon_nt.csv')



# #6 to 11
# series_dry = get_dry(series)
# dry_ = analyze(series_dry)
# print(dry_.head())
# train(dry_)
# print(len(dry_))
# predictions_ = predict(dry_)
# print(predictions_)







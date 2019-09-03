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


from dateandtime import get_date_time_after

from season import get_rainy, get_dry
from architecture_1 import analyze, train, predict
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




def run(file_, button_, cons, eps, p, gam):

	series = pd.read_csv(file_)
	print(series.head())
	series = series.fillna(0)





	#12 to 5
	#series_rainy = get_rainy(series)
	rainy = analyze(series)
	#rainy = represent(rainy)
	#train(rainy)

	print(series.head())
	date_time = get_date_time_after()
	date_time = date_time[:12]


	predictions = predict(rainy, button_, cons, eps, p, gam)
	ser = pd.Series(predictions)
	ser.to_csv('prediction_series.csv')
	print("Length: " + str(len(predictions)))
	prediction = pd.DataFrame()
	prediction['PREDICTIONS'] = predictions
	print(prediction)

	print("==============PREDICTION====================")

	return prediction



# #6 to 11
# series_dry = get_dry(series)
# dry_ = analyze(series_dry)
# print(dry_.head())
# train(dry_)
# print(len(dry_))
# predictions_ = predict(dry_)
# print(predictions_)







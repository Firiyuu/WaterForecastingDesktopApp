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
import pickle
import time
import random


def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100



# def analyze(series):

# 	series['DATETIME'] = pd.to_datetime(series['DATETIME'])
# 	series['DATE'] = [d.date() for d in series['DATETIME']]
# 	series['TIME'] = [d.time() for d in series['DATETIME']]
# 	series['WATERLEVEL'] = series['WATERLEVEL']/1000


	 

# 	series['DATE'] = pd.to_datetime(series['DATE'])
# 	series['MONTH'] =   series['DATE'].dt.to_period('M')



# 	series['YEAR'] = pd.DatetimeIndex(series['DATE']).year
# 	series['MONTH'] = pd.DatetimeIndex(series['DATE']).month
# 	series['DAY'] = pd.DatetimeIndex(series['DATE']).day


# 	series['DATETIME'] = (series['DATETIME'] - series['DATETIME'].min())  / np.timedelta64(1,'D')
# 	series['DATE'] = pd.to_datetime(series['DATE'])
# 	series['DATE'] =  (series['DATE'] - series['DATE'].min())  / np.timedelta64(1,'D')
# 	series['TIME'] =  series['DATETIME'] - series['DATE']




# 	series = series.drop(columns="DATETIME")
# 	series = series.drop(columns="DAY")

# 	scaler = MinMaxScaler()
# 	scaler.fit(series)
# 	series = scaler.transform(series)
# 	series = pd.DataFrame(series, columns=['WATERLVEL','RF_DIGKILAAN','RF_ROGONGON', 'DAY', 'TIME', 'MONTH', 'YEAR'])
# 	print(series.head())

# 	return series


# def analyze(series):

# 	series['DATETIME'] = pd.to_datetime(series['DATETIME'])
# 	series['DATE'] = [d.date() for d in series['DATETIME']]
# 	series['TIME'] = [d.time() for d in series['DATETIME']]
# 	series['WATERLEVEL'] = series['WATERLEVEL']/1000


	 

# 	series['DATE'] = pd.to_datetime(series['DATE'])
# 	series['MONTH'] =   series['DATE'].dt.to_period('M')



# 	series['YEAR'] = pd.DatetimeIndex(series['DATE']).year
# 	series['MONTH'] = pd.DatetimeIndex(series['DATE']).month
# 	series['DAY'] = pd.DatetimeIndex(series['DATE']).day


# 	series['DATETIME'] = (series['DATETIME'] - series['DATETIME'].min())  / np.timedelta64(1,'D')
# 	series['DATE'] = pd.to_datetime(series['DATE'])
# 	series['DATE'] =  (series['DATE'] - series['DATE'].min())  / np.timedelta64(1,'D')
# 	series['TIME'] =  series['DATETIME'] - series['DATE']




# 	series = series.drop(columns="DATETIME")
# 	series = series.drop(columns="MONTH")
# 	series = series.drop(columns="YEAR")
# 	series = series.drop(columns="DATE")

# 	print(series.head())

# 	scaler = MinMaxScaler()
# 	scaler.fit(series)
# 	series = scaler.transform(series)
# 	series = pd.DataFrame(series, columns=['WATERLVEL','RF_DIGKILAAN','RF_ROGONGON', 'DAY', 'TIME'])
# 	print(series.head())

# 	return series


def train(series):
	print("---------- Training")
	print(series)
	
	

	scaler = MinMaxScaler()
	scaler.fit(series)
	print(series)
	series = scaler.transform(series)

	print("---------- Transformed")
	print(series)

	series = pd.DataFrame(series, columns=['WATERLVEL','RF_DIGKILAAN','RF_ROGONGON', 'DAY', 'TIME', 'MONTH', 'YEAR'])


	print("---------- New Dataframe")
	print(series)


	series = series[['WATERLVEL','RF_DIGKILAAN','RF_ROGONGON', 'DAY', 'TIME', 'MONTH', 'YEAR']]
	print("Normalized: ")
	print(series)

	series.to_csv('merge_normalized_ffffff1_nt.csv')



	#P-value gives us the probability of finding an observation under an assumption that a particular hypothesis is true.
	#This probability is used to accept or reject that hypothesis.

	# Correlation is a statistical term which in common usage refers 
	# to how close two variables are to having a linear relationship with each other.
	print("-----------------\nFeature Selection: Spearman\n")
	corr, p_value = spearmanr(series)
	print("Correlation: " + str(corr))
	print("P Value: " + str(p_value))
	print(series)

	#Using Pearson Correlation
	print("-----------------\nFeature Selection: Pearson\n")
	plt.figure(figsize=(12,10))
	cor = series.corr()
	sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
	plt.show()

def train_ui(series, button_, cons, eps, p, gam):
	#PREDICTION
	print(series.head())

	X = series[['WATERLVEL','RF_DIGKILAAN','RF_ROGONGON', 'DAY', 'TIME', 'MONTH', 'YEAR']]
	y = series[['WATERLVEL']]

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=101)

	lm = LinearRegression(normalize=True)
	lm.fit(X_train,y_train)

	# save the model to disk
	filename = 'finalized_model.sav'
	pickle.dump(lm, open(filename, 'wb'))


	for index, row_ in series.iterrows():
		predictions_ = []
		row = row_.values
		X_new = np.array(row).reshape(1, 7)
		predictions = lm.predict(X_new)
		predictions_.append(predictions[0][0])

		row_['WATERLVEL'] = predictions[0][0]
		row = row_.values

		X_new = np.array(row).reshape(1, 7)
		predictions = lm.predict(X_new)
		predictions_.append(predictions[0][0])


		row_['WATERLVEL']= predictions[0][0]
		row = row_.values
		X_new = np.array(row).reshape(1, 7)
		predictions = lm.predict(X_new)
		predictions_.append(predictions[0][0])

		print(predictions_)

		series.at[index,'i-1'] = predictions_[0]
		series.at[index,'i-2'] = predictions_[1]
		series.at[index,'i-3'] = predictions_[2]

	return series

def validate(series ,button_, cons, eps, p, gam):
	#PREDICTION


	X = series[['WATERLVEL', 'DAY', 'TIME', 'MONTH', 'YEAR','t-12','t-24','t-72','t-168']] 
	y = series[['WATERLVEL']]

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=101)

	series = series.reindex(columns=['WATERLVEL', 'DAY', 'TIME', 'MONTH', 'YEAR','t-12','t-24','t-72','t-168'])

	container = series.reindex(columns=['WATERLVEL', 'DAY', 'TIME', 'MONTH', 'YEAR','t-12','t-24','t-72','t-168','Predicted','RMSE','MAPE'])


	parameters = {'kernel': (str(button_).lower(), ),'C':[float(cons)],'gamma':[float(gam)],'epsilon':[float(eps)]}
	# print("======================================")
	# print(parameters)
	# print("======================================")

	svc = svm.SVR()
	clf = GridSearchCV(svc, parameters, cv=2)
	fitted = clf.fit(X_train.astype('int'), y_train.astype('int'))



	for index, row_ in series.iterrows():
		try:

			predictions_ = []
			row = row_.values
			X_new = np.array(row).reshape(1, 9)


			print("\nBest parameters set found on development set:\n")
			print(clf.best_params_)
			print("Grid scores on development set:")
			means = clf.cv_results_['mean_test_score']
			stds = clf.cv_results_['std_test_score']



			predictions = clf.predict(X_new)


			y_val_new = []


			for predict in predictions:
				item_ = float(predict) + random.uniform(0.001,0.1)
				print(str(item_))
				y_val_new.append(float(predict) + random.uniform(0.001,0.1))

			y_new = y_test.iloc[index]['WATERLVEL']
			y_new = [y_new]
			# print(y_new)

			rms = sqrt(mean_squared_error(y_new, y_val_new))
			print("\n\nRMSE Accuracy score: " + str(rms))

			mape = mean_absolute_percentage_error(y_new, y_val_new)
			print("\n\nMAPE Accuracy score: " + str(mape))


			container.at[index,'Predicted'] = str(y_val_new[0])
			container.at[index,'MAPE'] = rms
			container.at[index,'RMSE'] = mape

		except Exception as e:
			print(e)
			continue



	container.drop(['DAY','TIME','MONTH','YEAR','t-12','t-24','t-72','t-168'], axis=1, inplace=True)
	print("==================Final==========================")
	print(container)
	return container




def predict(series, button_, cons, eps, p, gam):
	#PREDICTION
	print(series.head())

	X = series[['WATERLVEL','RF_DIGKILAAN','RF_ROGONGON', 'DAY', 'TIME', 'MONTH', 'YEAR']]
	y = series[['WATERLVEL']]

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=101)

	lm = LinearRegression()
	lm.fit(X_train,y_train)

	for x in X_test['WATERLVEL']:
		predictions = lm.predict(X_test)
		print(predictions)


	plt.scatter(y_test,predictions)
	plt.show()

	predictions = lm.predict(series)
	series['PREDICTIONS'] = predictions
	series.to_csv('spearman_predict_f111.csv')



	X = series[['WATERLVEL','RF_DIGKILAAN','RF_ROGONGON', 'DAY', 'TIME', 'MONTH', 'YEAR']]
	y = series[['WATERLVEL']]



	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=101)




	#GRID SEARCH CROSS VALIDATION
	#GRID SEARCH CROSS VALIDATION
	#parameters = {'kernel': ('linear', 'rbf','poly'), 'C':[1.5, 10],'gamma': [1e-7, 1e-4],'epsilon':[0.1,0.2,0.5,0.3]}

	parameters = {'kernel': (str(button_).lower(), ),'C':[float(cons)],'gamma':[float(gam)],'epsilon':[float(eps)]}
	print("======================================")
	print(parameters)
	print("======================================")

	svc = svm.SVR()
	clf = GridSearchCV(svc, parameters, cv=2)
	fitted = clf.fit(X_train.astype('int'), y_train.astype('int'))
	print(fitted)


	print("\nBest parameters set found on development set:\n")
	print(clf.best_params_)
	print("Grid scores on development set:")
	means = clf.cv_results_['mean_test_score']
	stds = clf.cv_results_['std_test_score']
	for mean, std, params in zip(means, stds, clf.cv_results_['params']):
	    print("%0.3f (+/-%0.03f) for %r"
	          % (mean, std * 2, params))\

	#VALIDATE VIA RMSE

	predictions = clf.predict(X_test)
	print(predictions)
	rms = sqrt(mean_squared_error(y_test, predictions))
	print("\n\nRMSE Accuracy score: " + str(rms))

	mape = mean_absolute_percentage_error(y_test, predictions)

	print("\n\nMAPE Accuracy score: " + str(mape))
	plt.plot(y_test)
	plt.plot(predictions)
	plt.legend(["true", "pred"])
	plt.show()

	return predictions
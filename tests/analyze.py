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
def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100



def analyze(series):

	series['DATETIME'] = pd.to_datetime(series['DATETIME'])
	series['DATE'] = [d.date() for d in series['DATETIME']]
	series['TIME'] = [d.time() for d in series['DATETIME']]
	series['WATERLVEL'] = series['WATERLVEL']


	 

	series['DATE'] = pd.to_datetime(series['DATE'])
	series['MONTH'] =   series['DATE'].dt.to_period('M')



	series['YEAR'] = pd.DatetimeIndex(series['DATE']).year
	series['MONTH'] = pd.DatetimeIndex(series['DATE']).month
	series['DAY'] = pd.DatetimeIndex(series['DATE']).day


	series['DATETIME'] = (series['DATETIME'] - series['DATETIME'].min())  / np.timedelta64(1,'D')
	series['DATE'] = pd.to_datetime(series['DATE'])
	series['DATE'] =  (series['DATE'] - series['DATE'].min())  / np.timedelta64(1,'D')
	series['TIME'] =  series['DATETIME'] - series['DATE']




	series = series.drop(columns="DATETIME")
	series = series.drop(columns="DAY")

	# scaler = MinMaxScaler()
	# scaler.fit(series)
	# series = scaler.transform(series)
	# series = pd.DataFrame(series, columns=['WATERLVEL', 'DAY', 'TIME', 'MONTH', 'YEAR'])
	# print(series.head())

	return series


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

	series = pd.DataFrame(series, columns=['WATERLVEL', 'DAY', 'TIME', 'MONTH', 'YEAR'])


	print("---------- New Dataframe")
	print(series)


	series = series[['WATERLVEL', 'DAY', 'TIME', 'MONTH', 'YEAR']]
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
	#plt.show()




def archi1(series, last_):

	ranges = [356, 730, 1095]

	for range_ in ranges:
		print(str(range_))

		for num in range(1,range_):
			_index = 't-' + str(range_)

			for i in range(0,num*48):
				i_index = series.iloc[last_-i]['WATERLVEL']
				series.at[i,_index] = i_index

	series = series.fillna(0)

	return series


def archi2(series, last_):
	ranges = [12, 24, 72, 168]

	for range_ in ranges:
		print(str(range_))

		for num in range(1,range_):
			_index = 't-' + str(range_)

			for i in range(0,num*2):
				i_index = series.iloc[last_-i]['WATERLVEL']
				series.at[i,_index] = i_index

	series = series.fillna(0)

	return series


def train_ui(series):
	#PREDICTION



	last_ = int(len(series['WATERLVEL'].tolist())) -1

	series = archi1(series, last_)
	#series2 = archi1(series, last_)


	#print(series.head())
	#print(series2.head())



	return series

def validate(series ,button_, cons, eps, p, gam):
	#PREDICTION

	X = series[['WATERLVEL', 'DAY', 'TIME', 'MONTH', 'YEAR','t-356','t-730','t-1095']]
	y = series[['WATERLVEL']]

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=101)



	parameters = {'kernel': (str(button_).lower(), ),'C':[float(cons)],'gamma':[float(gam)],'epsilon':[float(eps)]}
	# print("======================================")
	# print(parameters)
	# print("======================================")

	svc = svm.SVR()
	clf = GridSearchCV(svc, parameters, cv=2)
	fitted = clf.fit(X_train.astype('int'), y_train.astype('int'))
	# print(fitted)




	for index, row_ in series.iterrows():
		try:
			predictions_ = []
			row = row_.values
			X_new = np.array(row).reshape(1, 10)


			# ---------------------------



			print("\nBest parameters set found on development set:\n")
			print(clf.best_params_)
			print("Grid scores on development set:")
			means = clf.cv_results_['mean_test_score']
			stds = clf.cv_results_['std_test_score']


			#VALIDATE VIA RMSE

			predictions = clf.predict(X_new)
			y_new = y_test.iloc[index]['WATERLVEL']
			y_new = [y_new]
			# print(y_new)

			rms = sqrt(mean_squared_error(y_new, predictions))
			print("\n\nRMSE Accuracy score: " + str(rms))

			mape = mean_absolute_percentage_error(y_new, predictions)
			print("\n\nMAPE Accuracy score: " + str(mape))


			series.at[index,'Predicted'] = str(predictions[0])

			series.at[index,'MAPE'] = rms
			series.at[index,'RMSE'] = mape

		except Exception as e:
			continue

	# series.drop(['DAY','TIME','MONTH','YEAR','i-1','i-2','i-3'], axis=1, inplace=True)
	return series



def predict(series, button_, cons, eps, p, gam, archi):
	#PREDICTION
	# print(series.head())
	print("Archi: " + str(archi))

	if archi == "ARCHITECTURE1":
		X = series[['WATERLVEL', 'DAY', 'TIME', 'MONTH', 'YEAR','t-356','t-730','t-1095']]
		y = series[['WATERLVEL']]
	else:
		X = series[['WATERLVEL', 'DAY', 'TIME', 'MONTH', 'YEAR','t-12','t-24','t-72','t-168']]   #[12, 24, 72, 168]
		y = series[['WATERLVEL']]		

	# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=101)
	# lm.fit(X_train,y_train)
	# lm = LinearRegression()


	# for x in X_test['WATERLVEL']:
	# 	predictions = lm.predict(X_test)


	# plt.scatter(y_test,predictions)
	# plt.show()

	# predictions = lm.predict(series)
	# series['PREDICTIONS'] = predictions
	# series.to_csv('NEWPREDICT.csv')



	if archi == "ARCHITECTURE1":
		X = series[['WATERLVEL', 'DAY', 'TIME', 'MONTH', 'YEAR','t-356','t-730','t-1095']]
		y = series[['WATERLVEL']]
	else:
		X = series[['WATERLVEL', 'DAY', 'TIME', 'MONTH', 'YEAR','t-12','t-24','t-72','t-168']]   #[12, 24, 72, 168]
		y = series[['WATERLVEL']]		


	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)


	X_train, X_val, y_train, y_val  = train_test_split(X_train, y_train, test_size=0.25, random_state=1)

	#GRID SEARCH CROSS VALIDATION
	#GRID SEARCH CROSS VALIDATION
	#parameters = {'kernel': ('linear', 'rbf','poly'), 'C':[1.5, 10],'gamma': [1e-7, 1e-4],'epsilon':[0.1,0.2,0.5,0.3]}

	parameters = {'kernel': (str(button_).lower(), ),'C':[float(cons)],'gamma':[float(gam)],'epsilon':[float(eps)]}
	# print("======================================")
	# print(parameters)
	# print("======================================")

	svc = svm.SVR()
	clf = GridSearchCV(svc, parameters, cv=2, scoring="accuracy",n_jobs=32, iid=False, verbose=2)



	print("Training")

	fitted = clf.fit(X_train, y_train)

	filename = str(archi) + "-Rainy-"  + str(button_)+"-"+str(cons)+"-"+str(eps)+"-"+str(gam)+'.sav'
	pickle.dump(fitted, open(filename, 'wb'))

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
	#print(predictions)
	print("Train: " + str(len(y_train['WATERLVEL'].tolist())))
	print("Val: " + str(len(y_val['WATERLVEL'].tolist())))
	print("Test: " + str(len(y_test['WATERLVEL'].tolist())))
	print("Prediction: " + str(len(predictions)))

	y_val1 = pd.read_csv('raintest.csv')
	y_val1 = y_val1['waterlevel'].tolist()

	rms = sqrt(mean_squared_error(y_val1, predictions[:len(y_val1)]))
	print("\n\nRMSE Accuracy score: " + str(rms))

	mape = mean_absolute_percentage_error(y_val1, predictions[:len(y_val1)])

	print("\n\nMAPE Accuracy score: " + str(mape))

	# SCATTER
	fig, ax = plt.subplots()
	ax.set_title(str(archi) + " Rainy " + str(button_)+", Parameters: cons: " +str(cons)+ " epsilon: " +str(eps)+" gamma: "+str(gam))
	ax.plot(y_val, predictions[:len(y_val)], color = "red")
	#ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=4, color = "blue")
	ax.set_xlabel('Actual')
	ax.set_ylabel('Predicted')
	#plt.show()
	figure_name = "Images/" + str(archi) + "-Rainy-"  + str(button_)+"-"+str(cons)+"-"+str(eps)+"-"+str(gam)+".png"
	fig.savefig(figure_name, format="png")
	plt.close(fig)  


	return predictions
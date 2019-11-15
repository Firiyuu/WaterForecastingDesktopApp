from final import run_nt
import os
import numpy
import pandas as pd
from analyze import validate, predict
from statsmodels.graphics.tsaplots import plot_acf
from matplotlib import pyplot
import time

from season import get_rainy, get_dry
from analyze import analyze

import logging
logging.basicConfig(filename='DRYArchi1and2.log',level=logging.DEBUG)



def autocorr(x, t=1):
    return numpy.corrcoef(numpy.array([x[:-t], x[t:]]))



def set_a(file, Kernel, df, df1):
	cons = 26.91
	eps = 0.0004
	gam = 0.105
	p=1



	predict(df, Kernel, cons, eps, p, gam, "ARCHITECTURE2")
	predict(df1, Kernel, cons, eps, p, gam, "ARCHITECTURE1")





	print("====================================================")

def set_b(file, Kernel, df, df1):
	cons = 2.83
	eps = 0.006
	gam = 0.297
	p=1




	#validate(df, Kernel, cons, eps, p, gam)
	predict(df, Kernel, cons, eps, p, gam, "ARCHITECTURE2")
	predict(df1, Kernel, cons, eps, p, gam, "ARCHITECTURE1")




	print("====================================================")

def set_c(file, Kernel, df, df1):
	cons = 1.41
	eps = 0.006
	gam = 0.297
	p=1




	#validate(df, Kernel, cons, eps, p, gam)
	predict(df, Kernel, cons, eps, p, gam, "ARCHITECTURE2")
	predict(df1, Kernel, cons, eps, p, gam, "ARCHITECTURE1")




	print("====================================================")

def set_d(file, Kernel, df, df1):
	cons = 1.19
	eps = 0.008
	gam = 0.707
	p=1



	predict(df, Kernel, cons, eps, p, gam, "ARCHITECTURE2")
	predict(df1, Kernel, cons, eps, p, gam, "ARCHITECTURE1")




	print("====================================================")

def set_e(file, Kernel, df, df1):
	cons = 1.00
	eps = 0.011
	gam = 0.841
	p=1




	predict(df, Kernel, cons, eps, p, gam, "ARCHITECTURE2")
	predict(df1, Kernel, cons, eps, p, gam, "ARCHITECTURE1")




	print("====================================================")


def set_f(file, Kernel, df, df1):
	cons = 1.00
	eps = 0.011
	gam = 0.189
	p=1




	#validate(df, Kernel, cons, eps, p, gam)
	predict(df, Kernel, cons, eps, p, gam, "ARCHITECTURE2")
	predict(df1, Kernel, cons, eps, p, gam, "ARCHITECTURE1")




	print("====================================================")





file = "D:/Aug/waterlevel_forecastingsystem/NORMALIZED-DATA.csv"

Kernels = ["Linear","Poly", "Sigmoid", "RBF"]

# df, df1 = run_nt(file)
# df.to_csv("NEWCSV.csv")
# df = df.fillna(0)

# df1.to_csv("NEWCSV1.csv")
# df1 = df1.fillna(0)


df = pd.read_csv('NEWCSV.csv')
df1 = pd.read_csv('NEWCSV111.csv')
df = df.fillna(0)
df1 = df1.fillna(0)

for Kernel in Kernels:
	print("Kernel: " + str(Kernel))
	set_a(file,Kernel, df, df1)
	set_b(file,Kernel, df, df1)
	set_c(file,Kernel, df, df1)
	set_d(file,Kernel, df, df1)
	set_e(file,Kernel, df, df1)
	set_f(file,Kernel, df, df1)



import math
import os
from keras.utils import to_categorical
import numpy as np

x=0

#windoof
'''
print("test"+os.path.realpath(__file__))
splitted_path=os.path.realpath(__file__).split("\\")
print(splitted_path)
splitted_path_shorted=splitted_path[0:len(splitted_path)-1]
print(splitted_path_shorted)
zusammengefuegt=""
for teil in splitted_path_shorted:
	zusammengefuegt+=teil+"\\"

#Lesen der Datei
DATA_CSV = open(zusammengefuegt+'DATACSV.txt', 'w+', encoding='utf-8', errors='ignore')
'''

#DATA_CSV=open('DATACSV.txt', 'w+', encoding='utf-8')
DATA_CSV=open('csv_data/DATACSV.txt', 'w+')

DATA_CSV.write("Input,Output")



while(1):
	print ("\n"+str(x)+":")
	#y=round(math.sin(x/2), 2)
	#y = round(-(1 / (1 + math.exp(-x))), 2)
	#y=round(math.sin(x), 2)
	#y=3*x**5-4*x**3-6*x
	y=0.2+0.4*x/10**2+0.3*x/10*np.sin(15*x/10)+0.05*np.cos(50*x/10)
	#y=x**2/10
	DATA_CSV.write("\n"+str(x)+","+str(y))
	print("\n"+str(x)+","+str(y))
	x+=0.05
	x=round(x, 2)
	if x>10:
		break
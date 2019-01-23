import math
import os
from keras.utils import to_categorical
x=-20

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
	y=round(math.sin(x/2), 2)
	#y = to_categorical(y)
	DATA_CSV.write("\n"+str(x)+","+str(y))
	x+=0.5
	if x==20.5:
		break
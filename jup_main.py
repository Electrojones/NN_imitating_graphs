#!/usr/bin/env python
# coding: utf-8

# In[7]:


from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils
import numpy
import pandas as pd


    

numpy.random.seed(7)

# Defining column names for datasets
COLUMN_NAMES = [
        'Input', 
        'Output'
        ]
		
# Import training dataset
training_dataset = pd.read_csv('csv_data/DATACSV.txt', names=COLUMN_NAMES, header=0, dtype=numpy.float32)

train_x = training_dataset.iloc[:, 0].values
train_y = training_dataset.iloc[:, 1].values

# Encoding training dataset
encoding_train_y = np_utils.to_categorical(train_y)

# Creating a model
model = Sequential()
model.add(Dense(1, input_dim=1, activation='relu'))
model.add(Dense(60, activation='relu'))
model.add(Dense(1, activation='relu'))



# Compiling model
model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy'])

# Training a model
model.fit(train_x, train_y, epochs=100, batch_size=1)




# Get test value
print(model.predict(numpy.array([3])))


# In[ ]:


training_dataset


# In[6]:


import matplotlib.pyplot as plt
plt.figure()
# Defining column names for datasets
COLUMN_NAMES = [
        'Input', 
        'Output'
        ]
		
# Import training dataset
training_dataset = pd.read_csv('csv_data/DATACSV.txt', names=COLUMN_NAMES, header=0, dtype=numpy.float32)

train_x = training_dataset.iloc[:, 0].values
train_y = training_dataset.iloc[:, 1].values

ax = plt.gca()

#training_dataset=training_dataset.cumsum()
training_dataset.plot(kind='line',x='Input',y='Output',ax=ax);


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[20]:


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
training_dataset = pd.read_csv('csv_data/DATACSV.txt', names=COLUMN_NAMES, header=0)
train_x = training_dataset.iloc[:, 0].values
train_y = training_dataset.iloc[:, 1].values

# Encoding training dataset
encoding_train_y = np_utils.to_categorical(train_y)

# Creating a model
model = Sequential()
model.add(Dense(10, input_dim=1, activation='relu'))
model.add(Dense(10, activation='relu'))

#old, random fix
#model.add(Dense(3, activation='softmax'))

model.add(Dense(2, activation='softmax'))


# Compiling model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Training a model
model.fit(train_x, encoding_train_y, epochs=100, batch_size=1)

# evaluate the model
scores = model.evaluate(train_x, encoding_train_y)
print("\nAccuracy: %.2f%%" % (scores[1]*100))

print(model.predict(numpy.array([3])))


# In[17]:


import numpy
import pandas as pd

numpy.random.seed(7)

# Defining column names for datasets
COLUMN_NAMES = [
        'Input', 
        'Output'
        ]
		
# Import training dataset
training_dataset = pd.read_csv('csv_data/DATACSV.txt', names=COLUMN_NAMES, header=0)
train_x = training_dataset.iloc[:, 0].values
train_y = training_dataset.iloc[:, 1].values

train_y


# In[ ]:





import random
from fastapi import APIRouter
import joblib
import pandas as pd
from pydantic import BaseModel, confloat
import logging
import random
import pandas as pd
import numpy as np
from fastapi import APIRouter
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from keras.models import load_model
#import tensorflow as tf
#from tensorflow import keras
#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import Dense


log = logging.getLogger(__name__)
router = APIRouter()

#load and read the file
'''df = pd.read_csv("airbnb.csv", index_col=0)
dataset = df.values
X = dataset[:,0:12]
y = dataset[:,12]
y = np.reshape(y, (-1,1))
scaler_x = MinMaxScaler()
scaler_y = MinMaxScaler()
scaler_x.fit(X)
xscale=scaler_x.transform(X)
scaler_y.fit(y)
yscale=scaler_y.transform(y)
X = StandardScaler().fit_transform(X)
y = StandardScaler().fit_transform(y.reshape(len(y),1))[:,0]
X_train, X_test, y_train, y_test = train_test_split(xscale, yscale)
model = Sequential()
model.add(Dense(12, input_dim=10, kernel_initializer='normal', activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(loss='mse', optimizer='adam', metrics=['mse','mae'])
history = model.fit(X_train, y_train, epochs=50, batch_size=50,  verbose=1, validation_split=0.2)
model.save('keras_nn_model')
'''
#classifier = joblib.load('app/api/classifier.joblib')
#print('Pickled model loaded!')
classifier = load_model('keras_model/keras_nn_model.h5')

class AirBnB(BaseModel):
    """Data model to parse & validate airbnb measurements"""
    {
    "userId":float=Field(..., example=10292),
    "name":str=Field(..., example="Chris"),
    "room_type":str=Field(..., example="large"),
    "location":str=Field(..., example="Japan"),
    "price":float=Field(..., example=255.99),
    "accommodates":float=Field(..., example=2),
    "bathrooms":float=Field(..., example=3),
    "bedrooms":float=Field(..., example=4),
    "beds":float=Field(..., example=2),
    "guests_included":float=Field(..., example=4),
    "minimum_nights":float=Field(..., example=3),
    "maximum_nights":float=Field(..., example=6)
    }

    def to_df(self):
        return pd.DataFrame([dict(self)])

@router.post('/predict')
async def predict_species(airbnb: AirBnB):
    """Random baseline predictions for classification problem"""
    X_new = airbnb.to_df()
    log.info(X_new)
    model = classifier
    Xnew = np.array([
        X_new['userId'].iloc[0], X_new['name'].iloc[0], X_new['room_type'].iloc[0], 
        X_new['location'].iloc[0], X_new['price'].iloc[0], X_new['accommodates'].iloc[0],
        X_new['bathrooms'].iloc[0], X_new['bedrooms'].iloc[0], X_new['beds'].iloc[0],
        X_new['guests_included'].iloc[0], X_new['minimum_nights'].iloc[0], 
        X_new['maximum_nights']]
    )
    Xnew = scaler_x.transform(Xnew)
    y_pred = model.predict(Xnew)
    y_pred = scaler_y.inverse_transform(y_pred)
    y_pred = float(y_pred[0][0])
    return {
        'prediction':y_pred
    }

    


@router.get('/random')
def random_airbnb():
    """Return a random airbnb species"""
    return random.choice([{"userId":1, "name":"Chris", "room_type":"large", 
    "location":"Japan",
    "price":255.99,
    "accommodates":3,
    "bathrooms":2,
    "bedrooms":2,
    "beds":3,
    "guests_included":2,
    "minimum_nights":3,
    "maximum_nights":6}])
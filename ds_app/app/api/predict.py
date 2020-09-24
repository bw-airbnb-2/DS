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
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


log = logging.getLogger(__name__)
router = APIRouter()

#load and read the file
df = pd.read_csv("airbnb.csv", index_col=0)
dataset = df.values
X = dataset[:,0:10]
y = dataset[:,10]
y = np.reshape(y, (-1,1))
scaler_x = MinMaxScaler()
scaler_y = MinMaxScaler()
scaler_x.fit(X)
xscale=scaler_x.transform(X)
scaler_y.fit(y)
yscale=scaler_y.transform(y)
'''
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
  "userId":1,
  "name":"Chris",
  "room_type":"large",
  "location":"Japan",
  "price":255.99,
  "accommodates":3,
  "bathrooms":2,
  "bedrooms":2,
  "beds":3,
  "guests_included":2,
  "minimum_nights":3,
  "maximum_nights":6
    }

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""
        return pd.DataFrame([dict(self)])

@router.post('/predict')
async def predict_species(item: AirBnB):
    """Make random baseline predictions for classification problem."""
    X_new = item.to_df()
    log.info(X_new)
    model = tf.keras.models.load_model("keras_model2")
    Dict = {'Apartment' : 1, 'House' : 0, 'flexible' : 0, 'moderate' : 1, 'strict' : 2, 'yes' : 1, 'no' : 0}
    prop_type = Dict.get(X_new['property_type'].iloc[0])
    can_pol = Dict.get(X_new['cancellation_policy'].iloc[0])
    free_park = Dict.get(X_new['free_parking'].iloc[0])
    wi_fi = Dict.get(X_new['wifi'].iloc[0])
    cab_tv = Dict.get(X_new['cable_tv'].iloc[0])
    Xnew = np.array([[X_new['zipcode'].iloc[0], X_new['square_footage'].iloc[0], X_new['bedrooms'].iloc[0], X_new['bathrooms'].iloc[0], X_new['review_score_rating'].iloc[0], X_new['accommodates'].iloc[0], X_new['cleaning_fee'].iloc[0], float(free_park), 
                           float(wi_fi), float(cab_tv), float(prop_type), float(can_pol)]])
    Xnew= scaler_x.transform(Xnew)
    y_pred = model.predict(Xnew)
    y_pred = scaler_y.inverse_transform(y_pred)
    y_pred = float(y_pred[0][0])
    #y_pred = float(random.randint(100, 500))
    return {
        'prediction': y_pred
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
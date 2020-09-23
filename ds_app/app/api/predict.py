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
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
#import tensorflow as tf
#from tensorflow import keras
#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import Dense

# load and read the file
df = pd.read_csv("https://raw.githubusercontent.com/bw-airbnb-2/DS/master/airbnb.csv", index_col=0)
dataset = df.values

log = logging.getLogger(__name__)
router = APIRouter()

#classifier = joblib.load('app/api/classifier.joblib')
#print('Pickled model loaded!')


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
        return pd.DataFrame([dict(self)])

@router.post('/predict')
async def predict_species(airbnb: AirBnB):
    """Random baseline predictions for classification problem"""
    X_new = airbnb.to_df()
    log.info(X_new)
    model = tf.keras.models.load_model("ds_app/keras_model/saved_model-3.pb")
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
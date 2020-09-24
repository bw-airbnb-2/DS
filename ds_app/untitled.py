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
from keras.models import load_model
import os

log = logging.getLogger(__name__)
router = APIRouter()

model = load_model('keras_nn_model.h5')

class AirBnB(BaseModel):
    """Data model to parse & validate airbnb measurements"""
    
    zipcode: float = Field(..., example=10453)
    property_type: str = Field(..., example='House')
    square_footage: float = Field(..., example=4000)
    bedrooms: float = Field(..., example=6)
    bathrooms: float = Field(..., example=2)
    review_score_rating: float = Field(..., example=70)
    accommodates: float = Field(..., example=1)
    cancellation_policy: str = Field(..., example='moderate')
    cleaning_fee: float = Field(..., example=300)
    free_parking: str = Field(..., example='yes')
    wifi: str = Field(..., example='yes')
    cable_tv: str = Field(..., example='yes')

    def to_df(self):
        """Convert pydantic object to pandas dataframe with 1 row."""

@router.post('/predict')
async def predict_species(item: AirBnB):
    """Make random baseline predictions for classification problem."""
    X_new = item.to_df()
    log.info(X_new)
    Dict = {'Apartment' : 1, 'House' : 0, 'flexible' : 0, 'moderate' : 1, 'strict' : 2, 'yes' : 1, 'no' : 0}
    prop_type = Dict.get(X_new['property_type'].iloc[0])
    can_pol = Dict.get(X_new['cancellation_policy'].iloc[0])
    free_park = Dict.get(X_new['free_parking'].iloc[0])
    wi_fi = Dict.get(X_new['wifi'].iloc[0])
    cab_tv = Dict.get(X_new['cable_tv'].iloc[0])
    Xnew = np.array([[X_new['zipcode'].iloc[0], X_new['square_footage'].iloc[0], X_new['bedrooms'].iloc[0],
                      X_new['bathrooms'].iloc[0], X_new['review_score_rating'].iloc[0], X_new['accommodates'].iloc[0],
                      X_new['cleaning_fee'].iloc[0], float(free_park), 
                      float(wi_fi), float(cab_tv), float(prop_type), float(can_pol)]])
    Xnew= scaler_x.transform(Xnew)
    y_pred = model.predict(Xnew)
    y_pred = scaler_y.inverse_transform(y_pred)
    y_pred = float(y_pred[0][0])
    #y_pred = float(random.randint(100, 500))
    return {
        'prediction': y_pred
    }


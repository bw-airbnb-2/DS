import logging
import random

import pandas as pd
import numpy as np
from fastapi import APIRouter
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


log = logging.getLogger(__name__)
router = APIRouter()


df = pd.read_csv('airbnb.csv', index_col=0)
dataset = df.values
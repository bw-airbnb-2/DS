import logging
import random
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV

from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get('/vis/{meanerror}')
async def vis(meanerror: str):

    df = pd.read_csv('https://raw.githubusercontent.com/Air-BnB-2-BW/data-science/master/airbnb_BW2.csv')
    #print(df.shape)
    #print(df.head())

    dataset = df.values
    #dataset

    X = dataset[:,0:10]
    y = dataset[:,10]
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
    history = model.fit(X_train, y_train, epochs=150, batch_size=50,  verbose=1, validation_split=0.2)

    def create_model(lr=.001,opt=SGD):
        opti = opt(lr)

        # create model
        model = Sequential()
        model.add(Dense(32, input_dim=10, kernel_initializer='normal', activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(10, activation="softmax"))

        # Compile model
        model.compile(loss='sparse_categorical_crossentropy', optimizer=opti, metrics=['accuracy'])
        return model

    # fix random seed for reproducibility
    seed = 7
    np.random.seed(seed)
    model = KerasClassifier(build_fn=create_model, verbose=1)

    # define the grid search parameters
    batch_size = [16,32,64]
    epochs = [32,64,128]
    param_grid = dict(batch_size=batch_size, epochs=epochs)
    grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1, cv=3)
    grid_result = grid.fit(X_train, y_train,validation_split=.2)

    # summarize results
    #print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
    means = grid_result.cv_results_['mean_test_score']
    maes = grid_result.cv_results_['mean_average_error']
    params = grid_result.cv_results_['params']
    for mean, mae, param in zip(means, maes, params):
        #print("%f (%f) with: %r" % (mean, mae, param))

        plt.figure(figsize=(10,8))
        plt.bar(means, maes, params, align='center')
        plt.xticks(means, maes, params)
        plt.xlabel('Mean Test Score')
        plt.ylabel('Mean Average Error')
        return plt.to_json()
## ☝️ **AirBnB Optimal Price**

According to data.world, since 2008, the airbnb seems to be familiar for hosts and guests to use it on traveling possibilities and present a more unique, personalized way of experiencing the world. Today, Airbnb became one of a kind service that is used and recognized by most people in the world. Data analysis on millions of listings provided through Airbnb is a crucial factor for the company. These millions of listings generate a lot of data. That can be analyzed and used for security, business decisions, understanding of customers and providers'behavior, and performance on the platform, guiding marketing initiatives, implementation of innovative additional services, such as price, room type, minimum number of nights, and location. According to this dataset: https://raw.githubusercontent.com/bw-airbnb-2/DS/master/airbnb.csv. The total abservations is about 84438 and 14 columns.

## ☝️ **Pitch**

Using historical booking data from AirBnB, AirBnB Optimal Price will allow a user to predict the trends for optimal pricing for their properties based on variables such as location, time of year and other considerations. The user will be able to manage multiple properties at different locations and be able to make adjustments to their expectations for booking, as well as what they should be charging.

## ☝️ **Objective Goals**

- Train a predictive model on AirBnB `prices` using historical data.
- Make predictions accessible to the rest of the team. (Ex: deploy via a Flask API [or equivalent] to receive inputs (`location`, `size`, etc) and output predicted optimal `price` in JSON format.


## ☝️ **AirBNB Deployed Through Heroku:

https://airbnb-price-web-app.herokuapp.com/


## This DS Build Week Include The Followings:

- [Tech stack](#tech-stack)
- [Getting started](#getting-started)
- [File structure](#file-structure)
- [More instructions](#more-instructions)
- [Deploying to Heroku](#deploying-to-heroku)
- [Data visualization](#example-data-visualization)
- [Machine learning](#example-machine-learning)



## Tech stack
- [FastAPI](https://fastapi.tiangolo.com/): Web framework. Like Flask, but faster, with automatic interactive docs.
- [Flake8](https://flake8.pycqa.org/en/latest/): Linter, enforces PEP8 style guide.
- [Heroku](https://devcenter.heroku.com/): Platform as a service, hosts your API.
- [Pipenv](https://pipenv.pypa.io/en/latest/): Reproducible virtual environment, manages dependencies.
- [Plotly](https://plotly.com/python/): Visualization library, for Python & JavaScript.
- [Pytest](https://docs.pytest.org/en/stable/): Testing framework, runs your unit tests.

## Getting started

[Create a new repository from this template.](https://github.com/Lambda-School-Labs/ds-bw/generate)

Clone the repo
```
git clone https://github.com/bw-airbnb-2/DS

cd YOUR-REPO-NAME
```

Install dependencies
```
pipenv install --dev
```

Activate the virtual environment
```
pipenv shell
```

Launch the app
```
uvicorn app.main:app --reload
```

Go to `localhost:8000` in your browser.

![image](https://user-images.githubusercontent.com/7278219/87965040-c18ba300-ca80-11ea-894f-d51a69d52f8a.png)

You'll see your API documentation:

- Your app's title, "AirBnB Optimizing Price Predictor API"
- Your description, "Airbnb Optimizing Price"
- An endpoint for POST requests, `/predict`
- An endpoint for GET requests, `/viz/{location}`

Click the `/predict` endpoint's green button.

![image](https://user-images.githubusercontent.com/7278219/87965845-0532dc80-ca82-11ea-9690-b4c195a648d6.png)

You'll see the endpoint's documentation, including:

- Your function's docstring, """Make random baseline predictions for classification problem."""
- Request body example, as [JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON) (like a Python dictionary)
- A button, "Try it out"

Click the "Try it out" button.

![image](https://user-images.githubusercontent.com/7278219/87966677-39f36380-ca83-11ea-97f4-313bc11d3f19.png)

The request body becomes editable. 

Click the "Execute" button. Then scroll down.

![image](https://user-images.githubusercontent.com/7278219/87966896-948cbf80-ca83-11ea-9740-d0801148b1f3.png)

You'll see the server response, including:

- [Code 200](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200), which means the request was successful.
- The response body, as [JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON), with random baseline predictions for a classification problem.

***Your job is to replace these random predictions with real predictions from your model.*** Use this starter code and documentation to deploy your model as an API!

## File structure

```
.
└── app
    ├── __init__.py
    ├── main.py
    ├── api
    │   ├── __init__.py
    │   ├── predict.py
    │   └── viz.py    
    └── tests
        ├── __init__.py
        ├── test_main.py
        ├── test_predict.py
        └── test_viz.py
```

`app/app.py` is where you edit your app's title and description, which are displayed at the top of the your automatically generated documentation. This file also configures "Cross-Origin Resource Sharing", which you shouldn't need to edit. 

- [FastAPI docs - First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/)
- [FastAPI docs - Metadata](https://fastapi.tiangolo.com/tutorial/metadata/)
- [FastAPI docs - CORS](https://fastapi.tiangolo.com/tutorial/cors/)

`app/api/predict.py` defines the **Machine Learning** endpoint. `/predict` accepts POST requests and responds with random predictions. In a notebook, train your model and pickle it. Then in this source code file, unpickle your model and edit the `predict` function to return real predictions.

- [Scikit-learn docs - Model persistence](https://scikit-learn.org/stable/modules/model_persistence.html)
- [Keras docs - Serialization and saving](https://keras.io/guides/serialization_and_saving/)

When your API receives a POST request, FastAPI automatically parses and validates the request body JSON, using the `Item` class attributes and functions. Edit this class so it's consistent with the column names and types from your training dataframe. 

- [FastAPI docs - Request Body](https://fastapi.tiangolo.com/tutorial/body/)
- [FastAPI docs - Field additional arguments](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#field-additional-arguments)
- [calmcode.io video - FastAPI - Json](https://calmcode.io/fastapi/json.html)
- [calmcode.io video - FastAPI - Type Validation](https://calmcode.io/fastapi/type-validation.html)
- [pydantic docs - Validators](https://pydantic-docs.helpmanual.io/usage/validators/)

`app/api/viz.py` defines the **Visualization** endpoint. Currently `/viz/{statecode}` accepts GET requests where `{statecode}` is a 2 character US state postal code, and responds with a Plotly figure of the state's unemployment rate, as a JSON string. Create your own Plotly visualizations in notebooks. Then add your code to this source code file. Your web developer teammates can use [react-plotly.js](https://github.com/Lambda-School-Labs/labs-spa-starter/tree/main/src/components/pages/ExampleDataViz) to show the visualizations.

![react-plotly.js animation](https://media.giphy.com/media/j3QG8qVBQcpKvCfO3T/giphy.gif)

- [Lambda School docs - Data visualization with React & Plotly](https://github.com/Lambda-School-Labs/labs-spa-starter/tree/main/src/components/pages/ExampleDataViz). This is the code for the example above. Your web teammates can reuse this as-is.
- [Plotly docs](https://plotly.com/python/)


`app/tests/test_*.py` is where you edit your pytest unit tests. 

- [FastAPI docs - Testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [calmcode.io videos - FastAPI - Testing](https://calmcode.io/fastapi/testing-one.html)
- [calmcode.io videos - pytest](https://calmcode.io/pytest/introduction.html)

## More instructions

Activate the virtual environment
```
pipenv shell
```

Install additional packages
```
pipenv install PYPI-PACKAGE-NAME
```

Launch a Jupyter notebook
```
jupyter notebook
```

Run tests
```
pytest
```

Run linter
```
flake8
```

[calmcode.io videos - flake8](https://calmcode.io/flake8/introduction.html)

## Deploying to Heroku

Prepare Heroku
```
heroku login

heroku create YOUR-APP-NAME-GOES-HERE

heroku git:remote -a YOUR-APP-NAME-GOES-HERE
```

Deploy to Heroku
```
git add --all

git add --force Pipfile.lock

git commit -m "Deploy to Heroku"

git push heroku main:master

heroku open
```

<small>(If you get a `Locking failed!` error when deploying to Heroku or running `pipenv install` then delete `Pipfile.lock` and try again, without `git add --force Pipfile.lock`)</small>

Deactivate the virtual environment
```
exit
```


Test locally, then [deploy to Heroku](#deploying-to-heroku) with your work-in-progress. Get to this point by the middle of Build Week. (By Wednesday lunch for full-time cohorts. By end of week one for part-time cohorts.) Now your web teammates can make POST requests to your API endpoint.

In a notebook, train your pipeline and pickle it. See these docs:

- [Scikit-learn docs - Model persistence](https://scikit-learn.org/stable/modules/model_persistence.html)
- [Keras docs - Serialization and saving](https://keras.io/guides/serialization_and_saving/)

Get version numbers for every package you used in your pipeline. [Install the exact versions of these packages](#more-instructions) in your virtual environment.

Edit `app/api/predict.py` to unpickle your model and use it in your predict function. 

Now you are ready to re-deploy! 🚀

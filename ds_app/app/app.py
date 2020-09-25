from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from .api import predict, viz
#from .api.webapp import database

description = """
Deploys a logistic regression model fit on the [Palmer AirBnB](https://raw.githubusercontent.com/bw-airbnb-2/DS/master/airbnb.csv) dataset.

<img src="https://lh5.googleusercontent.com/-7EBrOOgWBhwF7TEZeICAdnAlCGU7GN29j1xC617Yrzxc0gzTZKtpvFbIYZ3PkESVLeBz6ius_ZEboiXRGjlR81QZgU3P4ZdmWjuzg0ArzeI-F1otytgHxByF2tFl6qdqEu35JXv" width="40%" />
"""


app = FastAPI(
    title='AirBnB Optimal Price Predictor API',
    description=description,
    version='0.1',
    docs_url='/',
)

app.include_router(predict.router)
app.include_router(viz.router)
#app.include_router(vis.router)
#app.include_router(database.router)

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex='https?://.*',
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if __name__ == '__main__':
    uvicorn.run(app)

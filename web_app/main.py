from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from fast.api import predict

app = FastAPI(
    title='airbnb ds api',
    description='',
    version='1.0'
    docs_url='/'
)

app.include_router(predict.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

if __name__ = '__main__':
    uvicorn.run(app)
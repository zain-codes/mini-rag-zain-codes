from fastapi import FastAPI, APIRouter
import os


#APIRouter is a class that helps to group related routes together
base_router = APIRouter( 
    prefix = "/api/v1",
    tags = ["api_v1"]
)

'''
# async is used to make the function asynchronous, it helps uvicorn to run the function in a separate thread which is 
more efficient when there are requests coming from multiple functions or many requests at the same time
'''
@base_router.get("/")
async ``def welcome(): 
    app_name = os.getenv('APP_NAME')
    app_version = os.getenv('APP_VERSION')

    return {
        "app_name": app_name,
        "app_version": app_version,
    }
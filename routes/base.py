from fastapi import FastAPI, APIRouter

base_router = APIRouter() #APIRouter is a class that helps to group related routes together


@base_router.get("/")
def welcome():
    return {
        "message": "Hello World"
    }
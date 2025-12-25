from fastapi import FastAPI #web framework
from routes import base

app = FastAPI()

app.include_router(base.base_router)




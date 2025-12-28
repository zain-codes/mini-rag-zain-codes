from fastapi import FastAPI #web framework
from dotenv import load_dotenv # order is important
load_dotenv()
from routes import base

app = FastAPI()

app.include_router(base.base_router)




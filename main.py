from fastapi import FastAPI #web framework
app = FastAPI()


@app.get("/welcome") #app as decorator to define a route
def welcome():
    return {
        "message": "Hello World"

    }



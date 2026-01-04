from fastapi import FastAPI

# 1. Create the 'app' instance (this is your API)
app = FastAPI()

# 2. Create a 'route'. This says: 
# "When someone visits the /hello folder of my website, run this function."
@app.get("/hello")
def say_hello():
    return {"message": "Hello from the FastAPI Brain!"}
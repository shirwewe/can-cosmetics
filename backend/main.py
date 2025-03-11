from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to Canadian Beauty Catalog API"}

# Sample brands endpoint
@app.get("/brands")
def get_brands():
    return {"brands": ["MAC", "Lise Watier", "Bite Beauty", "Vasanti"]}

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to KrishiYantra!"}

@app.get("/equipment")
def get_equipment():
    equipment_list = [
        {"id": 1, "name": "Tractor", "price_per_day": 1500, "location": "Guntur"},
        {"id": 2, "name": "Harvester", "price_per_day": 3000, "location": "Krishna"},
        {"id": 3, "name": "Sprayer", "price_per_day": 500, "location": "Gudivada"},
    ]
    return equipment_list

@app.get("/about")
def about():
    return {"app": "KrishiYantra", "version": "1.0", "developer": "Bharadwaj"}
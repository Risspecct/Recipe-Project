from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.services.spoonacular import request_spoonacular

router = APIRouter()


@router.get("/{id}/nutritions")
def get_nutrients(id: int):
    if id < 1:
        return HTTPException(status_code=400, detail="Invalid recipe id")
    response = request_spoonacular(f"/recipes/{id}/nutritionWidget.json")
    if response.status_code != 200:
        return JSONResponse(status_code=response.status_code, content={"error": "Could not fetch nutrition data"})
    data = response.json()
    if not data:
        return JSONResponse(status_code=404, content={"error": "No nutrition data found"})
    required_nutrients = ["Calories", "Fat", "Carbohydrates", "Sugar", "Cholesterol", "Protein", "Iron", "Calcium", "Fiber"]
    nutrition = [
        {nutrient["name"]: f"{nutrient['amount']}{nutrient['unit']}"}
        for nutrient in data.get("nutrients", [])
        if nutrient["name"] in required_nutrients
    ]
    return {"nutrition": nutrition}

from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from app.services.spoonacular import request_spoonacular

router = APIRouter()


@router.get("/")
def get_substitute(ingredient: str = Query(..., alias="ingredientName")):
    response = request_spoonacular("/food/ingredients/substitutes", {"ingredientName": ingredient})
    if response.status_code != 200:
        return JSONResponse(status_code=response.status_code, content={"error": "Could not fetch substitutes"})
    data = response.json()
    return {
        "message": data.get("message", "No message available"),
        "substitutes": data.get("substitutes", [])
    }

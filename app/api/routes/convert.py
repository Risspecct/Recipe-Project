from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from app.services.spoonacular import request_spoonacular

router = APIRouter()


@router.get("/")
def convert(
    ingredient: str = Query(..., alias="ingredientName"),
    sourceAmount: float = Query(..., ge=0),
    sourceUnit: str = Query("cups"),
    targetUnit: str = Query("grams")
):
    params = {
        "ingredientName": ingredient,
        "sourceAmount": sourceAmount,
        "sourceUnit": sourceUnit,
        "targetUnit": targetUnit,
    }
    response = request_spoonacular("/recipes/convert", params)
    if response.status_code != 200:
        return JSONResponse(status_code=response.status_code, content={"error": f"Couldn't fetch the converted amount {response.status_code}"})
    data = response.json()
    return {"ingredient": ingredient, "converted_amount": data["targetAmount"], "unit": data["targetUnit"], "formatted": f"{data['targetAmount']} {data['targetUnit']}"}

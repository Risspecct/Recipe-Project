from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.services.spoonacular import request_spoonacular

router = APIRouter()


@router.get("/")
def trivia():
    response = request_spoonacular("/food/trivia/random")
    if response.status_code != 200:
        return JSONResponse(status_code=response.status_code, content={"error": "Couldn't retrieve food trivia"})
    data = response.json()
    return {"Trivia": data["text"]}

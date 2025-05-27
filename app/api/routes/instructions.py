from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.services.spoonacular import request_spoonacular

router = APIRouter()


@router.get("/{id}/instructions")
def get_instructions(id: int):
    if id < 1:
        raise HTTPException(status_code=400, detail="Invalid recipe id")
    response = request_spoonacular(f"/recipes/{id}/analyzedInstructions")
    if response.status_code != 200:
        return JSONResponse(status_code=response.status_code, content={"error": "Could not fetch recipe instructions"})
    data = response.json()
    if not data or "steps" not in data[0]:
        return JSONResponse(status_code=404, content={"error": "No instructions found"})
    steps = data[0]["steps"]
    instructions = [f"{step['number']}. {step['step']}" for step in steps]
    return {"instructions": instructions}

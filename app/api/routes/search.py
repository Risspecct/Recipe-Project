from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse
from app.enums.cuisine import Cuisine
from app.enums.diet import Diet
from app.enums.intolerances import Intolerances
from app.enums.sort import Sort
from app.services.spoonacular import request_spoonacular

router = APIRouter()


@router.get("/")
def search(
    query: str = Query(default=None),
    ingredients: str = Query(default=None),
    cuisine: Cuisine = Query(default=None),
    diet: Diet = Query(default=None),
    intolerances: Intolerances = Query(default=None),
    sort: Sort = Query(default=None),
    page: int = Query(1, gt=0),
    page_size: int = Query(5, gt=0)
):
    offset = (page - 1) * page_size
    params = {
        "query": query,
        "includeIngredients": ingredients,
        "cuisine": cuisine,
        "diet": diet,
        "intolerances": intolerances,
        "sort": sort,
        "number": page_size,
        "offset": offset
    }
    response = request_spoonacular("/recipes/complexSearch", params)
    if response.status_code != 200:
        return JSONResponse(status_code=response.status_code, content={"error": "Could not load recipes"})
    data = response.json().get("results", [])
    recipes = [{"id": r["id"], "name": r["title"], "image": r["image"]} for r in data]
    if not recipes:
        return {"error": "No more recipes found"}
    return {"recipes": recipes}

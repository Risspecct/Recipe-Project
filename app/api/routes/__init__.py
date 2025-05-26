from fastapi import APIRouter

from .search import router as search_router
from .instructions import router as instructions_router
from .nutrition import router as nutrition_router
from .substitute import router as substitute_router
from .convert import router as convert_router
from .trivia import router as trivia_router

router = APIRouter()

router.include_router(search_router, prefix="/search", tags=["Search"])
router.include_router(instructions_router, prefix="/recipe", tags=["Instructions"])
router.include_router(nutrition_router, prefix="/recipe", tags=["Nutrition"])
router.include_router(substitute_router, prefix="/substitute", tags=["Substitute"])
router.include_router(convert_router, prefix="/convert", tags=["Convert"])
router.include_router(trivia_router, prefix="/trivia", tags=["Trivia"])

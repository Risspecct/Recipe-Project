from enum import Enum


class Diet(str, Enum):
    GLUTEN_FREE = "Gluten Free"
    WHOLE30 = "Whole30"
    LOW_FODMAP = "Low FODMAP"
    PRIMAL = "Primal"
    PALEO = "Paleo"
    PESCETARIAN = "Pescetarian"
    VEGAN = "Vegan"
    OVO_VEGETARIAN = "Ovo-Vegetarian"
    LACTO_VEGETARIAN = "Lacto-Vegetarian"
    VEGETARIAN = "Vegetarian"
    KETOGENIC = "Ketogenic"

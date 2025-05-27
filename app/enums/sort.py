from enum import Enum


class Sort(str, Enum):
    CHOLESTEROL = "Cholesterol"
    TOTAL_FAT = "Total Fat"
    ALCOHOL = "Alcohol"
    CAFFEINE = "Caffeine"
    ENERGY = "Energy"
    CARBS = "Carbs"
    CALORIES = "Calories"
    PRICE = "Price"
    TIME = "Time"
    HEALTHINESS = "Healthiness"
    POPULARITY = "Popularity"

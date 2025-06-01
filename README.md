# Recipe API

This FastAPI-based application provides a range of food-related functionalities such as recipe search, cooking instructions, nutritional analysis, ingredient conversions, substitutes, and food trivia. It uses the [Spoonacular API](https://spoonacular.com/food-api) under the hood.

> 🔪 **Note:** Weather-related files in this repository were used only for testing and are not part of the recipe API.

---

## 🔧 Features

* 🔍 Search recipes with filters (ingredients, cuisine, diet, etc.)
* 📖 Get step-by-step instructions for a recipe
* 🧮 Get detailed nutritional information
* 🔄 Convert ingredient quantities between units
* 🫒 Get ingredient substitutes
* 🎲 Get random food trivia

---

## 🚀 Getting Started

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create `.env` File

Create a `.env` file in the root directory with your Spoonacular API key:

```ini
SPOONACULAR_API_KEY=your_api_key_here
```

Make sure to add `.env` to your `.gitignore` file.

### Run the Server

```bash
uvicorn app.main:app --reload
```

### API Docs (Swagger UI)

Once the server is running, visit:

```
http://localhost:8000/docs
```

---

## 📂 Project Structure

```
└── risspecct-recipe-project/
    ├── README.md
    ├── requirements.txt
    ├── weather.html                  # For testing only
    ├── weather_app.py                # For testing only
    └── app/
        ├── main.py                   # FastAPI entry point
        ├── api/
        │   └── routes/
        │       ├── __init__.py
        │       ├── convert.py
        │       ├── instructions.py
        │       ├── nutrition.py
        │       ├── search.py
        │       ├── substitute.py
        │       └── trivia.py
        ├── enums/
        │   ├── cuisine.py
        │   ├── diet.py
        │   ├── intolerances.py
        │   └── sort.py
        └── services/
            └── spoonacular.py
```

---

## 📘 API Endpoints & Examples

### 1. **Search Recipes**

Search for recipes using keywords, ingredients, or filters like cuisine and diet.

**GET** `/search`

**Query Parameters:**

* `query` (optional)
* `ingredients` (optional)
* `cuisine`, `diet`, `intolerances` (optional)
* `sort` (optional)
* `page`, `page_size` (optional, default = 1 and 5)

**Example:**

```bash
curl "http://localhost:8000/search?query=pasta&cuisine=italian&page=1"
```

---

### 2. **Get Recipe Instructions**

Fetch detailed cooking instructions for a specific recipe.

**GET** `/recipe/{id}/instructions`

**Path Parameter:**

* `id` — Recipe ID

**Example:**

```bash
curl "http://localhost:8000/recipe/715538/instructions"
```

---

### 3. **Get Nutritional Information**

Retrieve nutritional breakdown (calories, protein, etc.) of a recipe.

**GET** `/recipe/{id}/nutritions`

**Path Parameter:**

* `id` — Recipe ID

**Example:**

```bash
curl "http://localhost:8000/recipe/715538/nutritions"
```

---

### 4. **Get Ingredient Substitutes**

Get recommended alternatives for a given ingredient.

**GET** `/substitute`

**Query Parameter:**

* `ingredientName` — Name of the ingredient

**Example:**

```bash
curl "http://localhost:8000/substitute?ingredientName=milk"
```

---

### 5. **Convert Ingredient Quantities**

Convert ingredient quantities between different measurement units.

**GET** `/convert`

**Query Parameters:**

* `ingredientName` (required)
* `sourceAmount` (required)
* `sourceUnit` (default: cups)
* `targetUnit` (default: grams)

**Example:**

```bash
curl "http://localhost:8000/convert?ingredientName=flour&sourceAmount=2&sourceUnit=cups&targetUnit=grams"
```

---

### 6. **Get Random Food Trivia**

Get a fun, random fact related to food.

**GET** `/trivia`

**Example:**

```bash
curl "http://localhost:8000/trivia"
```

---

## 💠 Error Handling

Returns standard HTTP error codes and JSON error messages.

**Example:**

```json
{
  "error": "Page and page_size must be positive integers"
}
```

---

## 📦 Dependencies

```
fastapi==0.115.2
uvicorn==0.29.0
requests==2.32.3
python-dotenv==1.0.1
pydantic==2.11.5
```

---

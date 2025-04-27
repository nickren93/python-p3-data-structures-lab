spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    #pass
    food_names = [key["name"] for key in spicy_foods]
    return food_names

def get_spiciest_foods(spicy_foods):
    #pass
    spiciest_foods = [key for key in spicy_foods if key["heat_level"] > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    #pass
    for key in spicy_foods:
        print(f"{key['name']} ({key['cuisine']}) | Heat Level: " + "🌶"*key['heat_level'])

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    #pass
    for key in spicy_foods:
        if key["cuisine"] == cuisine:
            return key

def print_spiciest_foods(spicy_foods):
    #pass
    print_spicy_foods(get_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    #pass
    total_spicy_level = 0
    for key in spicy_foods:
        total_spicy_level += key["heat_level"]
    average_heat_level = total_spicy_level / len(spicy_foods)
    return average_heat_level

def create_spicy_food(spicy_foods, spicy_food):
    #pass
    spicy_foods.append(spicy_food)
    return spicy_foods

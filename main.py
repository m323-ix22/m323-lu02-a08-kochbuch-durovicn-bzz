# Dein Code kommt hier hin
import json


def adjust_recipe(recipee, new_servingss):
    # Berechne den Faktor, mit dem die Mengen angepasst werden
    factor = new_servingss / recipee['servings']

    # Erstelle ein neues Dictionary mit den angepassten Zutatenmengen
    adjusted_ingredients = {ingredient: amount * factor for ingredient, amount in recipee['ingredients'].items()}

    # Rückgabe eines neuen Rezepts mit angepassten Zutaten und neuer Personenzahl
    return {
        'title': recipee['title'],
        'ingredients': adjusted_ingredients,
        'servings': new_servingss
    }


def load_recipe(recipe_jsonn):
    return json.loads(recipe_jsonn)


if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = ('{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, '
                   '"Minced Meat": 500}, "servings": 4}')
    # Dein Code kommt hier hin
    recipe = load_recipe(recipe_json)

    # Neue Anzahl an Personen
    new_servings = 2

    # Passe das Rezept an die neue Anzahl der Personen an
    adjusted_recipe = adjust_recipe(recipe, new_servings)

    # Ausgabe des angepassten Rezepts
    print("Originales Rezept:", recipe)
    print("Angepasstes Rezept für", new_servings, "Personen:", adjusted_recipe)

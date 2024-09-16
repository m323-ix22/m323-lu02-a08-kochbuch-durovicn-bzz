"""
Dieses Modul passt die Mengenangaben eines Rezepts an eine neue Anzahl von Personen an,
basierend auf einem JSON-String, der das Rezept darstellt. Es verwendet ausschließlich
Immutable Data und Pure Functions.
"""

import json


# Funktion zur Anpassung des Rezepts
def adjust_recipe(recipee, new_servingss):
    """
    Diese Funktion passt die Mengenangaben eines Rezepts an die neue Anzahl von Personen an.

    Args:
        recipee (dict): Das ursprüngliche Rezept als Python-Dictionary.
        new_servingss (int): Die neue Anzahl der Personen.

    Returns:
        dict: Ein neues Rezept-Dictionary mit angepassten Mengenangaben.
    """
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


# Funktion zum Laden eines Rezepts aus einem JSON-String
def load_recipe(recipe_jsonn):
    """
    Diese Funktion wandelt einen JSON-kodierten String in ein Python-Dictionary um.

    Args:
        recipe_jsonn (str): Der Rezept-String im JSON-Format.

    Returns:
        dict: Das Rezept als Python-Dictionary.
    """
    return json.loads(recipe_jsonn)


if __name__ == '__main__':
    # Beispiel für die Datenstruktur eines Rezepts
    recipe_json = ('{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, '
                   '"Minced Meat": 500}, "servings": 4}')

    # Lade das Rezept
    recipe = load_recipe(recipe_json)

    # Neue Anzahl an Personen
    new_servings = 2

    # Passe das Rezept an die neue Anzahl der Personen an
    adjusted_recipe = adjust_recipe(recipe, new_servings)

    # Ausgabe des angepassten Rezepts
    print('Originales Rezept:', recipe)
    print('Angepasstes Rezept für', new_servings, 'Personen:', adjusted_recipe)

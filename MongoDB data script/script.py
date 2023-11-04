# This is a sample Python script.
import datetime
import random

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from pymongo import MongoClient


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    client = MongoClient('localhost', 27017)
    db = client['test_is']

    base = datetime.datetime.today()
    date_list = [base - datetime.timedelta(weeks=x) for x in range(354)]

    foods = [
        ('Frutilla', 'Frutas'),
        ('Naranja', 'Frutas'),
        ('Ajo', 'Hortalizas'),
        ('Pimiento', 'Hortalizas'),
        ('Pollo Entero', 'Carnes'),
        ('Cordero', 'Carnes')
    ]
    collection = db['foods']
    for f in foods:
        collection.insert_one({
            "food_id": f[0],
            "group": f[1]
        })

    regions = [
        "Arica y Parinacota",
        "Coquimbo",
        "Valparaíso",
        "Metropolitana",
        "Maule",
        "Ñuble",
        "Biobío",
        "La Araucanía",
        "Los Lagos"
    ]

    food_docs = collection.find()
    collection = db['history']
    for f in food_docs:
        for r in regions:
            for d in date_list:
                collection.insert_one({
                    "region": r,
                    "price": random.randint(1, 8000),
                    "date": d,
                    "food_id": f.get('_id')
                })

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

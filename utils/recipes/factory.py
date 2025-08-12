import requests

from random import randint

from faker import Faker

def rand_ratio():
    return randint(840, 900), randint(473, 573)

fake = Faker("pt_BR")

def get_foodish_image_url():
    response = requests.get("https://foodish-api.com/api/")
    if response.status_code == 200:
        data = response.json()
        return data.get("image")
    return None

def make_recipe():
    return{
        "title": fake.sentence(nb_words=6),
        "description": fake.sentence(nb_words=12),
        "preparation_time": fake.random_number(digits=2, fix_len=True),
        "preparation_time_unit": "Minutos",
        "servings": fake.random_number(digits=2, fix_len=True),
        "servings_unit": "Porção",
        "preparation_steps": fake.date_time(),
        "created_at": fake.date_time(),
        "author": {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
        },
        "category": {
            "name": fake.word()
        },
        "cover": {
            # Nova URL com um ID de imagem aleatório do Lorem Picsum
            #"url": f"https://picsum.photos/id/{randint(1, 1000)}/{rand_ratio()[0]}/{rand_ratio()[1]}"
            "url": get_foodish_image_url() or "https://via.placeholder.com/800x600?text=Image+Unavailable"       
        }
    }

if __name__== "__main__":
    from pprint import pprint
    pprint(make_recipe)
# person_1 = {"first_name": "Billy", "last_name": "Smith", "city": "London"}
# person_2 = {"first_name": "Trevor", "last_name": "Falcon", "city": "Liverpool"}
# person_3 = {"first_name": "Sam", "last_name": "Jones", "city": "New York"}
#
# people = [person_1, person_2, person_3]
#
# for person in people:
#     print(person)

# pet_1 = {"name": "Lion", "color": "Grey", "favorite_food": "KFC"}
# pet_2 = {"name": "Panther", "color": "Black", "favorite_food": "Fish"}
# pet_3 = {"name": "Tiger", "color": "White", "favorite_food": "Deer"}
#
# pets = [pet_1, pet_2, pet_3]
#
# for pet in pets:
#     print(pet)

# favorite_places = {
#     "Bill": ["India", "France", "England"],
#     "Trevor": ["United States", "Ireland", "Spain"],
#     "Fred": ["Portugal", "Italy", "Greece"],
#      }
#
# for name, places in favorite_places.items():
#     print(f"\n{name.title()}'s favorite places are:")
#     for place in places:
#         print(f"\t{place.title()}")

# favorite_numbers = {
#     "Bill": [15, 19, 23],
#     "Trevor": [25, 35, 45],
#     "Fred": [47, 55, 75],
#      }
#
# for name, numbers in favorite_numbers.items():
#     print(f"\n{name.title()}'s favorite numbers are:")
#     for number in numbers:
#         print(f"\t{number}")

cities = {
    'London': {
        'Country': 'England',
        'Population': '9 million',
        'Fact': 'It has 12 professional football teams.',
         },

    'Madrid': {
        'Country': 'Spain',
        'Population': '7 million',
        'Fact': 'It has 3 professional football teams.',
         },

    'Berlin': {
        'Country': 'Germany',
        'Population': '4 million',
        'Fact': 'It has 2 professional football teams.',
        }

    }

for city, city_info in cities.items():
    country = city_info['Country'].title()
    population = city_info['Population']
    info = city_info['Fact'].title()

    print(f"\n{city.title()} is in {country}.")
    print(f"  It has a population of about {population}.")
    print(f"  The {info} mounats are nearby.")





















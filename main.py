"""app main"""
from src.get_person_data import get_name_and_age

try:
    person = get_name_and_age(112)
    print(
        f"Name: {person['name']}, Age: {person['age']}"
    )
except KeyError:
    print("Not a good user ID")

print("Hey")

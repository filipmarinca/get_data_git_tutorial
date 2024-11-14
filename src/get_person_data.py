"""Get person data"""

DATA = {
    111: {
        "name": "Daniel",
        "age": 20
    },
    112: {
            "name": "Maria",
            "age": 33
        }
}

def get_name_and_age(person_id):
    """Return person name and age"""
    return DATA[person_id]


if __name__ == "__main__":
    person = get_name_and_age(112)
    print(
        f"Name: {person['name']}, Age: {person['age']}"
    )
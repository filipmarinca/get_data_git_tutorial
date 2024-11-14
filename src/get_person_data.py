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

def save_data(file, person_data):
    """Save person data to file"""
    with open(file, "w") as fw:
        fw.write(person_data)

if __name__ == "__main__":
    try:
        person = get_name_and_age(112)
        print(
            f"Name: {person['name']}, Age: {person['age']}"
        )
    except KeyError:
        print("Not a good user ID")
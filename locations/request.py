LOCATIONS = [
    {
      "name": "The Hills (Seeing why other stuff isn't popping up right now)",
      "address": "417 Grateful Drive",
      "employeeId": 6,
      "animalId": 7,
      "id": 7
    },
    {
      "name": "Cairo ",
      "address": "123 Pyramid Avenue",
      "employeeId": 9,
      "animalId": 8,
      "id": 8
    },
    {
      "name": "East Nashville",
      "address": "Eastside",
      "employeeId": 9,
      "animalId": 9,
      "id": 9
    },
    {
      "name": "The Wild West",
      "address": "Optimistic Lane",
      "employeeId": 6,
      "animalId": 12,
      "id": 10
    }
  ]  

def get_all_locations():
    return LOCATIONS

# Function with a single parameter
def get_single_location(id):
    # Variable to hold the found animal, if it exists
    requested_location = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location = location

    return requested_location
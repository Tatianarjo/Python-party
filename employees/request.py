EMPLOYEES = [
    {
      "id": 1,
      "name": "Anna Lee",
      "locationId": 7
    },
    {
      "id": 2,
      "name": "Jaielle Michelle",
      "locationId": 8
    },
    {
      "id": 3,
      "name": "Rickema Lateefah",
      "locationId": 7
    },
    {
      "id": 4,
      "name": "Lessie Lacy",
      "locationId": 9
    },
]

def get_all_employees():
    return EMPLOYEES

# Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found animal, if it exists
    requested_employee = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
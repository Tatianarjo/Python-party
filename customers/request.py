CUSTOMERS = [
    {
      "id": 1,
      "name": "Hannah Hall",
      "address": "7002 Chestnut Ct",
      "email": "hannah@hall.com"
    },
    {
      "id": 2,
      "name": "Lindsay Vanderberg",
      "address": "584 10th Avenue",
      "email": "lindsay@vanderberg.com"
    },
    {
      "id": 3,
      "name": "Cherice Toliver",
      "address": "2021 East Main Street",
      "email": "cherice@cherice.com"
    }
]
# GET ALL CUSTOMERS AS AN ITERABLE LIST
# ----------------
def get_all_customers():
    return CUSTOMERS

# Function with a single parameter

# GET CUSTOMER BY ID
# ----------------
def get_single_customer(id):
    # Variable to hold the found animal, if it exists
    requested_customer= None


    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer
# CREATE CUSTOMER
# ----------------
def create_customer(customer):
  max_id = CUSTOMERS[-1]["id"]

  new_id = max_id + 1

  customer["id"] = new_id

  CUSTOMERS.append(customer)

  return customer
# DELETE CUSTOMER
# ----------------
def delete_customer(id):
  customer_index = -1

  for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

  if customer_index >= 0:
    CUSTOMERS.pop(customer_index)  

# UPDATE CUSTOMER
# ----------------
def update_customer(id, new_customer):
  for index, customer in enumerate(CUSTOMERS):
    if customer["id"] == id:
      CUSTOMERS[index] = new_customer
      break
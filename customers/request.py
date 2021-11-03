import sqlite3
import json

from models import Customer, customer

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
  # Open a connection to the database
  with sqlite3.connect("./kennel.db") as conn:

      # Just use these. It's a Black Box.
      conn.row_factory = sqlite3.Row
      db_cursor = conn.cursor()

      # Write the SQL query to get the information you want
      db_cursor.execute("""
      SELECT
          c.id,
          c.name,
          c.address,
          c.email
      FROM customer c
      """)

      # Initialize an empty list to hold all animal representations
      customers = []

      # Convert rows of data into a Python list
      dataset = db_cursor.fetchall()

      # Iterate list of data returned from database
      for row in dataset:

          # Create a customer instance from the current row.
          # Note that the database fields are specified in
          # exact order of the parameters defined in the
          # Customer class above.
          customer = Customer(row['id'], row['name'], row['address'],
                          row['email'])

          customers.append(customer.__dict__)

  # Use `json` package to properly serialize list as JSON
  return json.dumps(customers)

# Function with a single parameter

# GET CUSTOMER BY ID
# ----------------
# def get_single_customer(id):
#     # Variable to hold the found animal, if it exists
#     requested_customer= None


#     # Iterate the ANIMALS list above. Very similar to the
#     # for..of loops you used in JavaScript.
#     for customer in CUSTOMERS:
#         # Dictionaries in Python use [] notation to find a key
#         # instead of the dot notation that JavaScript used.
#         if customer["id"] == id:
#             requested_customer = customer

#     return requested_customer

def get_single_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email
        FROM customer c
        WHERE c.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        customer = Customer(data['id'], data['name'], data['address'],
                            data['email'])

        return json.dumps(customer.__dict__)

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

def get_customers_by_email(email):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)

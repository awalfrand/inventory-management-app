import csv
import os

def menu(username="@Aria", products_count=20):
    # this is a multi-line string, also using preceding `f` for string interpolation
    menu = f"""
    -----------------------------------
    INVENTORY MANAGEMENT APPLICATION
    -----------------------------------
    Welcome {username}!
    There are {products_count} products in the database.
        operation | description
        --------- | ------------------
        'List'    | Display a list of product identifiers and names.
        'Show'    | Show information about a product.
        'Create'  | Add a new product.
        'Update'  | Edit an existing product.
        'Destroy' | Delete an existing product.
    Please select an operation: """ # end of multi- line string. also using string interpolation
    return menu

def read_products_from_file(filename="products.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    print(f"READING PRODUCTS FROM FILE: '{filepath}'")
    products = []

    #TODO: open the file and populate the products list with product dictionaries
    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
        for row in reader:
            print(row["name"], row["price"])
            products.append(dict(row))

    return products

def write_products_to_file(filename="products.csv", products=[]):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    #print(f"OVERWRITING CONTENTS OF FILE: '{filepath}' \n ... WITH {len(products)} PRODUCTS")
    #TODO: open the file and write a list of dictionaries. each dict should represent a product.
    #done with above to-do

    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id", "name","aisle","department","price"])
        writer.writeheader()
        for p in products:
            writer.writerow(p)

def reset_products_file(filename="products.csv", from_filename="products_default.csv"):
    print("RESETTING DEFAULTS")
    products = read_products_from_file(from_filename)
    print(len(products))
    write_products_to_file(filename, products)

def auto_incremented_id(products):
    if len(products) == 0:
        return 1
    else:
        product_ids = [int(p["id"]) for p in products]
        return max(product_ids) + 1

def run():
    # First, read products from file...
    products = read_products_from_file()

    # Then, prompt the user to select an operation...
    number_of_products = len(products)
    my_menu = menu(username="@Aria", products_count=number_of_products)
    operation = input(my_menu)

    operation = operation.title()

    if operation == "List":
        print("LISTING PRODUCTS")
        for p in products:
            print(p["id"] + " " + p["name"])


    elif operation == "Show":
        print("SHOWING A PRODUCT")
        product_id = input("Please enter the Product ID of the product you wish to display: ")
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_products[0]
        print(matching_product)

    elif operation == "Create":
        new_id = auto_incremented_id(products)
        new_product = {
            "id": new_id
            new_name = input("Please enter the new product name: ")
            new_aisle = input("Please enter the new product aisle: ")
            new_department = input("Please enter the new product department: ")
            new_price = input("Please enter the new product price: ")
            "name": new_name
            "aisle": new_aisle
            "department": new_department
            "price": new_price
        }
        products.append(new_product)
        print("CREATING A NEW PRODUCT: ")
        print(new_id, new_name, new_aisle, new_department, new_price)

    elif operation == "Update":
        print("UPDATING PRODUCTS")
        product_id = input("Please input the Product ID of the item you'd like to update: ")
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_products[0]
        updated_aisle = input("Please input the new aisle: ")
        matching_product["aisle"] = updated_aisle
        updated_department = input("Please input the new aisle: ")
        matching_product["department"] = updated_department
        updated_price = input("Please input the new price: ")
        matching_product["price"] = updated_price

    elif operation == "Destroy":
        product_id = input("Please input the Product ID of the item you'd like to destroy: ")
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_products[0]
        del products[products.index(matching_product)]
        print("DELETING A PRODUCT")

    elif operation == "Reset":
        reset_products_file()

    else:
        print("Please select a valid option")
    #TODO instead of printing, capture user input

    # Then, handle selected operation: "List", "Show", "Create", "Update", "Destroy" or "Reset"...
    #TODO: handle selected operation

    # Finally, save products to file so they persist after script is done...
    write_products_to_file(products=products)

# only prompt the user for input if this script is run from the command-line
# this allows us to import and test this application's component functions
if __name__ == "__main__":
    run()

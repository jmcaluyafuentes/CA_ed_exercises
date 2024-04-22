def update_warehouse_product_database():
    warehouse_product_database = {
        "Xbox": 77,
        "PS5": 912,
        "Switch": 311,
        "Steam Deck": 51,
        "Valve Index": 102
    }
    todays_orders = {
        "Xbox": 12,
        "PS5": 112,
        "Switch": 310,
        "Steam Deck": 51,
        "Valve Index": 62
    }
    # Using todays orders update the warehouse product database.
    for product in warehouse_product_database.keys():
        left = warehouse_product_database[product] - todays_orders[product]
        warehouse_product_database[product] = left

    return warehouse_product_database

update_warehouse_product_database()

# WRITE YOUR FUNCTIONS HERE

# TEST_1
def get_pet_shop_name(shop):
    return shop["name"]


#TEST_2
def get_total_cash(cash_total):
    return cash_total["admin"]["total_cash"]


#TEST_3 & 4
def add_or_remove_cash(cash, amount):
    cash["admin"]["total_cash"] += amount


#TEST_5
def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]


#TEST_6
def increase_pets_sold(sold, amount):
    sold["admin"]["pets_sold"] += amount



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


#TEST_7
# def get_stock_count(count):
#     count = 0
#     for pet in "pets":
#         count += 1
#     return count


#TEST_8
def get_pets_by_breed(pets, breed_of_pet):
    breed_number = []
    for pet in pets["pets"]:
        if breed_of_pet == "breed":
            breed_number.append(pet)
    return breed_number
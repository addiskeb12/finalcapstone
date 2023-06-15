# this is the an example of phtyon program shows loop through list and dictionaries
total_stock = 0
menu = ["coffee", "tea", "juice", "snack"]

stock = {"coffee": 155,
         "tea": 234,
         "juice":98,
         "snack":124
}

price = {"coffee": 2.75,
         "tea": 2.10,
         "juice": 1.89,
         "snack": 1.10
         }
# itterates through menu list
for item in menu:
    item_value = (stock[item] * price[item])
    total_stock += item_value
print(f"Total stock of 4 product in our cafe worth £{total_stock:.2f}")
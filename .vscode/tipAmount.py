
def tip_amount(tip_percentage, total):
    return total * tip_percentage


def buy_produce(num_of_tomatoes, num_of_bananas, num_of_potatoes):
    total_price = num_of_tomatoes * 2.00 + num_of_bananas * 1.50 + num_of_potatoes * 3.00
    print("Welcome to Dev Branch Groceries")
    print("Today you bought: ")
    print(str(num_of_tomatoes) + "tomatoes")
    print(str(num_of_bananas) + "bananas")
    print(str(num_of_potatoes) + "potatoes")
    print("Your total is: $" + str(total_price))
    tips = tip_amount(0.15, total_price)
    print("Please tip me $" + str(tips))
    tips_more = tip_amount(0.5, total_price)
    print("If you're feeling rich, give me $" + str(tips_more))
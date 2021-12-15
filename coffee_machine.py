MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}





def is_resource_sufficient(order_ingredients):
    """returns the ingredient is insufficient to make a coffee"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """return the total calculted value of coin"""
    print("Please! enter the coin")
    total = int(input("how many quaters?:"))*0.25
    total += int(input("how many dime?:"))*0.1
    total += int(input("how many Nikel?:"))*0.05
    total += int(input("how many penny?:"))*0.01
    return total


def is_transaction_successful(money_received,drink_cost):
    """return True if the money is sufficient and False if the enter money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        global profit
        profit += drink_cost
        print(f"here is your change!{change}")
        return True
    else:
        print("sorry you dont have enough money!")
        return False


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"Money: {profit}")
        is_on = False
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            is_transaction_successful(payment, drink["cost"])




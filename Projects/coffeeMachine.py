
profit = 0

resource = {
    "water":500,
    "milk":200,
    "coffee":100,
    }


is_on  = True

while is_on:
    choice = input("What would you like to have? (Latte/Espresso/Cappccino)")
    if choice is "off":
        is_on = False
    elif choice is "report":
        print(f"Water = {resource["water"]}ml")
        print(f"Milk = {resource["milk"]}ml")
        print(f"Coffee = {resource["coffee"]}gm")
        print(f"Money Rs.{profit}")
        
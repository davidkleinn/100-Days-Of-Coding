from data import MENU
from data import resources

def generate_reports():
    """format and print the remaining resources in the coffee machine"""
    print(" ")
    print("========================================")
    print("RESOURCES LEFT:")
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]}')
    print("========================================")
    print(" ")

def check_resources(order_ingredients):
    """returns True if ingredients are enough, otherwise, returns false"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"not enough {item}.")
            return False
    return True

def payment():
             """returns the total calculated value the user is giving"""
             print(" ")
             quarters = int(input("How many quarters? "))
             dimes = int(input("How many dimes? "))
             nickels = int(input("How many nickels? "))
             pennies = int(input("How many pennies? "))

             total_quarters = quarters * 0.25
             total_dimes = dimes * 0.1
             total_nickels = nickels * 0.05
             total_pennies = pennies * 0.01
             total_value = total_quarters + total_dimes + total_nickels + total_pennies

             return total_value

def pay_check(payment_received, drink_cost):
     """return True when the payment is valid and calculates the change if needed, or False if not enough money"""     

     if payment_received >= drink_cost:
          change = round(payment_received - drink_cost, 2)
          print(" ")
          print(f"you received ${change} in change. ")
          resources["money"] += drink_cost

          # print(f"${resources["money"]}")
          return True
     else:
          print("not enough money to pay, you'll be refunded.\n")
          return False
                
def do_coffee(drink_name, order_ingredients):
     """deduct the order's ingredients from the machine resources"""
     for item in order_ingredients:
          resources[item] -= order_ingredients[item]
     print(" ")
     print(f"Here's your {drink_name}. Thank you and goodbye!")
     print(" ")
     
def coffee_machine():

    working = True
    while working:

        print("Welcome to the coffee machine system! please select the flavor you'd like the most!")
        print("1. Espresso: $1.5\n2. Latte: $2.5\n3. Cappuccino: $3.0")
        users_input = input("choose your flavor or type 'report' to show the machine's resources\n")

        if users_input == 'off':
            working = False
        elif users_input.strip() == 'report':
            generate_reports()
        else:
            flavor = MENU[users_input]
            
            # cost = flavor["cost"]
            # print(cost)
            if check_resources(flavor["ingredients"]):
                users_payment = payment()
                if pay_check(users_payment, flavor["cost"]):
                    do_coffee(users_input, flavor["ingredients"])
                    working = False

coffee_machine()
       
    
from list import menu,resources

def coffee(drink_name,order_intg):
    for item in order_intg:
        resources[item]-=order_intg[item]
    print(f"Here is your {drink_name}☕")
def ingridrents(order_intg):
    for item in order_intg:
        if order_intg[item]>=resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True
def money():
    print("Please insert coins")
    quater = float(input("How many quaters($0.25): "))
    dime = float(input("How many dimes($0.10): "))
    nickel = float(input("How many nickels($0.05): "))
    penny = float(input("How many pennies($0.01): "))
    amount=(0.25*quater)+(0.10*dime)+(0.05*nickel)+(0.01*penny)
    return amount
def transition(amount1):
    if menu[choice]["cost"]>amount1:
        print("Sorry that's not enough money. Money refunded")
        return False
    elif menu[choice]["cost"]<=amount1:
        global profit
        profit+=menu[choice]["cost"]
        change=amount1-menu[choice]["cost"]
        change1=round(change,2)
        print(f"Here is ${change1} dollars in change")
        return True

profit=0
machine_on = True
while machine_on:
    choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice=="off":
        machine_on=False
        break
    elif choice=="report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink=menu[choice]
        if ingridrents(drink["ingredients"]):
            payment=money()
            if transition(payment):
                coffee(choice,(drink["ingredients"]))


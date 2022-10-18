water = 400
milk = 540
beans = 120
cups = 9
money = 550


def coffee_mgs():
    print("I have enough resources, making you a coffee!")


def coffee_msg2():
    print("Sorry, not enough water!")


def status():
    print(f"""The coffee machine has:
{water} ml of water
{milk} ml of milk
{beans} g of coffee beans
{cups} disposable cups
${money} of money""")


def checker():
    if water > 0 and milk > 0 and beans > 0 and money > 0 and cups > 0:
        return True
    else:
        return False


while True:
    action = input("Write action (buy, fill, take, remaining, exit)\n")
    if action == "fill":
        water += int(input("Write how many ml of water you want to add: "))
        milk += int(input("Write how many ml of milk you want to add: "))
        beans += int(input("Write how many grams of coffee beans you want to add: "))
        cups += int(input("Write how many disposable cups you want to add: "))

    elif action == "buy":
        buy = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
        if buy == "1":
            water -= 250
            beans -= 16
            money += 4
            cups -= 1
            if checker():
                coffee_mgs()
            else:
                water += 250
                beans += 16
                money -= 4
                cups += 1
                coffee_msg2()
        elif buy == "2":
            water -= 350
            milk -= 75
            beans -= 20
            money += 7
            cups -= 1
            if checker():
                coffee_mgs()
            else:
                water += 350
                milk += 75
                beans += 20
                money -= 7
                cups += 1
                coffee_msg2()
        elif buy == "3":
            water -= 200
            milk -= 100
            beans -= 12
            money += 6
            cups -= 1
            if checker():
                coffee_mgs()
            else:
                water += 200
                milk += 100
                beans += 12
                money -= 6
                cups += 1
                coffee_msg2()
        elif buy == "back":
            pass

    elif action == "take":
        print(f"I gave you ${money}")
        money = 0


    elif action == "remaining":
        status()

    elif action == "exit":
        break
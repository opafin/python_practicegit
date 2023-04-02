import os

def coffee_shop():

    from coffee_dicts import MENU, resources, coin_types, units, cost

    def calculate_coins(coin_list):
        coin_list = list(map(int, coin_list))
        coin_value = [0.25, 0.10, 0.05, 0.01]
        for i in range(0, len(coin_list)):
            coin_list[i] = coin_list[i] * coin_value[i]
        return (sum(coin_list))

    def manage_resources(ingredient):

        for item in ingredient:
            if ingredient[item] > resources[item]:
                print("* internal screech *")
                return False
        return True

    def successfull_transaction(ingredient, choice):
        for item in ingredient:
            resources[item] -= ingredient[item]
        resources['money'] += cost[choice]
        return

    def get_report():
        os.system('cls')
        for item in resources:
            print(f"{item}: {resources[item]} {units[item]} ")
        input("done viewing?")
        ai_service()

    def order_more():
        more = input("more coffee? y|n\n")
        if more == 'report':
            get_report()
        if more == 'y':
            ai_service()
        else:
            exit()

    def ai_service():

        total_coins = []
        transaction_completed = False

        os.system('cls')
        print("**Welcome to the coffee shop!**")
        print()
        for index, item in enumerate(MENU):
            print(f"{index} {item}, {cost[item]} $")
        print()

        request = input("what would you like? (0, 1, 2): ")
        if request == 'report':
            get_report()
        else:
            choice = list(MENU)[int(request)]
            ingredient = MENU[choice]

        os.system('cls')
        if manage_resources(ingredient):
            print(f"{cost[choice]} $ for {choice} please\n")
        else:
            print("Sorry we've ran out of ingredients!\n")
            order_more()

        for coin in coin_types:
            coin = input(
                f"insert {coin}, or just hit enter\n")
            if coin == 'report':
                answer = input(
                    "why do you want a report now? just get your coffee!")
                if answer == 'report':
                    get_report()
                else:
                    ai_service()
            if coin != '':
                total_coins.append(coin)
                total_value = calculate_coins(total_coins)
                os.system('cls')
                print(
                    f"you've inserted a total of {round(total_value, 2)} $")
                if total_value == cost[choice]:
                    print(f"that's exactly what's needed for {choice}")
                elif total_value > cost[choice]:
                    overhead = total_value - cost[choice]
                    print(f"that's {overhead} $ over, here's your change")
                if total_value == cost[choice] or total_value > cost[choice]:
                    print("Enjoy your coffee!")
                    transaction_completed = True
                    successfull_transaction(ingredient, choice)
                    break
                else:
                    print(f"that's {round(total_value - cost[choice], 2)} $ short, do you have some more coins?")

        if transaction_completed == False and total_coins:
            print(f"bummer, that's not enough, here are your coins: {round((total_value), 2)}")
        elif transaction_completed == False:
            print("\nyou have got to insert some coins, buddy")

        order_more()

    ai_service()

coffee_shop()

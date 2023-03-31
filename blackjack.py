import random


def blackjack():
    from art import blackjack_logo
    print(blackjack_logo)

    def draw_cards_to(hand):
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        hand.append(cards[random.randint(0, 12)])

    def flip_ace_in(hand):
        ace = hand.index(11)
        hand[ace] = 1

    def draw_the_table():
        # print(sum(dealers_hand)
        # print(dealers_hand)
        print(table)
        print(your_hand)
        print(sum(your_hand))
        print("------------")

    def choose_actions():

        while sum(your_hand) < 21 or 11 in your_hand and sum(your_hand) != 21:

            draw_the_table()

            if 11 in your_hand:
                choice = input(
                    "to flip an ace send 'f' to hit send 'h', or just press enter to continue: ")
                if choice == 'f':
                    flip_ace_in(your_hand)
                    continue
                if choice == 'h':
                    draw_cards_to(your_hand)
                    continue
                else:
                    return
            else:
                choice = input(
                    "to hit send 'h' or just press enter to continue: ")
                if choice == 'h':
                    draw_cards_to(your_hand)
                    continue
            return
        else:
            return

    def end_scenario():
        draw_the_table()
        if sum(your_hand) == 21:
            print("A Blackjack!!")
        while sum(dealers_hand) < 17:
            draw_cards_to(dealers_hand)
            if sum(dealers_hand) > 21 and 11 in dealers_hand:
                flip_ace_in(dealers_hand)
            for i in range(len(dealers_hand) - len(table)):
                table.append("[ ]")
            if sum(dealers_hand) < 17:
                table.append("[ ]")
            for i in range(1, len(dealers_hand)):
                table[i] = (f"[{dealers_hand[i]}]")
            print("********************")
            input("ready to see the dealer's next card?")
            print("********************")
            print(sum(dealers_hand))
            draw_the_table()

    def calculate_score():
        print(f"the dealer got {sum(dealers_hand)}")
        print(f"you got {sum(your_hand)}")
        if sum(your_hand) > 21 and sum(dealers_hand) > 21:
            print("You both bust!")
        elif sum(dealers_hand) > 21 or sum(your_hand) <= 21 and sum(your_hand) > sum(dealers_hand):
            print("You won!")
        elif sum(your_hand) == sum(dealers_hand):
            print("It's a draw!")
        else:
            print("You lost!")

    dealers_hand = []
    draw_cards_to(dealers_hand)

    table = [f"[{dealers_hand[0]}]", "[ ]"]

    your_hand = []
    while len(your_hand) < 2:
        draw_cards_to(your_hand)

    choose_actions()
    end_scenario()
    calculate_score()

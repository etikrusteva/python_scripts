#!/usr/bin/env python3


def disc():
    print("""Please type in the next lines the information for your ticket:
    Are you with child?
    Have you discount for loyal client?
    Have you bonus giftcard?
    \nNote that you can use only one discount and you use only the giftcard bonus if you have it! \n""")

    child = input("Are you with child? ")
    card = input("Have you discount for loyal client? ")
    bonus = input("Have you bonus giftcard? ")


    def discount1(bonus):
        return 0.15

    def discount2(card):
        return 0.25

    def discount3(child):
        return 0.10

    def price():
        return 10

    if bonus == "Yes" or bonus == "yes" or bonus == "YES":
        result = discount1(bonus)

    elif bonus == "No" or bonus == "no" or bonus == "NO":
        result = 1

    elif child == "Yes" or child == "yes" or child == "YES":
        result = discount3(child)

    elif child == "No" or child == "no" or child == "NO":
        result = 1

    elif card == "Yes" or card == "yes" or card == "YES":
        result = discount2(card)

    elif card == "No" or card == "no" or card == "NO":
        result = 1

    else:
        result = 1


    print("\nYour discount is: ",result)
    print("Your discount is: ", result*price(),"$")
    print("The price of your ticket is: ", price() - (result*price()), "$")

if __name__ == "__main__":
    disc()

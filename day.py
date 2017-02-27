#!/usr/bin/env python3

def weekdays():
    print("Please type Number from 1 to 7 - which day of the week is today:")
    today = input("Number:")
    today = int(today)

    def Monday(today):
        return "Monday"

    def Thuesday(today):
        return "Thuesday"

    def Wednesday(today):
        return "Wednesday"

    def Thursday(today):
        return "Thursday"

    def Friday(today):
        return "Friday"

    def Sunday(today):
        return "Sunday"

    def Saturday(today):
        return "Saturday"

    if today > 7 or today <1:
        print("Sorry, the days of the week are only 7!")
    elif today <7 and today >1:

        if today == 1:
            result = Monday(today)

        elif today == 2:
            result = Thuesday(today)

        elif today == 3:
            result = Wednesday(today)

        elif today == 4:
            result = Thursday(today)

        elif today == 5:
            result = Friday(today)

        elif today == 6:
            result = Sunday(today)

        elif today == 7:
            result = Saturday(today)

        print("Today is", result, "and it's a beautiful day!")


if __name__ == "__main__":
    weekdays()


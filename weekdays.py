def weekdays():
    print("Please type Number from 1 to 7 - which day of the week is today:")
    today = input("Number:")
    today = int(today)


    if today == "1":
        result = "Monday"

    elif today == "2":
        result = Thuesday

    elif today == "3":
        result = Wednesday

    elif today == "4":
        result = Thursday

    elif today == "5":
        result = Friday

    elif today == "6":
        result = Sunday

    elif today == "7":
        result = Saturday


    print("Today is", result)

if __name__ == "__main__":
    weekdays()

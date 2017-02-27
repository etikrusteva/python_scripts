#!/usr/bin/env python3

def g():
    print("""Please type your scores from your exams:
     \nEach exam makes 50 points. You can have maximum 100 points from both exams.
     \nFor grade A you should have over 90 points and the minimum of 20 points is for Lowest score.\n""")

    exam1 = input("Provide your score from exam 1: ")
    exam2 = input("Provide your score from exam 2: ")
    exam1 = int(exam1)
    exam2 = int(exam2)
    points = (int(exam1 + exam2))

   # if points >=100 or points <=20:
       # print("Scores not valid. Enter again.")

    def A(points):
        return "Otlichen 6"

    def B(points):
        return "Mnogo dobar 5"

    def C(points):
        return "Dobar 4"

    def D(points):
        return "Sreden 3"

    def E(points):
        return "Slab 2"

    if points > 100 or points <20:
        print("Sorry, invalid score.")
    elif points < 100 and points >20:

        if exam1 + exam2 >= 90 and exam1 + exam2 <= 100:
            result = A(points)

        elif exam1 + exam2 >= 75:
            result = B(points)

        elif exam1 + exam2 >= 50:
            result = C(points)

        elif exam1 + exam2 >= 35:
            result = D(points)

        elif exam1 + exam2 >= 20:
            result = E(points)

        print("\nThank you! Your result is {0}. Youre grade is {1}.".format(points,result))

#elif exam1 + exam2 > 100 and exam1 + exam2 < 20:
#print("That is not a correct result! Please check your exam scores again! ")

if __name__ == "__main__":
    g()

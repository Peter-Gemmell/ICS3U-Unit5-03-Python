#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on May 2022
# This program turns grades into percentage


def grade_to_percentage(grade_level):
    # turns grade into percentage

    if grade_level == "4+":
        grade_percentage = 97

    elif grade_level == "4":
        grade_percentage = 90

    elif grade_level == "4-":
        grade_percentage = 83

    elif grade_level == "3+":
        grade_percentage = 78

    elif grade_level == "3":
        grade_percentage = 75

    elif grade_level == "3-":
        grade_percentage = 71

    elif grade_level == "2+":
        grade_percentage = 68

    elif grade_level == "2":
        grade_percentage = 65

    elif grade_level == "2-":
        grade_percentage = 61

    elif grade_level == "1+":
        grade_percentage = 58

    elif grade_level == "1":
        grade_percentage = 55

    elif grade_level == "1-":
        grade_percentage = 51

    elif grade_level == "R":
        grade_percentage = 30

    else:
        grade_percentage = -1

    return grade_percentage


def main():

    user_grade_level = input("Enter the grade you would like to convert to % : ")

    grade_Percentage = grade_to_percentage(user_grade_level)  # call function

    if grade_Percentage == -1:  # error check
        print("ERROR, invalid input.")
    else:
        print(
            "The middle percentage of the grade {} is {}%.".format(
                user_grade_level, grade_Percentage
            )
        )

    print("\nDone.")


if __name__ == "__main__":
    main()

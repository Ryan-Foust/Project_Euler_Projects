#!/usr/bin/python3

def main():
    # COUNT INSTANCES OF 1-9
    total = 0  # keep the running total

    # for each 1 found, add another 3 characters
    total += (3 * 9)  # once for each set of 10 numbers (except for 11), up to 100
    total += (3 * 100)  # once for each number that starts with "one hundred" (100-199)
    total += (3 * 1)  # once for "one thousand" (1000)

    # for each 2 found, add another 3 characters
    total += (3 * 9)  # once for each set of 10 numbers (except for 12), up to 100
    total += (3 * 100)  # once for each number that starts with "two hundred" (200-299)

    # for each 3 found, add another 5 characters
    total += (5 * 9)  # once for each set of 10 numbers (except for 13), up to 100
    total += (5 * 100)  # once for each number that starts with "three hundred" (300-399)

    # for each 4 found, add another 4 characters
    total += (4 * 9)  # once for each set of 10 numbers (except for 14), up to 100
    total += (4 * 100)  # once for each number that starts with "four hundred" (400-499)

    # for each 5 found, add another 4 characters
    total += (4 * 9)  # once for each set of 10 numbers (except for 15), up to 100
    total += (4 * 100)  # once for each number that starts with "five hundred" (500-599)

    # for each 6 found (except for 16), add another 3 characters
    total += (3 * 9)  # once for each set of 10 numbers (except for 16), up to 100
    total += (3 * 100)  # once for each number that starts with "six hundred" (600-699)

    # for each 7 found, add another 5 characters
    total += (5 * 9)  # once for each set of 10 numbers (except for 17), up to 100
    total += (5 * 100)  # once for each number that starts with "seven hundred" (700-799)

    # for each 8 found, add another 5 characters
    total += (5 * 9)  # once for each set of 10 numbers (except for 18), up to 100
    total += (5 * 100)  # once for each number that starts with "eight hundred" (800-899)

    # for each 9 found, add another 4 characters
    total += (4 * 9)  # once for each set of 10 numbers (except for 19), up to 100
    total += (4 * 100)  # once for each number that starts with "nine hundred" (900-999)


    # COUNT INSTANCES OF 10-19

    # for each 10 found, add another 3 characters
    total += (3 * 10)  # once for each set of 100

    # for each 11 found, add another 6 characters
    total += (6 * 10)  # once for each set of 100

    # for each 12 found, add another 6 characters
    total += (6 * 10)  # once for each set of 100

    # for each 13 found, add another 8 characters
    total += (8 * 10)  # once for each set of 100

    # for each 14 found, add another 8 characters
    total += (8 * 10)  # once for each set of 100

    # for each 15 found, add another 7 characters
    total += (7 * 10)  # once for each set of 100

    # for each 16 found, add another 7 characters
    total += (7 * 10)  # once for each set of 100

    # for each 17 found, add another 9 characters
    total += (9 * 10)  # once for each set of 100

    # for each 18 found, add another 8 characters
    total += (8 * 10)  # once for each set of 100

    # for each 19 found, add another 8 characters
    total += (8 * 10)  # once for each set of 100


    # COUNT INSTANCES OF MULTIPLES OF 10 (20, 30, 40, 50, 60, 70, 80, 90)

    # for each 20 found, add another 6 characters
    total += ((6 * 10) * 10)  # once for each set of 20-29 in each set of 100

    # for each 30 found, add another 6 characters
    total += ((6 * 10) * 10)  # once for each set of 30-39 in each set of 100

    # for each 40 found, add another 5 characters
    total += ((5 * 10) * 10)  # once for each set of 40-49 in each set of 100

    # for each 50 found, add another 5 characters
    total += ((5 * 10) * 10)  # once for each set of 50-59 in each set of 100

    # for each 60 found, add another 5 characters
    total += ((5 * 10) * 10)  # once for each set of 60-69 in each set of 100

    # for each 70 found, add another 7 characters
    total += ((7 * 10) * 10)  # once for each set of 70-79 in each set of 100

    # for each 80 found, add another 6 characters
    total += ((6 * 10) * 10)  # once for each set of 80-89 in each set of 100

    # for each 90 found, add another 6 characters
    total += ((6 * 10) * 10)  # once for each set of 90-99 in each set of 100


    # COUNT INSTANCES OF "HUNDRED"

    # for each instance found, add another 7 characters
    total += ((7 * 100) * 9)  # once for each of 100-999


    # COUNT INSTANCE OF "THOUSAND"

    # add 8 characters for the one use of "thousand"
    total += (8 * 1)

    print(total)


if __name__ == '__main__':
    main()

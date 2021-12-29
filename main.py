def divRecur(a, b):  # recursively divides
    if a < b:  # base case
        return 0  # if the first parameter is less then the second, program returns 0
    return 1 + divRecur(a - b, b)  # calculates division without / by continuously subtracting from the first parameter and adding one on the outside


def modRecur(a, b):  # recursively finds the remainder of division
    if b > a:  # base case
        return a  # returns first parameter if first parameter is greater then second
    return modRecur(a - b, b)  # continuously subtracts on first parameter until the program reaches the remainder


def is5saPower(n):  # recursively finds if the number is a power of 5
    if n < 5:  # checks to see if the number is less then 5 first
        return False
    if n % 5 != 0:  # checks to see if the number can be evenly divided by 5
        return False
    if n == 5:  # checks to see if the number is 5
        return True
    return is5saPower(n / 5)  # continuously divides by 5 and checks the if statements above


def main():  # contains the menu
    counter = True
    while counter:  # continuously reruns the menu after each function run
        print("Select from: ")
        print("1. Division")
        print("2. Finding Remainder")
        print("3. Finding if a number is a power of 5")
        print("0. Exit")

        counter = int(input("Enter the option number: "))  # user input to determine which function to run or to exit
        if counter == 1:  # runs division if user inputs 1
            x1 = int(input("Enter number1 x: "))  # first parameter input
            y1 = int(input("Enter number2 y: "))  # second parameter input
            print(f"The quotient is {divRecur(x1, y1)}")
        elif counter == 2:  # runs find remainder if user inputs 2
            x2 = int(input("Enter x2: "))  # first parameter input
            y2 = int(input("Enter y2: "))  # second parameter input
            print(f"The remainder is {modRecur(x2, y2)}")
        elif counter == 3:  # finds if the number is a power of five is user inputs 3
            n = int(input("Enter a number: "))  # parameter for following function run
            if is5saPower(n):  # if the function returns true then the number is a power of 5
                print(n, "is a power of 5")
            if not is5saPower(n):  # if the function returns false then the number is not a power of five
                print(n, "is not a power of 5")
        elif counter == 0:  # exits program if user inputs 0
            print("Goodbye!")
        else:
            print("Invalid Input")  # if user puts in a incorrect input, lets them know
        print()


if __name__ == '__main__':
    main()

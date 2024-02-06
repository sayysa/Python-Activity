def again():
    print("\nDo you want to try again?")
    print("[0] Yes")
    print("[1] No")

    answer = input("Enter Choice: ")

    if answer == '0':
        main()
        calculate()

    elif answer == '1':
        exit()

    else:
        print("Invalid Choice. Select 0 or 1 only.")
        again()


def calculate():
    print("\nSelect Operation")
    print("[1] ADD")
    print("[2] SUBTRACT")
    print("[3] MULTIPLY")
    print("[4] DIVIDE")
    print("[5] EXIT")

    choice = input("Enter Choice: ")

    if choice == '1':
        result = num1 + num2
        print("Result is", result)
        again()

    elif choice == '2':
        result = num1 - num2
        print("Result is", result)
        again()

    elif choice == '3':
        result = num1 * num2
        print("Result is", result)
        again()

    elif choice == '4':
        if num2 == 0:
            print("Cannot divide by zero. Please choose a non-zero divisor.")
            again()
        else:
            result = num1 / num2
            print("Result is", result)
            again()

    elif choice == '5':
        exit()

    else:
        print("\nInvalid Choice. Select 1-5 only.")
        calculate()
        print("test push")
        
def main():
    global num1, num2
    print("\nBasic Calculator")

    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))
    calculate()

main()


import os

def again():
    print("\nDo you want to try again?")
    print("[0] Yes")
    print("[1] No")

    answer = input("\nEnter Choice: ")

    if answer == '0':
        main()

    elif answer == '1':
        exit()

    else:
        print("Invalid Choice. Select 0 or 1 only.")
        again()

def determine_parity():
    if num % 2 == 0:
        print(num, "is an EVEN number.")
        again()

    elif num % 2 != 0:
        print(num, "is an ODD number.")
        again()

    else:
        print("Invalid Choice. Select 0 or 1 only.")
        again()

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    global num
    print("\nOdd or Even?")

    num = float(input("\nEnter your number: "))

    determine_parity()

main()
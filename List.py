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

def get_average(myList):
    return sum(myList) / len(myList)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    rawList = input("Enter elements of the list (numerical values only): ")

    """
    myList = rawList.split()
    myList = [int(num) for num in myList]
    """
    
    try:
        myList = [int(num) for num in rawList.split()]
    except ValueError:
        print("Invalid input. Please enter numerical values only.")
        main()

    ave = get_average(myList)

    print("List: ", myList)
    print("Length of List: ", len(myList))
    print("Sum of List: ", sum(myList))
    print("Average of List: ", round(ave, 2))

    again()
main()

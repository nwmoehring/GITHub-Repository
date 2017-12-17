def ODD_EVEN():
    x = input("Enter Number:  ")
    try:
        y = int(x) % 2
    except ValueError:
        print("Input must be an integer.")
        return

    if y == 0:
        print("The number is even.")
    else:
        print("The number is odd")

ODD_EVEN()

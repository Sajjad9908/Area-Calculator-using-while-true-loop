while True:
    print("*" * 10, "The Area Calculator", "*" * 10)
    choice = int(input("Enter the choice between 1-4: "))

    if choice == 1:
        while True:
            side = int(input("Enter the value of side: "))
            area = side ** 2
            print("Area of square =", area)
            repeat = input("Do you want to repeat yes/no: ")
            if repeat == "no" or repeat == "NO":
                break

    elif choice == 2:
        while True:
            base = float(input("Enter the base of a triangle: "))
            height = float(input("Enter the height of a triangle: "))
            area = 0.5 * height * base
            print("The area of triangle =", area)
            repeat = input("Do you want to repeat yes/no: ")
            if repeat == "no" or repeat == "NO":
                break

    elif choice == 3:
        while True:
            r = float(input("enter the radious of circle"))
            area = 3.142 * r**2
            print("area of circle==", area)
            repeat = input("Do you want to repeat yes/no: ")
            if repeat == "no" or repeat == "NO":
                break

    elif choice == 4:
        while True:
            length = float(input("enter the length of rectangle"))
            width = float(input("enter the width of rectangle"))
            area = length * width
            print("the area of rectangle=")
            repeat = input("do you want to repeat yes/no ??")
            if repeat == "no" or repeat == "NO":
                break



    repeat1 = input("Do you want to perform another calculation? yes/no: ")
    if repeat1 == "no" or repeat1 == "NO":
        break

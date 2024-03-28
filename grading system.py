while True:
    marks = int(input("Enter marks (or enter -1 to exit): "))
    if marks == -1:
        break
    elif marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: A-")
    elif marks >= 70:
        print("Grade: B+")
    elif marks >= 60:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C+")
    elif marks >= 40:
        print("Grade: C")
    else:
        print("Grade: F")

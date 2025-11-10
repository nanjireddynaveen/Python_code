#Largest of the 3 numbers:
def large_number(x, y, z):
    if x > y and x > z:
        print("X is the larest number")
    elif y > z and y  > x:
        print("Y is the laregest number")
    elif z > y and z > x:
        print("Z is the larest number")
    else:
        print("All the number are equal")

# smallest of the 3 numbers:
def small_number(x, y , z):
    if x < y and x < z:
        print("X is the smallest number")
    elif y < z and y < x:
        print("Y is the smallest number")
    elif z < x and z < y:
        print("Z is the smallest number")
    else:
        print("All the numbers are equal")


# Input from user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if __name__ == "__main__":
    # Function calls
    large_number(num1, num2, num3)
    small_number(num1, num2, num3)
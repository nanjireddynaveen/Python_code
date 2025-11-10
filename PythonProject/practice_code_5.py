# Sum of Elements
def sum_elements(numbers):
    numbers =  [int(x) for x in numbers.split(",")]
    print("numbers split",numbers)
    total = sum(numbers)
    print("Sum of the total numbers is: ", total)


if __name__ == "__main__":
    numbers = input("Enter the numbers: ")
    sum_elements(numbers)
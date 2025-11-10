# Largest number in the list
def largest_number(numbers):
    numbers = [int (x) for x in numbers.split(",")]
    print("##### #####", numbers)
    print("Largest number is", max(numbers))

if __name__ == "__main__":
    numbers = input("Enter the numbers: ")
largest_number(numbers)
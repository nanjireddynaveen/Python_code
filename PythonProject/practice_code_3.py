# Print multiplication table
def multiplication_table(x):
    for i in range(1, 11):
        print(f"{x} x {i} = {x * i}")

number = int(input("Enter the number for table: "))

# Find the largest number
def largest_num(numbers):
    numbers = [int (x) for x in numbers.split(",")]
    print("###########", numbers)
    print("Largest number is", max(numbers))

user_input = input("Enter the numbers")
if __name__ == "__main__":
    #multiplication_table(number)
    largest_num(user_input)

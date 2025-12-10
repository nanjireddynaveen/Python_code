#sum of the numbers
def sum_numbers(numbers):
    numbers_int = [ int(x) for x in numbers.split(",")]
    print("numbers print", numbers_int)
    total = sum(numbers_int)
    print("Print the total : ", total)

if __name__ == "__main__":
    numbers = input("input number:")
    sum_numbers(numbers)

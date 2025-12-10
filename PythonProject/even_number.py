#check if the num is even

def even_check(num):
    if num % 2 == 0:
        print("number is even =>", num)
    else:
        print("number is odd =>", num)

if __name__ == "__main__":
    num = int(input("Enter the num: "))
    even_check(num)
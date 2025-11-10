# Palindrome check
def palindrome_check(string):
    string = string.strip()
    if string == string[::-1]:
        print("String is palindrome")
    else:
        print("String is not palindrome")

def reverse_string(s):
    print("Print the string in reverse order: ", s[: : -1])
if __name__ == "__main__":
    string = input("enter string: ")
    palindrome_check(string)
    reverse_string(string)
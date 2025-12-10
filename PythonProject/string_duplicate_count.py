def check_string(string):
    print("###### => ",string)
    if not string:
        return 0
    n = len(string)
    count = 0
    s = list(string)
    for i in range(1, n):
        if s[i] == s[i-1]:
            count += 1
            s[i] = '#'
    return count
#strings = ['aaadd','ddbfffssdd','nngddgdd']
strings = input("Enter the string: ").split()

if __name__ == "__main__":
    for string in strings:
        print(f"{string} => {check_string(string)}")



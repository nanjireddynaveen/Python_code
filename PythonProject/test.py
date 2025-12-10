#check strings for duplicates

def string_check(s):
    if not s:
        return 0
    duplicate_count = 0
    n = len(s)
    m = list(s)
    for i in range(1, n):
        if m[i] == m[i-1]:
            duplicate_count += 1
            m[i] = '#'
    return duplicate_count
if __name__ == "__main__":
    s = input("Enter the string: ")
    print(string_check(s))


    
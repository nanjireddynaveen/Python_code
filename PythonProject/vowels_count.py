#Count the number of vowels in string

def vowel_count(s):
    vowels = "aeiou"
    count = sum(1 for letter in s if letter in vowels)
    print("Vowel count", count)

if __name__ == "__main__":
    s = input("Enter string: ")
    vowel_count(s)

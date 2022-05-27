# Check if a word is an anagram
# Example:
# find_anagrams("hello") --> False
# find_anagrams(racecar") --> True


def find_anagrams():
    str1 = input("string1: ")
    str2 = input("string2: ")
    if sorted(str1) == sorted(str2):
        print("True")
    else:
        print("False")
find_anagrams()

import unittest

def is_palindrome(word):
    word = word.replace(" ", "")
    for index in range(len(word)):
        if word[index] != (word[len(word)-index-1]):
            return False
    return True

    
if __name__ == "__main__":
    print("test")
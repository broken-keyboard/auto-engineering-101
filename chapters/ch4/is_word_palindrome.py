'''
Create a program that does the followoing
1. Takes any word as input
2. Checks if the word is a palindrome
3. Tells the user whether it is or not
'''

def is_word_palindrome(word):
    word = word.lower()
    reverse_word = word[::-1]
    return reverse_word == word

if __name__ == '__main__':
    word = input('Enter a word to check if it is a palindrome: ')
    result = ''
    if not is_word_palindrome(word):
        result = 'not '
    print(f"The word {word} is {result}a palindrome")
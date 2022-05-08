'''
Create a program that does the followoing
1. Takes any sentence or word as input
2. Counts the number of vowels in the input
3. Prints that number back to the user
'''
def count_vowels(s):
    count = 0
    for i in s.lower():
        if i in 'aiueoy':
            count+=1
    return count


if __name__ == '__main__':
    word = input('Enter a word or a sentence: ')
    print(count_vowels(word))
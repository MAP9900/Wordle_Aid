#Imports
import pandas as pd

#DataFrame
df = pd.read_csv("Five_Letter_Words_Extended.txt", sep=' ', header=None, names=['Words'])

def find(pattern, letters):
    def matches_pattern_and_letters(word, pattern, letters):
        for i, char in enumerate(pattern):
            if char != '-' and word[i] != char:
                return False
        for letter in set(letters):
            if word.count(letter) < letters.count(letter):
                return False
        return True
    matching_words = []
    matches = df[df['Words'].apply(lambda x: matches_pattern_and_letters(x, pattern, letters))]
    matching_words.extend(matches['Words'].tolist())
    return list(set(matching_words))

def main():
    running_letters = []
    pattern = '-----'
    while True:
        print(f"Current search pattern: {pattern}")
        print(f"Current search letters: {', '.join(running_letters)}")
        user_input = input("Enter letters to add to the search, a pattern (e.g. a---r), '/' to clear letters, or 'exit' to quit: ").strip().lower()
        if user_input == 'exit':
            print('Program Finished')
            break
        elif user_input == '/':
            running_letters = []
            pattern = '-----'
            print('Search has been reset.')
            continue
        elif len(user_input) == 5:
            if all(c.isalpha() for c in user_input):  
                running_letters.extend(list(user_input))
            elif (c.isalpha() or c == '-' for c in user_input):
                pattern = user_input
            else:
                print('Invalid input')
                continue
        elif all(char.isalpha() for char in user_input):
            running_letters.extend(list(user_input))
        else:
            print('Invalid input')
            continue
        matching_words = find(pattern, running_letters)
        if matching_words:
            print('Words that match the pattern and/or contain the letters:', ', '.join(matching_words))
        else:
            print('No words found')

if __name__ == '__main__':
    main()

    

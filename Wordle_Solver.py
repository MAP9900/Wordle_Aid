#Imports
import pandas as pd

#Read In DataFrame
df = pd.read_excel('Five_Letter_Words.xlsx')

#Find Matches
import pandas as pd

def find(pattern, letters):
    def matches_pattern_and_letters(word, pattern, letters):
        for i, char in enumerate(pattern):
            if char != '-' and word[i] != char:
                return False
        for letter in set(letters):
            if word.count(letter) < letters.count(letter):
                return False
        return True
    matches = df[df['Words'].apply(lambda x: matches_pattern_and_letters(x, pattern, letters))]
    return matches['Words'].tolist()

#User Interface
def main():
    running_letters = []
    pattern = '-----'
    while True:
        print('Current search pattern: {pattern}')
        if running_letters:
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
        elif len(user_input) == 5 and all(c.isalpha() or c == '-' for c in user_input):
            pattern = user_input
        elif all(char.isalpha() for char in user_input):
            running_letters.extend(list(user_input))
        else:
            print('Invalid input')
            continue
        matching_words = find(pattern, running_letters)
        if matching_words:
            print('Words that match the pattern and contain the letters:', ', '.join(matching_words))
        else:
            print('No words found')

if __name__ == '__main__':
    main()

    
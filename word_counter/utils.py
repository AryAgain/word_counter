"""
- Utility functions for the word_counter package.
- Includes functions to read predefined words and display results.
"""

def read_predefined_words(file_path):
    '''
    reads predefined words, strips whitespace and returns as a set
    '''
    try:
        with open(file_path, 'r') as file:
            return set(line.strip().lower() for line in file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return set()

def display_results(match_counts):
    '''
    prints output in STDOUT as per requirement
    '''
    print(f"{'Predefined word':<25}{'Match count':<15}")
    for word, count in match_counts.most_common():
        print(f"{word:<25}{count:<15}")
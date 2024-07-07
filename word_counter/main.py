"""
Main module for the word_counter package.
"""

from config import PREDEFINE_WORDS_FILE, INPUT_FILE, CHUNK_SIZE
from utils import read_predefined_words, display_results
from process import count_word_match

def main():
    '''
    main method to execute count total occurrence of predefined words 
    in the provided input file
    '''
    predefined_words = read_predefined_words(PREDEFINE_WORDS_FILE)
    match_counts = count_word_match(INPUT_FILE, predefined_words, CHUNK_SIZE)
    display_results(match_counts)

if __name__ == "__main__":
    main()
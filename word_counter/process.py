"""
- Processing module for the word_counter package.
- Contains functions to process text chunks and count word matches.
"""

import re
from collections import Counter
from multiprocessing import Pool, cpu_count
import itertools

def process_chunk(args):
    '''
    counts occurrence of predefined words in the chunk provided
    '''
    chunk, predefined_words = args
    word_pattern = re.compile(r'\b\w+\b')
    chunk_counts = Counter()
    
    for line in chunk:
        words = word_pattern.findall(line.lower())
        chunk_counts.update(word for word in words if word in predefined_words)
    
    return chunk_counts

def count_word_match(input_file_path, predefined_words, chunk_size):
    '''
    divides input files into chunks for parallel processing based on cpu.
    Then, adds up total count from each process
    '''
    match_counts = Counter()
    
    try:
        with open(input_file_path, 'r') as file:
            with Pool(processes=cpu_count()) as pool:
                chunks = iter(lambda: list(itertools.islice(file, chunk_size)), [])
                results = pool.imap_unordered(process_chunk, 
                                              ((chunk, predefined_words) for chunk in chunks))
                
                for chunk_counts in results:
                    match_counts.update(chunk_counts)
    except FileNotFoundError:
        print(f"Error: The file {input_file_path} was not found.")
    
    return match_counts
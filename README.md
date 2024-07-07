# Project Readme

- Submitted by : Aryan Singh
- Email: arysin163@gmail.com
## How to Run the Program

1. Ensure you have Python installed.
2. Unzip the file
3. Open a terminal or load the project in an IDE.
4. Navigate to the project directory: **word_counter**.
5. Run the command: `python main.py`
6. New data file of predefined words or input file can be added under 'data' directory.
7. Filename or chunks unit can be modified under config.py


## What Has Been Tested

- Manual unit testing has been performed to ensure the correctness of the code.
- Exception handling for edge cases.
- The input file is not present.
- A word is not available in the input.
- Performance testing code has been included to measure the execution time of the program under different conditions. Code included:  `python test_performance.py`. Number of repetetions can be modified under config.py

## Assumptions

The following assumptions have been made for this project:

- **Input File**: The input file is a plain text (ASCII) file, with every record separated by a new line.
- **Language**: For this exercise, assume English words only.
- **File Size**: The file size can be up to 20 MB.
- **Predefined Words**: The predefined words are defined in a text file, with every word separated by a newline.
- **No Duplicates**: Predefined words file doesn’t contain duplicates.
- **Word Length**: The maximum length of a word can be up to 256 characters.
- **Case-Insensitive Matches**: Matches should be case-insensitive.
- **Absent Words**: If a predefined word is not present in the input file, then it is not displayed in the output.
- **Exact Match**: The match should be word to word match, no substring matches.
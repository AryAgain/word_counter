"""
Performance testing of the provided solution
"""

from config import TEST_REPEAT_NUMBER
import timeit
from main import main

def performance_test():
    '''
    tests the total execution time for running code multiple times
    '''
    execution_time = timeit.timeit(main, number=TEST_REPEAT_NUMBER)
    print(f"Execution time of main: {execution_time} seconds")

if __name__ == "__main__":
    performance_test()

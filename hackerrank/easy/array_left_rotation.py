import os
from collections import deque

"""
https://www.hackerrank.com/challenges/array-left-rotation/problem

# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
"""


def rotateLeft(d, arr): 
    queue = deque(arr)
    queue.rotate(-d)

    return queue


if __name__ == 'main':
    file = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)

    file.write(' '.join(map(str, result)))
    file.write('\n')

    file.close()

import os
import itertools

"""
https://www.hackerrank.com/challenges/crush/problem

The function is expected to return a LONG_INTEGER.
The function accepts following parameters:
    1. INTEGER n
    2. 2D_INTEGER_ARRAY queries
"""

"""
First not optimized version with Runtime error:

def arrayManipulation(n, queries):
    arr = []
    
    for q in queries:
        arr.append([0 for _ in range(n)])
        
    max_value = 0

    for q in queries:
        a, b, k = q

        for index, _ in enumerate(arr):
            for i in range(a - 1, b):
                arr[index][i] += k
                max_value = max(max_value, arr[index][i])

    return max_value
"""


def arrayManipulation(n, queries):
    arr = [0] * n

    for q in queries:
        a, b, k = q

        arr[a - 1] += k

        if b < n:
            arr[b] -= k

    return max(itertools.accumulate(arr))


if __name__ == '__main__':
    file = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    file.write(str(result) + '\n')

    file.close()

import os

"""
https://www.hackerrank.com/challenges/sparse-arrays/problem

The function is expected to return an INTEGER_ARRAY.
The function accepts following parameters:
 1. STRING_ARRAY stringList
 2. STRING_ARRAY queries
"""


def matchingStrings(stringList, queries):
    return [stringList.count(q) for q in queries]


if __name__ == '__main__':
    file = open(os.environ['OUTPUT_PATH'], 'w')

    stringList_count = int(input().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(stringList, queries)

    file.write('\n'.join(map(str, res)))
    file.write('\n')

    file.close()

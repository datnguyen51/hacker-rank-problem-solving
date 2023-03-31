#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    result = []
    for grade in grades:
        new_grade = grade
        for point in range(1, 4):
            print(int(grade+point) % 5)
            print('\n')
            if (grade+point % 5) == 0 or (grade+point % 10) == 0:
                new_grade = grade + point
                print(new_grade)
                break
        result.append(new_grade)
    return result
    # Write your code here


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()

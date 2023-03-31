#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#


def countApplesAndOranges(start_point_house, end_point_house, apple_tree_point, orange_tree_point, apples, oranges):
    # Write your code here
    number_of_apple = 0
    number_of_orange = 0

    new_list_apple = [apple + apple_tree_point for apple in apples]
    new_list_orange = [orange + orange_tree_point for orange in oranges]

    # print('apples: ', apples)
    # print("new apples: ", new_list_apple)

    for apple in new_list_apple:
        if apple >= start_point_house and apple <= end_point_house:
            number_of_apple += 1

    # print("oranges: ", oranges)
    # print("new oranges: ", new_list_orange)

    for orange in new_list_orange:
        if orange >= start_point_house and orange <= end_point_house:
            number_of_orange += 1

    print(number_of_apple)
    print(number_of_orange)


if __name__ == '__main__':
    # point Sam house
    first_multiple_input = input().rstrip().split()

    start_point_house = int(first_multiple_input[0])

    end_point_house = int(first_multiple_input[1])

    # point apple and orange tree
    second_multiple_input = input().rstrip().split()

    apple_tree_point = int(second_multiple_input[0])

    orange_tree_point = int(second_multiple_input[1])

    # list point
    third_multiple_input = input().rstrip().split()

    apples = int(third_multiple_input[0])

    oranges = int(third_multiple_input[1])

    apples_list = list(map(int, input().rstrip().split()))

    oranges_list = list(map(int, input().rstrip().split()))

    countApplesAndOranges(start_point_house, end_point_house,
                          apple_tree_point, orange_tree_point, apples_list, oranges_list)

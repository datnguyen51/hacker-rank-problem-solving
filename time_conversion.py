#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

time_conversion = {
    'AM': {
        '12': '00',
        '13': '01',
        '14': '02',
        '15': '03',
        '16': '04',
        '17': '05',
        '18': '06',
        '19': '07',
        '20': '08',
        '21': '09',
        '22': '10',
        '23': '11',
    },
    'PM': {
        '00': '12',
        '01': '13',
        '02': '14',
        '03': '15',
        '04': '16',
        '05': '17',
        '06': '18',
        '07': '19',
        '08': '20',
        '09': '21',
        '10': '22',
        '11': '23'
    }
}


def timeConversion(s):
    # Write your code here
    am_or_pm = s[-2:]
    s_hour = s[0:2]

    result_hour = s_hour

    if s_hour in time_conversion[am_or_pm].keys():
        result_hour = time_conversion[am_or_pm][s_hour]

    result = result_hour + s[2:8]

    return result


s = input()

result = timeConversion(s)

print(result)

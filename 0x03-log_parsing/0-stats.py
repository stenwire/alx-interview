#!/usr/bin/python3
"""A module that neatly returns log data"""
import sys
import re

status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
status_dict = {}
count, file_size = 0, 0

try:
    for line in sys.stdin:
        count += 1
        try:
            data = line.split()
            s_code, f_size = data[-2], data[-1]
            file_size += int(f_size)
            if status_dict.get(s_code):
                status_dict[s_code] += 1
            elif s_code in status_codes:
                status_dict[s_code] = 1
        except Exception:
            pass
        if count == 10:
            count = 0
            res = "File size: {}".format(file_size)
            for status_code in sorted(status_dict.keys()):
                res += "\n{}: {}".format(status_code, status_dict[status_code])
            print(res)
    res = "File size: {}".format(file_size)
    for status_code in sorted(status_dict.keys()):
        res += "\n{}: {}".format(status_code, status_dict[status_code])
    print(res)
except KeyboardInterrupt:
    res = "File size: {}".format(file_size)
    for status_code in sorted(status_dict.keys()):
        res += "\n{}: {}".format(status_code, status_dict[status_code])
    print(res)
    raise

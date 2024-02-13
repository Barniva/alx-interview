#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''

import sys

status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
cache = {code: 0 for code in status_codes}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) < 7:
            continue
        size = line_list[-1]
        code = line_list[-2]
        if code in cache:
            cache[code] += 1
            total_size += int(size)
            counter += 1

        if counter == 10:
            print("File size: {}".format(total_size))
            for code in sorted(cache.keys()):
                if cache[code] > 0:
                    print("{}: {}".format(code, cache[code]))
            counter = 0

except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(total_size))
    for code in sorted(cache.keys()):
        if cache[code] > 0:
            print("{}: {}".format(code, cache[code]))

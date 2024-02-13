#!/usr/bin/python3
# This is a script that reads stdin line by line and computes metrics

import sys

# We initialize a dictionary to keep track of the status codes and their counts
status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
cache = {code: 0 for code in status_codes}

# We also initialize variables to keep track of the total file size and the line counter
total_size = 0
counter = 0

try:
    # We read from stdin line by line
    for line in sys.stdin:
        # We split the line into a list of words
        line_list = line.split(" ")
        # If the line does not contain at least 7 words, we skip it
        if len(line_list) < 7:
            continue
        # We extract the size and the status code from the line
        size = line_list[-1]
        code = line_list[-2]
        # If the status code is in our cache, we increment its count and add the size to the total size
        if code in cache:
            cache[code] += 1
            total_size += int(size)
            counter += 1

        # After every 10 lines, we print the statistics
        if counter == 10:
            print("File size: {}".format(total_size))
            for code in sorted(cache.keys()):
                if cache[code] > 0:
                    print("{}: {}".format(code, cache[code]))
            counter = 0

# We handle keyboard interruptions gracefully
except KeyboardInterrupt:
    pass

# Finally, we print the statistics one last time
finally:
    print("File size: {}".format(total_size))
    for code in sorted(cache.keys()):
        if cache[code] > 0:
            print("{}: {}".format(code, cache[code]))


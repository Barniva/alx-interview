
# Log Parsing Script :page_with_curl:

This repository contains a Python script that reads stdin line by line and computes metrics. :bar_chart:

## Description :book:

The script takes an input in the following format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`. If the format is not this one, the line is skipped.

After every 10 lines and/or a keyboard interruption (CTRL + C), the script prints these statistics from the beginning:
- Total file size: File size: `<total size>` where `<total size>` is the sum of all previous `<file size>` (see input format above)
- Number of lines by status code: possible status code: 200, 301, 400, 401, 403, 404, 405 and 500. If a status code doesn’t appear or is not an integer, the script doesn't print anything for this status code. The format is: `<status code>: <number>`. Status codes are printed in ascending order.

:warning: In this sample, you will have random value - it’s normal to not have the same output as this one.

## Usage :computer:

Run the generator script and pipe its output to the stats script:

```bash
./0-generator.py | ./0-stats.py 
```

## Repository Info :file_folder:

- GitHub repository: alx-interview
- Directory: 0x03-log_parsing
- Main File: 0-stats.py

Enjoy using the script! :smile:


# Log Parsing Script

This script reads stdin line by line and computes metrics.

## Input Format

The input format is as follows:

```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```

If the format is not this one, the line will be skipped.

## Output

After every 10 lines and/or a keyboard interruption (CTRL + C), the script prints these statistics from the beginning:

- Total file size: File size: `<total size>`, where `<total size>` is the sum of all previous `<file size>` (see input format above)
- Number of lines by status code: possible status codes are 200, 301, 400, 401, 403, 404, 405, and 500. If a status code doesn’t appear or is not an integer, the script doesn't print anything for this status code. The format is `<status code>: <number>`. Status codes are printed in ascending order.

## Warning

In this sample, you will have random values - it’s normal to not have the same output as this one.

## Usage

You can use the script as follows:

```bash
alexa@ubuntu:~/0x03-log_parsing$ cat 0-generator.py | ./0-stats.py 
```

## Repository

- GitHub repository: alx-interview
- Directory: 0x03-log_parsing
- File: 0-stats.py

## Your Answer

Your answer is a Python script that generates random logs and writes them to stdout:

```python
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()


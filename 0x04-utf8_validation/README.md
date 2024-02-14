
# UTF-8 Validation :mag: :computer:

Welcome to the **UTF-8 Validation** project! This repository is part of the `alx-interview` series. The goal of this project is to determine if a given data set represents a valid UTF-8 encoding.

## :rocket: Project Information

- **Repository:** alx-interview
- **Directory:** 0x04-utf8_validation
- **File:** 0-validate_utf8.py

## :gear: Function Prototype

```python
def validUTF8(data):
    """
    data: a list of integers
    Return: True if data is a valid UTF-8 encoding, else return False
    """
```

## :bulb: Function Details

- A character in UTF-8 can be 1 to 4 bytes long.
- The data set can contain multiple characters.
- The data will be represented by a list of integers.
- Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer.

## :fire: Usage

```bash
carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False
```

## :star2: Enjoy Coding!

We hope you find this project interesting and educational. Happy coding! :smile:


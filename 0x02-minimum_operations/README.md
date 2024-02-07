
# Minimum Operations Challenge 🚀

In this project, we have a single character 'H' in a text file. The text editor can execute only two operations in this file: Copy All and Paste. The challenge is to write a method that calculates the fewest number of operations needed to result in exactly 'n' H characters in the file.

## Prototype 📝

```python
def minOperations(n)
```
This function returns an integer. If 'n' is impossible to achieve, it returns 0.

## Example 🌟

For n = 9,

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6

## Usage 💻

```bash
carrie@ubuntu:~/0x02-minoperations$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
```

## Repository Info 📂

- GitHub repository: alx-interview
- Directory: 0x02-minimum_operations
- File: 0-minoperations.py

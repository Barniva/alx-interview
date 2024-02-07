# Pascal's Triangle :small_red_triangle: :small_red_triangle_down:

Welcome to `alx-interview`! This task in `0x00-pascal_triangle` is about **Pascal's Triangle**. :triangular_ruler:

## Task :clipboard:

Create a Python function `pascal_triangle(n)` that returns Pascal’s triangle of `n`. :snake:

### Requirements :memo:

1. Returns an empty list if `n <= 0`.
2. `n` will always be an integer.

## Usage :computer:

```python
#!/usr/bin/python3
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```

Output:

```shell
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```

Happy coding! :tada: :confetti_ball:


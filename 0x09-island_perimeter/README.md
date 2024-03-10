# 🏝️ Island Perimeter 🏝️

This Python module calculates the perimeter of an island! 🌊

## 🧩 Problem Statement

We have a grid representing a map:
- `0` is water 💧
- `1` is land 🏝️
- The grid is rectangular, max size 100x100
- The grid is surrounded by water
- There's only one island (or none)
- No lakes in the island

## 🚀 Usage

```python
#!/usr/bin/python3
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))


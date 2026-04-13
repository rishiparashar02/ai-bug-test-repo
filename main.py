```python
from math import gcd

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    if a == 0:
        return 0  # or any other default value
    return a / b

def main():
    try:
        print(divide(10, 2))
        print(divide(0, 2))
        print(divide(10, 0))
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
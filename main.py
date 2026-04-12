```python
from math import gcd

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    if a == 0:
        return 0  # or any other default value
    return a / b

print(divide(10, 2))
```
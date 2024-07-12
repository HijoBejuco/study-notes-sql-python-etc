# Notes on studying SQL, Python, etc 🚀🌀🌿

## Index
- <a href="#sql_arrays">Arrays on SQL</a>


<a name=sql_arrays></a>
## Arrays on SQL






## Python decorators
A decorator is a function that modifies the behavior of another function or method. Can be created using @ and they are used for code reuse and to add general functionalities to methods/functions.

```python
import time

# Creating decorator
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function {func.__name__} took {elapsed_time:.4f} seconds to complete")
        return result
    return wrapper

# decorating the function
@timer_decorator
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Calling decorated function
result = example_function(1000000)
print(f"Result: {result}")

# Notes on studying SQL, Python, etc 🚀🌀🌿

## Index
- <a href="#sql_arrays">Arrays on SQL</a>


<a name=sql_arrays></a>
## Arrays on SQL


<details>
  <!--<summary>Tabla de contenidos</summary>-->
  <ol><!-- Etiqueta de lista ordenada -->
    <li>
      <a href="#python-decorators">Python decorators</a>
      <ul>
        <li><a href="#explaining-code-of-decorators">Explaining code of decorators</a></li>
      </ul>
    </li>
    <li>
      <a href="#python-decorators">Python decorators</a>
    </li>
    <li>
      <a href="#deep-learning">Deep learning</a>
    </li>
  </ol>
</details>


## Python decorators
A decorator is a function that modifies the behavior of another function or method. Can be created using @ and they are used for code reuse and to add general functionalities to methods/functions.

The following code shows how to create a simple decorator which only calculates how much time takes to excecute a function. 

```python
import time

# Creating decorator
# The decorator recieves a function as parameter
def timer_decorator(func): 
    # wrapper envuelve la función original, y toma cualquier numero de 
    # argumentos y parámetros para poder recibir cualquier función y 
    # ejecutarla adentro suyo.
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function {func.__name__} took {elapsed_time:.4f} seconds to complete")
        # wrapper returns the result of the original function.
        return result
    # timer_decorator returns the wrapper function
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
```
#### Explaining code of decorators
timer_decorator returns the wrapper function (**returns the reference to wrapper**), but do not calls it. This means that we can create a variable to assign to the timer_decorator and consequently use that variable as it was the wrapper function. 

For example, in the following code, we assing timer_decorator to a variable called "var" and then we can use "var" as it was the function wrapper. 

```python
var = timer_decorator(example_function)
print(var(4))
```

When we apply a decorator to a function using the @, it is equivalent to do the following: 
```python
example_function = timer_decorator(example_function) 
```
Here we assign to the variable "example_function", the new functionalities of the decorator, so this means that after the function is decorated, when we use the example_function function, **WE ARE CALLING THE *wrapper* function** instead of the original one. 



## Arrays in bigquery and sql

### ARRAY_AGG:
This is an Aggregating function, so it aggregates all the values using a group by clause. It takes different rows and transform them into a single row of ARRAY datatype. 


## Deep learning

### The linear unit
This is the fundamental component of a NN. The individual neuron. A neuron with one input looks like: 
![individual neuron](images/individual_neuron.png)
The input is x,the connection to the network has a weighy w, whenever the input flows through a connection, the value is multiplied by the weight. A NN "learns" by modifying its weights.

**b** is a special weight called the bias, this has not any input., thats why, The bias enables the neuron to modify the output independently of it's inputs. 

**y** is the output of the neuron. The neuron sums up all the values it recieves through its connections. The neuron's activation is: ***y=wx+b*** (This is just the equation of a line)







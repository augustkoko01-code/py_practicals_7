# Python Functions - Week 7 Notes

## What is a Function?

A function is a block of code that performs a specific task.

Benefits of using functions:

* Reuse code
* Avoid code duplication
* Make programs shorter
* Make programs easier to read
* Make programs easier to maintain

Examples of functions:

```python
print()
input()
int()
float()
len()
```

---

# Function Definition

General syntax:

```python
def function_name(parameters):
    # code
    return result
```

### Notes

* `def` is used to define a function.
* The first line is called the **function header**.
* Parameters are optional.
* A function can have zero or more parameters.
* `return` is optional.
* A function can return:

  * None
  * One value
  * Multiple values
* A function can have multiple `return` statements.
* When a `return` statement executes, the function ends immediately.

---

# Types of Functions

## 1. No Parameters, No Return Value

```python
def display_menu():
    print("Menu")
```

Used when a function only performs an action.

---

## 2. Parameters, No Return Value

```python
def print_character(char, n):
    for i in range(n):
        print(char)
```

Used when input is needed but no result needs to be returned.

---

## 3. Parameters and Return Value

```python
def get_discount(price):
    if price < 100:
        return 0.0

    if price < 250:
        return 0.05

    return 0.1
```

Used when a function calculates and returns a result.

---

# Calling a Function

A function must be defined before it can be called.

Example:

```python
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

result = calculate_bmi(70, 1.75)
```

### Terminology

```python
def calculate_bmi(weight, height):
```

`weight` and `height` are **parameters**.

```python
calculate_bmi(70, 1.75)
```

`70` and `1.75` are **arguments**.

---

# User-Defined vs Built-In Functions

## User-Defined Functions

Functions written by the programmer.

Example:

```python
def calculate_bmi(weight, height):
    return weight / (height ** 2)
```

---

## Built-In Functions

Functions already provided by Python.

Examples:

```python
print()
input()
int()
float()
str()
len()
max()
min()
abs()
```

### Recommendation

Use built-in functions when they already solve the problem.

Do not reinvent the wheel.

---

# Python Modules

A module is a Python file containing functions and other code.

---

## Math Module

```python
import math

math.sqrt(25)
math.pow(2, 3)
math.ceil(4.73)
math.floor(4.73)
math.sin(0)
math.cos(0)
```

---

## Random Module

```python
import random

random.random()
random.randint(1, 10)
```

---

## Winsound Module

```python
winsound.MessageBeep()
winsound.PlaySound()
```

---

## Datetime Module

```python
datetime.today()
datetime.now()
```

---

# Importing Functions

Import an entire module:

```python
import math

math.ceil(4.73)
```

---

Import a specific function:

```python
from math import ceil

ceil(4.73)
```

---

Import everything:

```python
from math import *

ceil(4.73)
```

---

# Defining Functions in a Module

Functions can be stored in a separate Python file.

Example:

## fn.py

```python
import random

def random100():
    return random.randint(1, 100)

def max(x, y):
    if x > y:
        return x
    return y
```

## program.py

```python
import fn

n1 = fn.random100()
n2 = fn.random100()

result = fn.max(n1, n2)
```

Benefits:

* Better organisation
* Code reuse across multiple programs

---

# Variable Scope

Scope refers to where a variable can be accessed.

---

## Global Variable

Defined outside a function.

```python
x = 10
```

Accessible throughout the program after it is defined.

---

## Local Variable

Defined inside a function.

```python
def show():
    x = 10
```

Accessible only inside that function.

---

# Local vs Global Variables

Example:

```python
x = 10
y = 20

def fn1():
    result = x + y
    print(result)

def fn2():
    x = 20
    result = x + y
    print(result)
```

Output:

```python
30
40
```

Reason:

* `fn1()` uses global `x`
* `fn2()` uses local `x`

If a local variable has the same name as a global variable, the local variable takes priority.

---

# Updating Global Variables

### Not Recommended

```python
def f():
    global x
    x = x + 1
```

Using `global` is generally discouraged.

---

### Recommended

```python
def f(x):
    x = x + 1
    return x

x = 5
x = f(x)
```

Output:

```python
6
```

---

# Parameter Passing

There are two types.

---

## Pass-by-Value

Used for immutable objects:

* int
* float
* str
* bool
* tuple

A copy of the value is passed to the function.

Changes inside the function do not affect the original value.

Example:

```python
def change(n):
    n = 10

x = 5

change(x)

print(x)
```

Output:

```python
5
```

---

## Pass-by-Reference

Used for mutable objects:

* list
* dictionary
* set

The function works with the same object.

Changes inside the function affect the original object.

Example:

```python
def change_list(numbers):
    numbers[0] = 100

my_list = [1, 2, 3]

change_list(my_list)

print(my_list)
```

Output:

```python
[100, 2, 3]
```

---

# Function Call Pitfall

Every function call uses memory.

Bad example:

```python
def withdraw(balance):

    amount = float(input())

    if amount > balance:
        withdraw(balance)
```

Repeated function calls consume additional memory.

---

Better approach:

```python
while amount > balance:
    print("Invalid amount")
```

Use loops instead of repeatedly calling the same function.

---

# Quick Revision Table

| Concept           | Meaning                             |
| ----------------- | ----------------------------------- |
| Function          | Reusable block of code              |
| Parameter         | Input defined in a function         |
| Argument          | Value passed into a function        |
| Return            | Sends a result back                 |
| Global Variable   | Variable defined outside a function |
| Local Variable    | Variable defined inside a function  |
| Module            | Python file containing functions    |
| Import            | Makes functions available for use   |
| Pass-by-Value     | Original value is unchanged         |
| Pass-by-Reference | Original object can be modified     |

---

# Key Takeaways

1. Functions help reduce code duplication.
2. Functions improve readability and organisation.
3. Parameters are inputs to functions.
4. Return values are outputs from functions.
5. Local variables exist only inside functions.
6. Global variables exist outside functions.
7. Immutable objects use pass-by-value.
8. Mutable objects use pass-by-reference.
9. Use built-in functions when available.
10. Avoid unnecessary repeated function calls.

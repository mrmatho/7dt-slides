---
title: Python Variables
layout: cover
class: text-center
background: /img/duck-typing.png
hideInToc: false
transition: fade
---

# Python Variables

---
layout: li
---

::li::

- To be able to understand the purpose of variables in programming.
- To be able to create and use variables in Python for our micro:bit projects.
- To understand the difference between different data types in Python and why they are important.

::sc::

- Use variables in Python to store text and numbers
- Describe the difference between strings, integers, and floats

---
layout: center
zoom: 1.2
---

# Variables



- *Variables* are used to **store data** in a program.
- Their value can change - hence the name "variable".
- A variable is *like a container that holds information*.
- We use variables to keep track of values that we want to use later.
- In Python, we create a variable by:
    - giving it a name 
    - and assigning it a value


```python
my_variable = 10 

```


---
layout: center
zoom: 1.5
---

# Naming Variables

- Variable names can contain letters, numbers, and underscores.
- They cannot start with a number and cannot contain spaces or special characters (like @, #, $, etc.).
- Variable names should be descriptive to make the code more readable.
- For example, instead of using `x`, use `temperature` or `score`.

---
layout: center
zoom: 1.1
---

# Why do I need variables in my micro:bit program?

- Variables are used to store data that we want to use later in our program
- Variables help us keep track of values that change over time, like scores in a game or the temperature in a room.



```python

from microbit import *

count = 0

while True:
    if button_a.was_pressed():
        count = count + 1
    display.scroll(count)
```

What do you think this program does?

---
layout: center
zoom: 1.1
---

# Your Turn!

1. Open the sample code in Micro:bit Classroom. Test that it adds 1 to the `count` each time you press button A.
2. Change the program so that it also adds 2 to the `count` each time you press **button B**. (This will need an additional `if` statement.)
3. Update the program so that it resets the `count` to 0 when you shake the micro:bit.
 
*Sample Code*

```python

from microbit import *

count = 0

while True:
    if button_a.was_pressed():
        count = count + 1
    display.show(count)
``` 
---
layout: two-cols-header
zoom: 0.9
---

# Using Variables

- Variables can be used for calculating, comparing and storing data.

::left::

**Calculating**

```python
a = 5
b = 10

result = a + b  # result is now 15
```

We can use any of the mathematical operators: `+`, `-`, `*`, `/`.

We can also use the `+=` operator to add a value to a variable.

```python
a = 5
a += 2  # a is now 7
```

::right::

**Comparing**

```python
a = 5
b = 10

if a < b:
    print("a is less than b")
else:
    print("a is greater than or equal to b")
```

```python

a = 5
b = 5

if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")
```

*Note:* `==` is used for comparison, while `=` is used for assignment. To check for not equal, we use `!=`. 

---
layout: center
---

<img src="/img/duck-typing.png" alt="Duck Typing" id = "duck" style="width:300px; float:right; border-radius: 25px;" />
<caption style="width: 300px; clear: right;float:right; font-size: 0.8rem; color: #999;" for="duck">Prize for anyone who can tell me the significance of this image. (It's pretty niche)</caption>

# Data Types

- Data types are the different kinds of data that we can use in our programs.
- In Python, there are several data types, but the most common ones are:
    - **Integers**: Whole numbers (e.g., 1, 2, 3)
    - **Floats**: Decimal numbers (e.g., 1.5, 2.7)
    - **Strings**: Text (e.g., "Hello", "Micro:bit", "This is the best ever!!!!")
    - **Booleans**: True or False values (e.g., True, False)

Each data type has its own purpose and is used in different situations. 
- For example, we would use integers for counting, floats for measurements, strings for text, and booleans for true/false conditions.
- *Understanding data types is important* because it helps us choose the right type of variable for our data and avoid errors in our programs.

---
layout: center
zoom: 1.2
---

# Using variables with different data types

```python

name = "Alice"  # String
age = 10  # Integer
height = 1.5  # Float
is_student = True  # Boolean

```

Notice:
- Alice is in quotes because it is a **string**.
- 10 is not in quotes because it is an **integer**.
- We know that height is a **float** because it has a decimal point.
- is_student is a **boolean** because it can only be `True` or `False`.

---
layout: two-cols
---

# Data Types Questions

On the worksheet, identify the data type of each value by circling it:

1. "Hello"
2. 3.14
3. 42
4. True
5. "Micro:bit"
6. 0.5
7. 7 + 2.1
8. "10"

::right::

<div class="note" style="padding: 20px; text-size: 1.2rem;">

# Remember:

- Text data -> **String**
- Whole numbers -> **Integer**
- Decimal numbers -> **Float**
- True or False -> **Boolean**

</div>


---
layout: two-cols-header
zoom: 1.1
---

# Working with different data types

::left::

```python

name = "Philip"
multiplier = 2

out = name * multiplier
print(out)  # Output: PhilipPhilip

```

- We can multiply a string by an integer to repeat the string that many times.
- In this case, the string "Philip" is repeated 2 times, resulting in "PhilipPhilip".

::right::

```python

name = "Roger"
multiplier = 2.5

out = name * multiplier
print(out)  # Output: TypeError

```

- We cannot multiply a string by a float (decimal number).
- This will result in a `TypeError` because Python does not allow this operation.
- Python only allows multiplying a string by an integer because it needs to know how many times to repeat the string. A float does not represent a whole number, so this operation is not allowed.

---
layout: center
zoom: 0.9
---

# Converting between data types

- Sometimes we need to convert between different data types.
- For example, if we have a string that represents a number, we can convert it to an integer or float.
- We can use the `int()` and `float()` functions to convert strings to integers and floats, respectively.
- Be careful when converting strings to numbers. If the string does not represent a valid number (e.g., "hello"), Python will raise a `ValueError`.

```python
age = "10"  # String
age_int = int(age)  # Convert to Integer
age_float = float(age)  # Convert to Float

```

- We can also convert numbers to strings using the `str()` function.

```python

age = 10  # Integer
age_str = str(age)  # Convert to String

print("My age is " + age_str)  # Output: My age is 10

```

- This is useful when we want to display numbers as text or concatenate (merge) them with other strings.

---
layout: center
---

# Using A Variable for Temperature

Micro:bit allows us to measure the temperature using the built-in temperature sensor. We can use a variable to store the temperature value before we display it on the micro:bit's LED screen.

```python
from microbit import *

temp = temperature()  # Get the current temperature (in degrees Celsius) and store it in temp
display.show(temp)  # Display the temperature on the micro:bit
```

## Your Turn!

Create one of the following programs using a variable for temperature: 

| Mild | Medium | Spicy |
|----|---|---|
| Display the current temperature in Celsius | Display the temperature in Celsius, then in Fahrenheit | Decide whether the temperature as Cold, Mild or Hot, then give the temperature in Celsius and Fahrenheit |

 
<div class="note"> 

**Note:**

The formula for converting Celsius to Fahrenheit is:
`temp_fahrenheit = temp * 9/5 + 32`
</div>  
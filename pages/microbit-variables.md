---
title: Python Variables
layout: cover
class: text-center
background: /img/microbit-bg.webp
hideInToc: false
transition: fade
---

# Python Variables

---
layout: li
---

::li::

- To be able to understand the purpose of variables in programming.
- To be able to create and use variables in Python for our micro:bit projects
- To understand the difference between different data types in Python and why they are important.

::sc::

- Use variables in Python to store text and numbers
- Describe the difference between strings, integers, and floats

---
layout: center
zoom: 1.2
---

# Variables

<v-clicks depth="2">

- Variables are used to **store data** in a program.
- Their value can change - hence the name "variable".
- A variable is like a container that holds information.
- We use variables to keep track of values that we want to use later.
- In Python, we create a variable by:
    - giving it a name 
    - and assigning it a value

</v-clicks>

<v-clicks>
```python
my_variable = 10 
```
</v-clicks>

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
    display.show(count)
    sleep(100)
```

What do you think this program does?

---
layout: center
zoom: 1.1
---

# Your Turn!

1. Open the sample code in Micro:bit Classroom. Test that it adds 1 to the `count` each time you press button A.
2. Change the program so that it also adds 2 to the `count` each time you press **button B**.
3. Update the program so that it resets the `count` to 0 when you shake the micro:bit.
 
*Sample Code*

```python

from microbit import *

count = 0

while True:
    if button_a.was_pressed():
        count = count + 1
    display.show(count)
    sleep(100)
``` 

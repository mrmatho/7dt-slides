---
title: Programming with Micro:bit
layout: cover
class: text-center
background: /img/microbit-bg.webp
hideInToc: false
transition: fade
---

# Programming with Micro:bit

---
layout: center
---

# What is a Micro:bit?

- A small computer that can be programmed to do different things.
- It has sensors, buttons, and lights that can be used to create fun projects.
- It can be programmed using a block-based language (MakeCode) or Python
- We are using Python, which is a text-based programming language.

---
layout: two-cols-header
---

# Micro:bit features

<img src="/img/microbit-diagram.avif" alt="Micro:bit features" width="500" style="display:block; margin:auto"/>

::left::

- **LED display**: 5x5 grid of lights that can show images or text.
- **Buttons**: Two buttons (A and B) that can be pressed to trigger actions.
- **Accelerometer**: Detects movement and orientation.
- **Compass**: Measures direction (North, South, East, West).
- **Temperature sensor**: Measures the temperature.

::right::
- **Bluetooth**: Allows the Micro:bit to connect to other devices wirelessly.
- **USB port**: Used to connect the Micro:bit to a computer for programming.
- **Power supply**: Can be powered by batteries or USB.
- **Pins**: 25 pins that can be used to connect to other devices or sensors.

---
layout: center
---

# What is Python?
- Python is currently the most popular programming language in the world.
- It is used by professionals and beginners across many industries.
- It is considered easier to write and read than other programming languages.
- When AI tools like ChatGPT create code to solve problems, they often use Python

---
layout: center
zoom: 1.3
---

# Python basics - Hello World!


```python
print("Hello, World!")
```

- This code prints "Hello, World!" to the screen, using a terminal or console.
- The `print` function is used to display text or numbers.
- The text inside the parentheses is called a string, and it must be enclosed in quotation marks.

<v-click>

```python
display.scroll("Hello, World!")
```

- This is the same code, only using the Micro:bit display to scroll the message.

</v-click>
---
layout: center
---

# Our First Micro:bit Program

Open the Micro:bit editor at https://python.microbit.org/

- Click on the "New" button to create a new program.
- Remove everything in the editor **except** the `from microbit import *` line.
    - This line imports the Micro:bit library, which allows us to use the Micro:bit's features in our program.
- Write code to scroll a message on the Micro:bit display.
    - Remember: You can use the `display.scroll()` function to scroll text on the Micro:bit display.
- Test your code on the Micro:bit simulator on the right hand side

*Note:* The Micro:bit editor suggests code as you type. This is a great way to learn how to use the Micro:bit library and Python syntax (and makes it less likely that you will make a mistake). If you see a suggestion that you like, press the `Enter` key to accept it.




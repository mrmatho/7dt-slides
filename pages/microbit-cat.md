---
title: Micro:bit CAT
layout: cover
class: text-center
background: /img/microbit-bg.webp
hideInToc: false
transition: fade
---

# Your Micro:bit CAT

---
layout: center
zoom: 1.3
---

# What do you need to do?

1. **Select a problem** you want to solve
2. **Design** the solution (including using a flowchart)
3. **Write** the code
4. **Test** the code, documenting your results
5. **Reflect** on the process and results
6. Submit your code and documentation

---
layout: center
---

# Choosing a Problem to Solve

Your problem needs to have: 

- A clear goal
- Input and output
- Use of multiple micro:bit features (eg. sensors, buttons, LEDs, radio, etc.)

You can choose a problem from the provided list or choose your own. The more original ideas will be more interesting to work on!

Your problem can (but doesn't have to) use more that one micro:bit if you would like, and they can be running the same or different code from one another. 

---
layout: center
zoom: 1.3
---

# Project Example Ideas

- A simple game (e.g. rock-paper-scissors, a quiz, etc.)
- A weather station that displays temperature from another micro:bit
- Game show buzzers (uding buttons to buzz in and a control micro:bit to see who buzzed in first)
- A virtual pet that responds to button presses and displays emotions on the LED screen

---
layout: center
---

# Using a Flowchart

A flowchart is a visual representation of the steps in your program. It helps you plan the logic before you start coding.

```mermaid

flowchart LR
    A(Start) --> X[while True]
    X --> B{Is the button pressed?}
    B -- Yes --> C[Display Hello!]
    B -- No --> D[Show a Duck]
    C --> E[Wait 1 second]
    D --> E
    E --> X
```

---
layout: center
---

# Flowchart Basics:

- **Start/End**: Represented by rounded rectangles (e.g., Start, End).
- **Processes**: Represented by rectangles (e.g., Display Hello!).
- **Decisions**: Represented by diamonds (e.g., Is the button pressed?).
- **Arrows**: Show the flow of the program.

```mermaid

flowchart LR
    A(Start) --> B[Process 1]
    B --> C{Decision?}
    C -- Yes --> D[Process 2]
    C -- No --> E[Process 3]
    D --> F(End)
    E --> F

```
---
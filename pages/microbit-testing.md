---
title: Testing Your Micro:bit Project
layout: cover
class: text-center
background: /img/microbit-bg.webp
hideInToc: false
transition: fade
---

# Testing
## Running tests and creating a test table

---
layout: center
zoom: 1.3
---

# What is Testing?

<v-clicks>

- Testing is the process of running your code to see if it works as expected
- It helps you find any bugs or issues in your code
- An untested program will almost always have bugs!
- We record the results of our tests in a test table

</v-clicks>

---
layout: center
zoom: 1.1
---

# Test Data

When we test, we care about three main things:

- **Test Data**: The specific ways we will test our program
    - On a micro:bit project, this could be button presses, sensor readings, shaking the micro:bit, etc.
- **Expected Outcome**: What we *expect* to happen when we use the test data, if the program is working correctly
- **Actual Outcome**: What *actually* happens when we run the test

---
layout: center
zoom: 1
---

# Test Table Example
<br>
Felicity has created a micro:bit program to play rock-paper-scissors. The player uses Button A to select rock (R), paper (P), or scissors(S), and then shakes the micro:bit to see what the computer chooses. If the player wins, the micro:bit should show a happy face; if the computer wins, it should show a sad face; and if it's a tie, it should show a neutral face.

<v-clicks depth="1">

| Test Data               | Expected Outcome          | Actual Outcome            |
|-------------------------|---------------------------|---------------------------|
| Press Button A once, shake | Player chooses rock;   | Player chooses rock; |
|                         | If computer chooses scissors; happy face | When computer chose scissors; happy face|
|                         | If computer chooses paper; sad face | When computer chose paper; happy face|
|                         | If computer chooses rock; neutral face | When computer chose rock; happy face|

- Which tests *passed*?
- Which tests *failed*? (Note: Failed tests are good - that's what testing is for!)
- What does Felicity need to do next?
- *What else* does Felicity need to test?

</v-clicks>

---
layout: center
zoom: 1.1
---

# On your CAT

We aren't asking you to write as much - just a simplified version:
- Test (What will you do to test your program?)
- Outcome (What happened?)
- Notes (Anything you found, fixed, or need to do next)

Felicity's test table might look like this:

| Test                | Outcome            | Notes                   |
|---------------------|--------------------|-------------------------|
| Button A once, shake | Chose rock, face only worked if computer chose paper         | *Fixed this and now faces show correctly* |
| Button A twice, shake | Chose paper, face worked correctly for all computer choices        |                         |
| Button A three times, shake | Chose scissors, face worked correctly for all computer choices     |                         |
| *Button B pressed* | *Nothing happened*     | *This is expected*       |

---
layout: center
zoom: 1.2
---

# Working on the CAT Today:

- Test your code on the simulator and the micro:bit
- Fill in your test table with at least 5 different tests
- Make any necessary changes to your code based on your test results

---
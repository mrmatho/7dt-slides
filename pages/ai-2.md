---
title: AI - How do machines learn?
layout: cover
class: text-center
background: /img/ai-bg.png
hideInToc: false
transition: fade
---

# AI- How do machines learn?

---
layout: center
---

## Slides adapted from DayOfAIaustralia.com

*Used under Creative Commons Attribution-NonCommercial 4.0 International License*

<img src="/img/DOAI_HORIZONTAL.svg" alt="Day of AI Logo" style="width:300px; margin:auto;"/>

---
layout: li
---

::li::

- To be able to describe how machines learn
- To understand the concept of data labeling and training data
- To experience training a machine learning model

::sc::
- Identify the importance of data labeling and describe how it impacts machine learning
- Experienced training a machine learning model

---
layout: center
zoom: 1.1
---

# Fleeps and Bloops

This is a Fleep.

<img src="/img/fleep.png" alt="Fleep" style="width:300px; margin:auto;"/>

---
layout: center
---

# Fleeps and Bloops

These are also Fleeps.
<div class="flex justify-center">
  <img src="/img/fleep-2.png" alt="Fleep" style="width:300px;"/>
  <img src="/img/fleep-3.png" alt="Fleep" style="width:300px;"/>
</div>

---
layout: center
---

# Fleeps and Bloops

This is a Bloop.

<img src="/img/bloop.png" alt="Bloop" style="width:300px; margin:auto;"/>

---
layout: center
---

# Fleeps and Bloops

These are also Bloops.

<div class="flex justify-center">
  <img src="/img/bloop-2.png" alt="Bloop" style="width:300px;"/>
  <img src="/img/bloop-3.png" alt="Bloop" style="width:300px;"/>
</div>

---
layout: center
---

# What is this guy?

If you think this is a Fleep, put your hand on your head.
If you think this is a Bloop, put your hand on your heart.

<div class="flex justify-center">
  <img src="/img/fleep-4.png" alt="Fleep or Bloop?" style="width:250px;"/>
</div>

<v-clicks>

If you said Fleep, you are correct!

</v-clicks>
---
layout: center
zoom: 1.2
---

# Reminder from last lesson

- The three parts of a machine learning model:
  - **Data**: The information we use to train the model
  - **Algorithm**: The algorithm that learns from the data
  - **Prediction**: The process of teaching the model using the data

<v-clicks depth="2">

- The data was the *images of Fleeps and Bloops*
  - *AND the labels we gave them*. If I hadn't told you which was which, you wouldn't have been able to learn!
- The algorithm was the process of us *identifying what was special or different about Fleeps and Bloops*
- The prediction was us trying to *guess if the new image* was a Fleep or a Bloop

</v-clicks>

---
layout: center
zoom: 1.3
---

# Labelling data

- The only reason we could pick between Fleeps and Bloops was because we had labelled the data
- We had to know *which* images were Fleeps and which were Bloops
- This is called **data labeling**
- Data labeling is the process of identifying and tagging data with relevant information
- Labeling gives the model the *meaning* information it needs to learn

---
layout: center
zoom: 1.4
---

# Lesson 2 - Questions 1 & 2

In your booklet, describe why labelling data is important for AI and think about what would happen if we mis-labelled the data.

---
layout: center
zoom: 1.2
---

# So How Do Machines Learn?

Once the data is labelled, the machine learning model can learn from it. 
- The model uses the labelled data to identify patterns and relationships
- It then uses these patterns to make predictions on new, unseen data
- The more accurate data the model has, the better it can learn and make reliable predictions

---
layout: two-cols-header
zoom: 0.88
---

# The Teachable Machine

The Teachable Machine is an educational tool for creating our own machine learning models.
It allows us to train a model using our own data and see how it learns. The Teachable Machine runs training all in the browser, so you don't need to install anything and the data never leaves your computer.

::left::

## What we will do

- We are creating a model that we train ourselves. You can choose:
  - **An image model** that recognises something using your webcam (e.g. Pen or Scissors, Happy face or Sad face, Rock paper scissors)
  - **An audio model** that recognises sounds (e.g. Clap or Click, My voice or a friend's voice) 
  - **A pose model** that recognises different poses (e.g. Arms up or Arms down, Hands on head or Hands on hips)
- Train the model by providing examples of each class
- Test the model by providing new examples

::right::

# Plan of Action
1. Go to [Teachable Machine](https://teachablemachine.withgoogle.com/)
2. Click "Get Started"
3. Select the type of model you want to create. 
4. Add classes for each category you want to recognise
5. Click the Record button to **record examples** for each class
6. Click the Train button to train the model (this will take a bit of time)
7. Once the model is trained, you can test it by providing new examples

---
layout: center
zoom: 1.4
---

# Lesson 2 - Question 3 (Reflect)

Write 3 things you learned from your experiment with the Teachable Machine.

---
layout: center
zoom: 1.2
---

# (If time) AI in action

<Youtube id="GG3UNLUA1W4" width="600" height="400"/>

---
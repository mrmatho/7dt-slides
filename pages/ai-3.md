---
title: AI - How do machines create things?
layout: cover
class: text-center
background: /img/ai-bg.png
hideInToc: false
transition: fade
---

# AI - How do machines create things?
## Lesson 3

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
- To be able to describe how machines create things
- To understand the concept of generative AI

::sc::
- Identify examples of generative AI in real-world applications
- Discuss the positive and negative impacts of generative AI

---
layout: two-cols
zoom: 1.3
---

# What does "generative" mean?

<v-clicks depth="3">

- Creating something new
- Producing content

</v-clicks>

::right::

<v-clicks depth="3">

## So what is "Generative AI"?

- AI that can create new content
- Uses existing data to generate new ideas, images, text, or other media

</v-clicks>

---
layout: center
zoom: 0.9
---

# Examples of Generative AI

<div class="grid grid-cols-3 gap-4">
  <div class="bg-purple-400 p-4 rounded-lg shadow text-center">
    <img src="/img/generative-ai-text.png" alt="Text Generation" style="width:100px; margin:auto;"/>
    <h4>Text Generation</h4>
    <p>Like ChatGPT, Claude, Gemini</p>
  </div>
  <div class="bg-orange-400 p-4 rounded-lg shadow text-center">
    <img src="/img/generative-ai-image.png" alt="Image Generation" style="width:100px; margin:auto;"/>
    <h4>Image Generation</h4>
    <p>Like DALL-E, Midjourney</p>
  </div>
  <div class="bg-green-400 p-4 rounded-lg shadow text-center">
    <img src="/img/generative-ai-video.png" alt="Video Generation" style="width:100px; margin:auto;"/>
    <h4>Video Generation</h4>
    <p>Like Sora, Runway, Veo AI</p>
  </div>
  <div class="bg-red-400 p-4 rounded-lg shadow text-center">
    <img src="/img/generative-ai-music.png" alt="Music Generation" style="width:100px; margin:auto;"/>
    <h4>Music Generation</h4>
    <p>Like AIVA, MuseNet, Jukedeck</p>
  </div>
  <div class="bg-blue-400 p-4 rounded-lg shadow text-center">
    <img src="/img/generative-ai-code.png" alt="Code Generation" style="width:100px; margin:auto;"/>
    <h4>Code Generation</h4>
    <p>Like GitHub Copilot, Tabnine, Cursor</p>
  </div>

</div>

---
layout: center
zoon: 1.2
---

# ChatGPT


<img src="/img/generative-ai-text.png" alt="ChatGPT Logo" style="width:250px; float:right;"/>


ChatGPT is a generative AI model developed by OpenAI that can understand and generate human-like text. It can answer questions, write essays, create stories, and even engage in conversations. It uses a **Large Language Model (LLM)** to process and generate text based on the input it receives.

*Demo*

---
layout: two-cols-header
zoom: 0.95
---

# Generating Text

LLM's (like ChatGPT) break up text into tiny chunks called tokens.  

::left::

For example the sentence "Mr Matheson is very smart and teaches Year 7 students." would be broken up into the following tokens:

```json
[
  "Mr",
  " Matheson",
  " is",
  " very",
  " smart",
  " and",
  " teaches",
  " Year",
  " 7",
  " students",
  "."
]
```

::right::

Here is another example. The sentence "The unforgettable trip to New York was amazing." would be broken up like this:

```json
[
  "The",
  " un",
  "forgettable",
  " trip",
  " to",
  " New York",
  " was",
  " amazing",
  "."
]
```

*Note: The tokens are not always whole words, they can be parts of words or even punctuation.*

---
layout: center
---

# Generating Text

- The *algorithm* behind an *LLM* learns how tokens in the dataset relate to each other. 
- It uses this knowledge to *predict* the next token in a sequence. 

For example if the input is *"Mr Matheson is very"*, the model might predict the next token to be *"smart"* based on its training data.

|Prompt| Possible Next Tokens| Probabilities |
|---|---|---|
|Mr Matheson is very| smart, old, funny, strict| 40%, 20%, 30%, 10% |
|The capital of France is| Paris, London, Berlin, Madrid | 90%, 5%, 3%, 2% |
|The sun is| shining, bright, yellow, hot | 50%, 20%, 20%, 10% |
|Once| upon, there, I, it | 40%, 30%, 15%, 15% |

This process repeats until the model has generated a complete response or reaches a specified length.

---
layout: center
zoom: 1.4
---

# What are the benefits of Generative AI?

At your tables discuss benefits (think about jobs being easier, new possibilities, etc.) in:

- Images
- Text
- Video

*Write some of your best ideas in the space provided in your booklet*

---
layout: center
zoom: 1.2
---

# Plagiarism, Copyright and Deep Fakes

- **Plagiarism**: Passing off AI-generated content as your own is unethical, and in some cases can cost your job or academic progress.
- **Copyright**: Artificial intelligence needs massive amounts of data to learn from, and this data often includes copyrighted material. The people who originally created the data have usually not given permission or been paid for their work that the AI is using.
- **Deep Fakes**: AI can create realistic fake images, videos, and audio that can be used to mislead or manipulate people. This can lead to misinformation, privacy violations, cyberbullying and identity theft.

---
layout: center
zoom: 1.4
---

# Hallucinations

When a person sees something that isn't real, we call it a "hallucination". When an AI model generates information that is incorrect or made up, we also call this a "hallucination".

*LLMs* can generate text that sounds realistic but is actually false or misleading. Because the model is just predicting what the next word should be, it can get it completely wrong.

---
zoom: 1.3
---

# What are some potential problems with Generative AI?

At your tables discuss possible issues in:

- Images
- Text
- Video

*Write some of your best ideas in the space provided in your booklet*

---
layout: center
zoom: 1.2
---

# Bias in AI

- AI models can only create content based on the data they were trained on.
- Most AI models use data from the internet, which can contain biases and stereotypes.
- If the training data is biased, the AI will also be biased.
- This can lead to unfair or harmful content being generated, reinforcing existing stereotypes and discrimination.

*Summarise why AI might be biased towards certain groups of people in your booklet.*


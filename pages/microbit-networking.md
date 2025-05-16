---
title: Micro:bit Networking
description: Learn how to connect multiple micro:bits together using radio communication.
layout: cover
class: text-center
background: /img/microbit-bg.webp
hideInToc: false
transition: fade
---

# Micro:bit Networking

---
layout: center
---

# What is a Network?

A network is a group of devices that are connected together to share information and resources. 

In the case of micro:bits, we can connect multiple devices to communicate with each other using radio signals.

---
layout: center
---

# Messaging

For our micro:bits to communicate, we need to:

- **Send messages**: One micro:bit sends a message to another micro:bit.
- **Receive messages**: The other micro:bit receives the message and can respond or take action based on it.
- **Know which messages are for us**: We need to set up a way to ensure that only the intended recipient can read the message.

---
layout: two-cols-header
---

# Receiving a Message

To receive a message from another micro:bit, we can use the radio module built into the micro:bit. The radio module allows us to send and receive messages wirelessly.

::left::

```python
from microbit import *

import radio
radio.on()  # Turn on the radio
radio.config(group=1)  # Set the channel to 1

while True:
    # Check for incoming messages
    incoming = radio.receive()  
    
    if incoming:
         # Scroll the incoming message 
        display.scroll(incoming) 
```
::right::  

<div class="note" style="font-size:90%">

## Step by Step

1. **Import Libraries** - including the radio library which is new for us.
2. **Turn on Radio** - Use `radio.on()` to turn on the radio module.
3. **Set Group** - Use `radio.config(group=1)` to set the radio group to 1. Only devices in the same group can communicate with each other. You can set the group to any number between 0 and 255.
4. **Receive Messages** - Use `radio.receive()` to check for incoming messages. *If* a message is received, scroll it on the display using `display.scroll(incoming)`.

</div>

---
layout: two-cols-header
---

# Sending a Message

To send a message from one micro:bit to another, we can use the radio module built into the micro:bit. The radio module allows us to send and receive messages wirelessly.

::left::

```python
from microbit import *
import radio

radio.on()  # Turn on the radio
radio.config(group=7)  # Set the channel to 7

while True:
    # Check if button A is pressed
    if button_a.is_pressed(): 
        radio.send("Hello!")  # Send a message 
        display.show("S")  # Show "S" for sent
    
    # Check for incoming messages
    incoming = radio.receive()  
    
    if incoming:
         # Scroll the incoming message 
        display.scroll(incoming) 
```

::right::

## Step by Step

<div style="font-size:80%">

- **Import Libraries**
- **Turn on Radio**: Use `radio.on()` to turn on the radio module.
- **Set Channel**: Use `radio.config(channel=7)` to set the radio channel to 7. 
- **Button Press**: Check if button A is pressed using `button_a.is_pressed()`
- **Send Message**: Use `radio.send("Hello!")` to send a message
- **Display Sending**: Show "S" on the display to indicate that a message is being sent.
- **Receive Messages**: Use `radio.receive()` to check for incoming messages. If a message is received, scroll it on the display using `display.scroll(incoming)`.

</div>

---
layout: center
zoom: 1.3
---

# Why do you think we need to set a channel?

<v-clicks>

- To avoid interference with other devices using the same frequency.
- To ensure that only devices on the same channel can communicate with each other.
- To allow multiple groups of micro:bits to operate independently in the same area.

</v-clicks>

---
layout: center
---

# Sending a Message without anyone else knowing (Offline Activity)

- We can set a **group** to the radio module to ensure that only devices in the same group can communicate with each other.
- But if a random person is using the same channel, they can still read our messages.
- To prevent this, we would use **encryption** to scramble our messages so that only the intended recipient can read them.
- Encryption is like a secret code that only the sender and receiver know how to read.
- This way, even if someone else intercepts the message, they won't be able to understand it without the key to decrypt it 

---
layout: center
---

# Challenge 1 - Create our own encryption method

In groups of 2 or 3, decide on a secret code to use for your messages.

1. You can use a simple substitution cipher, where each letter is replaced by another letter or symbol.
2. For example, you could replace "A" with "X", "B" with "Y", and so on.
3. Or you could use a more complex code, like a number system where each letter corresponds to a number (A=1, B=2, C=3, etc.).
4. Each group member create a test message:
    - Encrypt the message using your secret code.
    - Pass the encrypted message to another group member.
5. Decrypt the message you were given by reversing the secret code.

## Example
- Original Message: "HELLO"
- Substitution Cipher: Shift each letter by 1 (A → B, B → C, C → D, Z → A etc.)
- Encrypted Message: "IFMMP"

---
layout: center
---

# Challenge 2 - Create a program to send and receive messages

- Make two micro:bits talk to each other using radio.
- Change your messages into your secret code before sending.
- Turn the secret code back into normal words when you get a message.
- Use `radio.send()` to send messages and `radio.receive()` to get messages.

---

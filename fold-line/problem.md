# Fold-Line

- Namespace: picoctf/ronghaon
- ID: fold-line
- Type: custom
- Category: Cryptography
- Points: 1
- Templatable: no
- MaxUsers: 0

## Description

You have intercepted a letter believed to contain a secret message encoded using
the fold-line method. At first glance, the letter appears to be a regular piece
of text, but hidden within it lies a 36-character secret message.

## Details

The fold-line method involves first folding the letter paper a few times in both
vertical and horizontal directions and then flattening it out. At this point, the
message you intend to transmit is separated sequentially and written on the intersection
points of the fold lines, one character per intersection.

After completing the important information, the blank spaces are filled with a regular
public message, making an effort to seamlessly connect the public text with the secret
message. In this way, a simple encrypted letter is created.

To decrypt:

- Extract the characters from the intersection points of the fold lines.
- Organize the characters sequentially to reveal the hidden message.

What we know about the letter is that it contains a 36-character secret message
and it is distributed in a 6x6 grid.

Download the letter {{url_for("cipher.txt", "here")}}.

## Hints

- The 6x6 grid is evenly distributed across the letter.
- The letter may also include padding on all borders, further obscuring the grid’s
  structure and the hidden message.

## Solution Overview

From the description, we know that the letter contains a 36-character secret, organized
as a 6x6 grid. This 6x6 grid is evenly distributed within the 24x26 grid letter.
Based on this, we can deduce that the gap between each secret character is 3 characters
(both between fold rows and fold columns). The only unknown is the padding—or, in
other words, the starting point of the 6x6 secret grid.

The solution is to try all possible starting points. Since we know the secret should
be a piece of English text, we can examine all the possible candidates and identify
the correct one.

The code to solve this challenge can be found in `solver/solve.py`.

## Challenge Options

```yaml
cpus: 0.5
memory: 128m
pidslimit: 20
ulimits:
  - nofile=128:128
diskquota: 64m
init: true
```

## Learning Objective

Understand the fold-line method of encryption.

## Tags

## Attributes

- author: Ronghao Ni
- organization: picoCTF
- event: 18739-D Assignment

# Fold Line README

This challenge is a cryptography CTF challenge that involves understanding the
fold-line method of encoding secret messages. The fold-line method involves
folding a letter paper a few times in both vertical and horizontal directions
and then flattening it out. The message is then written on the intersection
points of the fold lines, one character per intersection. The challenge requires
the player to extract the characters from the intersection points of the fold
lines and organize them sequentially to reveal the hidden message.

## File Structure

- `cipher.txt`: The letter containing the encoded secret message.
- `flag.txt`: The flag for the challenge.
- `Dockefile`: The Dockerfile for building the challenge image.
- `problem.md`: The problem statement for the challenge (parsed by `cmgr`).
- `solver/solve.py`: The solution script for the challenge.
- `README.md`: This file.

## Setup with `cmgr` (borrowed from example picoCTF challenges)

1. You have `cmgr` installed and configured.

   - Refer to the
     [setup page](https://github.com/picoCTF/start-problem-dev/blob/master/setup-cmgr.md)
     if this is not the case for you.

2. copy this challenge directory to the `cmgr/challenges` directory (or other
   directories that `CMGR_DIR` environment variable points to).

3. Run `cmgr update` and `cmgr playtest picoctf/ronghaon/fold-line`

4. Visit the link provided in the output to access the challenge.

## Possible Solution

See `solver/solve.py` for a possible solution to this challenge.

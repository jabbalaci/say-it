#!/usr/bin/env python3

from gtts import gTTS

TEXT = """
Python is an interpreted, high-level and general-purpose programming
language. Created by Guido van Rossum and first released in 1991, Python's
design philosophy emphasizes code readability with its notable use of
significant whitespace. Its language constructs and object-oriented
approach aim to help programmers write clear, logical code for small
and large-scale projects.

Python is dynamically typed and garbage-collected. It supports multiple
programming paradigms, including structured (particularly, procedural),
object-oriented, and functional programming. Python is often described as
a "batteries included" language due to its comprehensive standard library.
""".replace("\n", " ")


def main():
    tts = gTTS(text=TEXT, lang='en')
    tts.save("audio.mp3")
    print("done")

##############################################################################

if __name__ == "__main__":
    main()

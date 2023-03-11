#!/usr/bin/env python3

import sys

from gtts import gTTS


def read_file(fname):
    with open(fname) as f:
        return f.read().strip().replace("\n", " ")


def main():
    fname = sys.argv[1]
    text = read_file(fname)
    #
    tts = gTTS(text=text, lang='en')
    tts.save(f"out.mp3")
    #
    print("done")

##############################################################################

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: provide an input file (the text to read)")
        sys.exit(1)
    # else
    main()

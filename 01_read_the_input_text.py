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
    print("# working...")
    tts = gTTS(text=text, lang="en")
    tts.save("out.mp3")
    #
    print("# out.mp3 was saved")


##############################################################################

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: provide an input file (the text to read)")
        sys.exit(1)
    # else
    main()

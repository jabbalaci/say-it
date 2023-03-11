#!/usr/bin/env python3

"""
Required programs:

* mplayer
* sox

Make sure they are installed and available in the command line.
"""

import os
import readline

from gtts import gTTS
from yachalk import chalk

VERSION = "v0.1.0"

SLOW = "slow.mp3"
FASTER = "faster.mp3"
TEMPO = 1.1  # 110%, i.e. 10% faster


def print_header():
    text = f"""
Say It {VERSION} by Jabba Laci
https://github.com/jabbalaci/say-it

r        - repeat the word
q        - quit
""".strip()
    print(text)
    print()


def play(mp3):
    if not os.path.isfile(mp3):
        print(f"Warning: {mp3} is not found")
        return
    # else
    cmd = f"mplayer {mp3} 1>/dev/null 2>/dev/null"
    # print("#", cmd)
    os.system(cmd)


def save(text: str) -> None:
    tts = gTTS(text=text, lang="en")
    tts.save(SLOW)
    cmd = f"sox {SLOW} {FASTER} tempo {TEMPO}"
    # print("#", cmd)
    os.system(cmd)


def main():
    print_header()

    while True:
        try:
            text = input(f"{chalk.bold('say_it>')} ").strip()
        except (KeyboardInterrupt, EOFError):
            print()
            break
        # else
        if text == "q":
            break
        elif text == "r":
            play(FASTER)
            continue
        elif text == "":
            continue
        # else
        save(text)
        play(FASTER)
    #
    print("bye")


##############################################################################

if __name__ == "__main__":
    main()

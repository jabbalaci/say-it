# Say It

Convert arbitrary text to audio.

## say_it.py

```
$ ./say_it.py
Say It v0.1.0 by Jabba Laci
https://github.com/jabbalaci/say-it

r        - repeat the word
q        - quit

say_it> hello world
say_it>
```

Here you get an interactive prompt. Type in some text, press Enter, and the program reads your
text aloud. The text is also saved in .mp3 format.

The text to speech transformation is done
with the [gtts](https://github.com/pndurette/gTTS) library. However, the resulting
audio is a bit slow. Using the Linux command `sox`,
the playback is sped up by 10%, which is
closer to normal speed in my opinion.

## 01_read_the_input_text.py

```
$ ./01_read_the_input_text.py examples/python.txt
# working...
# out.mp3 was saved
```

It's a variation of the previous. The difference is that the text is read from a file. The
output is saved to the file `out.mp3`.

```
$ ./02_play_out_mp3.sh
```

It plays back the previously created audio file
in normal (i.e., 110%) speed.

## Required programs

* mplayer
* sox

Make sure they are installed and available in the command line.

### Supported platforms

I only tried it under Linux.

## What is it good for?

It can be integrated in other programs. For instance, you have a book in PDF and you want
to turn it into an audiobook.

Or, you can quickly check the pronunciation of a word. Etc.

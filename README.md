
# number_pieces.py


### What is number_pieces.py?
number_pieces.py is a program written in the Python programming language that composes and generates sheet music for pieces in the style of John Cage’s “Five”. John Cage’s Number Pieces vary in form, so I chose to emulate the way he created “Five.” “Five” is a piece that lasts five minutes, written in parts for five players. Each part has five measures. The measures are played according to time-brackets which allow the player to choose when to begin and end a measure between the brackets. 20 of the measures are given different brackets chosen through some random process, while the third measure of the piece, the middle measure, begins and ends at the same time for all five players. Each measure has between 1 and 3 randomly selected notes, straying from the pattern of fives. Given this information, I interpreted the constraints of
a “number piece” given a piece called “N”:
- Length: N minutes
- N parts
- N measures per part
- 2-4 times per measure (at least one starting time and one ending time with the option of more if the player should be able to choose when to start from a range of times)
- Strict timing for center-point of piece (two different choices depending on whether N is even or odd)
- 1-3 random notes per measure

I decided to add a couple more constraints to make number_pieces.py compositions differ in a larger way from the example by John Cage. These constraints are as follow:
- Each time increment for brackets should be a multiple of N
- Given a scale when beginning the piece, any time a note in the scale is played N times, it should be removed from the scale and a new non-scale note should replace it

These constraints make the number in the number piece more significant, and also slowly change the mood of the piece. Using all these constraints, it is now time to generate and play a piece!

### How do I use number_pieces.py?
number_pieces.py is a Python program that uses a Python library. This means you need a compatible version of Python as well as the library installed.
number_pieces.py was written in Python 2.7.13, and should work with any new version of Python 2.7. If you have Python and the Python package installer PIP installed, you can open your terminal or command prompt window and type:

`pip install reportlab`

This should install the necessary library and allow you to run number_pieces.py. Once you have the necessary software installed, you can run number_pieces.py from your terminal or command prompt window with the command:

`python number_pieces.py N k`

where “N” is the number of the number piece, and k is a number from zero to twelve defining the starting note of the key where zero is C. If you don’t include an N or k, default values will be used.

Running this command spits out a file in the same folder as number_pieces.py named Number_Piece_N_in_k.pdf, where N is the number of the number piece and k is the key. This file contains the parts as well as instructions for how to play the number piece.

The instructions included in the piece can be read below:

> The parts are for voices or instruments or mixture of voices and instruments having the ability to play a twelve tone scale in a two octave range of their choice. All parts begin in the directed key and slowly (or rapidly, diverge). Time brackets are given. As in John Cage's number pieces:
> 
> Within these brackets the durations of tones are free, as are their beginnings and endings, which should be "brushed" in and out rather than turned on and off. It is recommended you use a large stopwatch visible to all performers, or synchronized stopwatches that can be started and stopp
>
>An explanation for how to read and perform the piece:
>
> "The timings in minutes and seconds used in what are now known as the "number" pieces by John Cage are called time brackets. The time brackets that appear to the left of each staff indicate a period of time during which the music on that staff must begin. The time brackets to the right indicate a period of time during which the music on that staff must end. These are flexible time brackets that overlap. The exact placement and duration of the music is free within these limitations. Some of the time brackets (those without arrows) are fixed meaning that the music must begin and end at exactly those periods of time. There should be no attempt to coordinate the different parts." Take breaths whenever you need to.

### Is there a future for number_pieces.py?
Maybe.

I would like to continue to develop certain aspects of the program which currently limit its ability. One specific problem I would like to fix is the fact that you are currently limited in the number you can use. Currently only number pieces in the 2 to 20 range work correctly, something I hope to remedy in the future to allow for number pieces where 100 players or more are possible.

I would also like to implement time division. That way you can change the length of time you would like a piece to be performed for without changing the number of players. For example a piece written for 100 players would last an hour and 40 minutes, but if we could make it shorter by dividing the time by two or four or more, it might be more reasonable to play the piece in 50 or 25 minutes instead.  It might also be interesting to allow for choice in the beginning scale. Currently the scale of available notes is set as major, but I would like to allow for the user to define a scale in the form of:

`[1,0,1,0,1,1,0,1,0,1,0,1]`

where 1s are notes in the scale (notes that are turned on) and 0s are notes not in the scale (notes that are turned off) for a twelve tone system. This scale definition could be stored in a text file or allowed as a command line variable (like N or k) in order to allow the scale to be as customized as possible. Options could include a common scale like major or minor, or even a scale with only one note value turned on.

# Calibration assist
### Used to assess accuracy in human signal detection tasks.

Assumes the signal detection task is strctured as a series of blocks of n trials at a given difficulty level.

How to use:
 - first indicate whether you are calibrating words or phrases

 - if words:
    - `y`: correct response
    - `n`: incorrect response
 
 - if phrases:
    - enter the number of lexical categories in the phrase that the subject correctly
   	 indentifies
    - then enter the path to .csv file

 - for both:
 - `new`: initiate new block
 - `export`: export settings as .csv  
 	- includes info about: participant ID, noise levels, signal levels, and actuator placement
 - `reset`: reset current block data
 - `exit`: nicely exits the program

Set `consoleSys` to `"windows"` or `"unix"` for prettier formatting.

Requires python 2.7.

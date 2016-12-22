# Calibration assist
### Used to assess accuracy in human signal detection tasks.

Assumes the signal detection task is strctured as a series of blocks of n trials at a given difficulty level.

How to use:
 - `y`: correct response
 - `n`: incorrect response
 - `new`: initiate new block
 - `export`: export settings as .csv  
 	- includes info about: participant ID, noise levels, signal levels, and actuator placement
 - `reset`: reset current block data
 - `done`: nicely exits the program

Set `consoleSys` to `"windows"` or `"unix"` for prettier formatting.

Requires python 2.7.

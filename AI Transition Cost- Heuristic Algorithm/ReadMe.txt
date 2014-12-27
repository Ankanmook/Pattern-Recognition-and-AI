Run the program with:

    python rblock.py <puzzle_file>

The output will be a series of lines like this:

    NORTH -> 2, 6, 3

which is of the form :

move direction -> Top Face of the Die, North Face of Die, East Face of Die
  

-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
Test Case 1:

Euclidean distance:
Direction -> Die-Face, Die-North, Die-East
SOUTH -> 2, 6, 3
EAST -> 4, 6, 2
EAST -> 5, 6, 4
EAST -> 3, 6, 5
EAST -> 2, 6, 3
NORTH -> 1, 2, 3
13 visited out of 19 generated.
Total Moves : 6
Manhattan distance:
Direction -> Die-Face, Die-North, Die-East
SOUTH -> 2, 6, 3
EAST -> 4, 6, 2
EAST -> 5, 6, 4
EAST -> 3, 6, 5
EAST -> 2, 6, 3
NORTH -> 1, 2, 3
16 visited out of 22 generated.
Total Moves : 6
Breadth First Search distance:
Direction -> Die-Face, Die-North, Die-East
SOUTH -> 2, 6, 3
EAST -> 4, 6, 2
EAST -> 5, 6, 4
EAST -> 3, 6, 5
EAST -> 2, 6, 3
NORTH -> 1, 2, 3
16 visited out of 22 generated.
Total Moves : 6

-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
Test Case 2:

Euclidean distance:
Direction -> Die-Face, Die-North, Die-East
SOUTH -> 2, 6, 3
EAST -> 4, 6, 2
NORTH -> 1, 4, 2
WEST -> 2, 4, 6
SOUTH -> 4, 5, 6
SOUTH -> 5, 3, 6
SOUTH -> 3, 2, 6
EAST -> 1, 2, 3
SOUTH -> 2, 6, 3
EAST -> 4, 6, 2
EAST -> 5, 6, 4
EAST -> 3, 6, 5
NORTH -> 1, 3, 5
WEST -> 5, 3, 6
NORTH -> 4, 5, 6
EAST -> 1, 5, 4
62 visited out of 82 generated.
Total Moves : 16
Manhattan distance:
Direction -> Die-Face, Die-North, Die-East
SOUTH -> 2, 6, 3
EAST -> 4, 6, 2
NORTH -> 1, 4, 2
WEST -> 2, 4, 6
SOUTH -> 4, 5, 6
SOUTH -> 5, 3, 6
SOUTH -> 3, 2, 6
EAST -> 1, 2, 3
SOUTH -> 2, 6, 3
EAST -> 4, 6, 2
EAST -> 5, 6, 4
EAST -> 3, 6, 5
NORTH -> 1, 3, 5
WEST -> 5, 3, 6
NORTH -> 4, 5, 6
EAST -> 1, 5, 4
61 visited out of 80 generated.
Total Moves : 16
Breadth First Search distance:
Direction -> Die-Face, Die-North, Die-East
SOUTH -> 2, 6, 3
EAST -> 4, 6, 2
NORTH -> 1, 4, 2
WEST -> 2, 4, 6
SOUTH -> 4, 5, 6
SOUTH -> 5, 3, 6
SOUTH -> 3, 2, 6
EAST -> 1, 2, 3
SOUTH -> 2, 6, 3
EAST -> 4, 6, 2
EAST -> 5, 6, 4
EAST -> 3, 6, 5
NORTH -> 1, 3, 5
WEST -> 5, 3, 6
NORTH -> 4, 5, 6
EAST -> 1, 5, 4
61 visited out of 83 generated.
Total Moves : 16

-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
Test Case 3:


Euclidean distance:
Direction -> Die-Face, Die-North, Die-East
SOUTH -> 2, 6, 3
EAST -> 4, 6, 2
EAST -> 5, 6, 4
EAST -> 3, 6, 5
EAST -> 2, 6, 3
NORTH -> 1, 2, 3
EAST -> 4, 2, 1
NORTH -> 5, 4, 1
NORTH -> 3, 5, 1
NORTH -> 2, 3, 1
WEST -> 1, 3, 5
SOUTH -> 3, 6, 5
EAST -> 2, 6, 3
NORTH -> 1, 2, 3
19 visited out of 20 generated.
Total Moves : 14
Manhattan distance:
Direction -> Die-Face, Die-North, Die-East
SOUTH -> 2, 6, 3
EAST -> 4, 6, 2
EAST -> 5, 6, 4
EAST -> 3, 6, 5
EAST -> 2, 6, 3
NORTH -> 1, 2, 3
EAST -> 4, 2, 1
NORTH -> 5, 4, 1
NORTH -> 3, 5, 1
NORTH -> 2, 3, 1
WEST -> 1, 3, 5
SOUTH -> 3, 6, 5
EAST -> 2, 6, 3
NORTH -> 1, 2, 3
19 visited out of 20 generated.
Total Moves : 14
Breadth First Search distance:
Direction -> Die-Face, Die-North, Die-East
SOUTH -> 2, 6, 3
EAST -> 4, 6, 2
EAST -> 5, 6, 4
EAST -> 3, 6, 5
EAST -> 2, 6, 3
NORTH -> 1, 2, 3
EAST -> 4, 2, 1
NORTH -> 5, 4, 1
NORTH -> 3, 5, 1
NORTH -> 2, 3, 1
WEST -> 1, 3, 5
SOUTH -> 3, 6, 5
EAST -> 2, 6, 3
NORTH -> 1, 2, 3
19 visited out of 20 generated.
Total Moves : 14

-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
Test Case 4:


Euclidean distance:
Direction -> Die-Face, Die-North, Die-East
SOUTH -> 2, 6, 3
EAST -> 4, 6, 2
NORTH -> 1, 4, 2
WEST -> 2, 4, 6
SOUTH -> 4, 5, 6
SOUTH -> 5, 3, 6
SOUTH -> 3, 2, 6
SOUTH -> 2, 4, 6
EAST -> 1, 4, 2
NORTH -> 3, 1, 2
WEST -> 2, 1, 4
WEST -> 4, 1, 5
WEST -> 5, 1, 3
WEST -> 3, 1, 2
SOUTH -> 1, 4, 2
WEST -> 2, 4, 6
NORTH -> 3, 2, 6
NORTH -> 5, 3, 6
NORTH -> 4, 5, 6
NORTH -> 2, 4, 6
EAST -> 1, 4, 2
116 visited out of 140 generated.
Total Moves : 21
Manhattan distance:
Direction -> Die-Face, Die-North, Die-East
SOUTH -> 2, 6, 3
EAST -> 4, 6, 2
NORTH -> 1, 4, 2
WEST -> 2, 4, 6
SOUTH -> 4, 5, 6
SOUTH -> 5, 3, 6
SOUTH -> 3, 2, 6
SOUTH -> 2, 4, 6
EAST -> 1, 4, 2
NORTH -> 3, 1, 2
WEST -> 2, 1, 4
WEST -> 4, 1, 5
WEST -> 5, 1, 3
WEST -> 3, 1, 2
SOUTH -> 1, 4, 2
WEST -> 2, 4, 6
NORTH -> 3, 2, 6
NORTH -> 5, 3, 6
NORTH -> 4, 5, 6
NORTH -> 2, 4, 6
EAST -> 1, 4, 2
105 visited out of 129 generated.
Total Moves : 21
Breadth First Search distance:
Direction -> Die-Face, Die-North, Die-East
SOUTH -> 2, 6, 3
EAST -> 4, 6, 2
NORTH -> 1, 4, 2
WEST -> 2, 4, 6
SOUTH -> 4, 5, 6
SOUTH -> 5, 3, 6
SOUTH -> 3, 2, 6
SOUTH -> 2, 4, 6
EAST -> 1, 4, 2
NORTH -> 3, 1, 2
WEST -> 2, 1, 4
WEST -> 4, 1, 5
WEST -> 5, 1, 3
WEST -> 3, 1, 2
SOUTH -> 1, 4, 2
WEST -> 2, 4, 6
NORTH -> 3, 2, 6
NORTH -> 5, 3, 6
NORTH -> 4, 5, 6
NORTH -> 2, 4, 6
EAST -> 1, 4, 2
114 visited out of 139 generated.
Total Moves : 21

-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
Test Case 5:

Euclidean distance:
Direction -> Die-Face, Die-North, Die-East
WEST -> 3, 2, 6
SOUTH -> 2, 4, 6
SOUTH -> 4, 5, 6
SOUTH -> 5, 3, 6
SOUTH -> 3, 2, 6
SOUTH -> 2, 4, 6
SOUTH -> 4, 5, 6
EAST -> 1, 5, 4
SOUTH -> 5, 6, 4
WEST -> 4, 6, 2
WEST -> 2, 6, 3
WEST -> 3, 6, 5
WEST -> 5, 6, 4
WEST -> 4, 6, 2
WEST -> 2, 6, 3
WEST -> 3, 6, 5
WEST -> 5, 6, 4
WEST -> 4, 6, 2
WEST -> 2, 6, 3
NORTH -> 1, 2, 3
WEST -> 3, 2, 6
SOUTH -> 2, 4, 6
SOUTH -> 4, 5, 6
SOUTH -> 5, 3, 6
SOUTH -> 3, 2, 6
SOUTH -> 2, 4, 6
EAST -> 1, 4, 2
NORTH -> 3, 1, 2
WEST -> 2, 1, 4
SOUTH -> 1, 5, 4
2832 visited out of 3069 generated.
Total Moves : 30
Manhattan distance:
Direction -> Die-Face, Die-North, Die-East
WEST -> 3, 2, 6
SOUTH -> 2, 4, 6
SOUTH -> 4, 5, 6
SOUTH -> 5, 3, 6
SOUTH -> 3, 2, 6
SOUTH -> 2, 4, 6
SOUTH -> 4, 5, 6
SOUTH -> 5, 3, 6
SOUTH -> 3, 2, 6
SOUTH -> 2, 4, 6
SOUTH -> 4, 5, 6
EAST -> 1, 5, 4
SOUTH -> 5, 6, 4
WEST -> 4, 6, 2
WEST -> 2, 6, 3
WEST -> 3, 6, 5
WEST -> 5, 6, 4
WEST -> 4, 6, 2
WEST -> 2, 6, 3
WEST -> 3, 6, 5
WEST -> 5, 6, 4
WEST -> 4, 6, 2
WEST -> 2, 6, 3
WEST -> 3, 6, 5
NORTH -> 1, 3, 5
EAST -> 2, 3, 1
SOUTH -> 3, 5, 1
WEST -> 1, 5, 4
2018 visited out of 2316 generated.
Total Moves : 28
Breadth First Search distance:
Direction -> Die-Face, Die-North, Die-East
WEST -> 3, 2, 6
SOUTH -> 2, 4, 6
SOUTH -> 4, 5, 6
SOUTH -> 5, 3, 6
SOUTH -> 3, 2, 6
SOUTH -> 2, 4, 6
SOUTH -> 4, 5, 6
SOUTH -> 5, 3, 6
SOUTH -> 3, 2, 6
SOUTH -> 2, 4, 6
SOUTH -> 4, 5, 6
EAST -> 1, 5, 4
SOUTH -> 5, 6, 4
WEST -> 4, 6, 2
WEST -> 2, 6, 3
WEST -> 3, 6, 5
WEST -> 5, 6, 4
WEST -> 4, 6, 2
WEST -> 2, 6, 3
WEST -> 3, 6, 5
WEST -> 5, 6, 4
WEST -> 4, 6, 2
WEST -> 2, 6, 3
WEST -> 3, 6, 5
NORTH -> 1, 3, 5
EAST -> 2, 3, 1
SOUTH -> 3, 5, 1
WEST -> 1, 5, 4
2018 visited out of 2316 generated.
Total Moves : 28

-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
Test Case 6:

Euclidean distance:
Direction -> Die-Face, Die-North, Die-East
NORTH -> 5, 1, 3
EAST -> 4, 1, 5
EAST -> 2, 1, 4
EAST -> 3, 1, 2
EAST -> 5, 1, 3
SOUTH -> 1, 2, 3
EAST -> 4, 2, 1
SOUTH -> 2, 3, 1
SOUTH -> 3, 5, 1
SOUTH -> 5, 4, 1
WEST -> 1, 4, 2
NORTH -> 3, 1, 2
EAST -> 5, 1, 3
SOUTH -> 1, 2, 3
19 visited out of 20 generated.
Total Moves : 14
Manhattan distance:
Direction -> Die-Face, Die-North, Die-East
NORTH -> 5, 1, 3
EAST -> 4, 1, 5
EAST -> 2, 1, 4
EAST -> 3, 1, 2
EAST -> 5, 1, 3
SOUTH -> 1, 2, 3
EAST -> 4, 2, 1
SOUTH -> 2, 3, 1
SOUTH -> 3, 5, 1
SOUTH -> 5, 4, 1
WEST -> 1, 4, 2
NORTH -> 3, 1, 2
EAST -> 5, 1, 3
SOUTH -> 1, 2, 3
19 visited out of 20 generated.
Total Moves : 14
Breadth First Search distance:
Direction -> Die-Face, Die-North, Die-East
NORTH -> 5, 1, 3
EAST -> 4, 1, 5
EAST -> 2, 1, 4
EAST -> 3, 1, 2
EAST -> 5, 1, 3
SOUTH -> 1, 2, 3
EAST -> 4, 2, 1
SOUTH -> 2, 3, 1
SOUTH -> 3, 5, 1
SOUTH -> 5, 4, 1
WEST -> 1, 4, 2
NORTH -> 3, 1, 2
EAST -> 5, 1, 3
SOUTH -> 1, 2, 3
19 visited out of 20 generated.
Total Moves : 14

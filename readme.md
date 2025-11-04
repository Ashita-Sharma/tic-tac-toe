# Tic Tac Toe recreation

## Description
A basic recreation of the classic tic tac toe game using the pygame module.

## Game logic used
### Tic Tac Toe logic 
We start by making a nested list that will act as our game "board", in a sense. 
Here, we use the format of   

board =  
[
[None, None, None],  

[None, None, None],  

[None, None, None]
]  

where len(board) will represent the rows while len(board[1]) will represent the columns.

Using basic coordinate/array naming system, we can check if a cell with the values of (row_val, col_val) is empty, i.e. checking if the value stored is "None".

#### NOTE: 
Unlike normal array/matrix naming conventions, here the enumeration begins with "0" in accordance to the default Python indexing logic.


As we start with have two players, we can assign the character "X" to player 1 and character "O" to player 2.

We can create logic for a horizontal combination of three by checking the values of all 3 rows until we satisfy our condition.
Similar logic works for both diagonals and verticals.

The game is "won" when a player manages to satisfy the above mentioned winning condition(s).

### Control logic
For ease of controls, I/We shall use the built-in pygame "event" function to receive the values of mouse's horizontal and vertical coordinates.
With this, we can use the obtained values to check if the location where the mouse was pressed lies in any specific "box" on the board.
And so, we'll be able to use this knowledge to draw an "x" or an "o" upon the aforementioned "box".
(I'm not sure how to prevent the player from accidentally clicking on the grid lines and using their move yet. Perhaps an if/else conditional?)

## Organization of code
### Section 1: Importing of all used modules.
(right now[4/11/2025] only pygame is being used.)

### Section 2: Constants
All the constants used in the code, for ease of access and preventing any discrepancies 

### Section 3: functions
defining of all functions to be used.

### Section 4: Loop logic
Logic to be used while "running == true" is active.
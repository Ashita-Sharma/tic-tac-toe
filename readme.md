# tic tac toe recreation

## Description
A basic recreation of the classic tic tac toe game using the pygame module.

## Game logic used
### Tic Tac Toe logic 
We start by making a nested list that will act as our game "board", in a sense. 
Here, we use the format of
board = [[None, None, None],
         [None, None, None],
         [None, None, None]]
where len(board) will represent the rows while len(board[1]) will represent the columns.

Using basic coordinate/array naming system, we can check if a cell with the values of (row_val, col_val) is empty, i.e. checking if the value stored is "None".

As we start with have two players, we can assign the character "X" to player 1 and character "O" to player 2.

We can create logic for a horizontal combination of three by checking the values of all 3 rows until we satisfy our condition.
Similar logic works for both diagonals and verticals.

The game is "won" when a player manages to satisfy the above mentioned winning condition(s).

### Control logic
For ease of controls, I/We shall use the built-in pygame "event" function to receive the values of mouse's horizontal and vertical coordinates.
With this, we can use the obtained values to check if the location where the mouse was pressed lies in any specific "box" on the board.
And so, we'll be able to use this knowledge to draw an "x" or an "o" upon the aforementioned "box".

## Organization of code
### Section 1: Importing of all used modules.
(right now onl pygame is being used.)

### Section 2: Constants
All the constants used in the code, for ease of access and preventing any discrepancies 

### Section 3: functions
defining of all functions to be used.

### Section 4: Loop logic
Logic to be used while "running == true" is active.
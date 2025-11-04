# tic tac toe recreation

## Description
A basic recreation of the classic tic tac toe game using the pygame module.

## Game logic used
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

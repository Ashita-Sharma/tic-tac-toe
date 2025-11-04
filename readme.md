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
### Winning Logic
For horizontal, I used the following code:    

        for row in range(BOARD_ROWS):
            if board[row][0] == board[row][1] == board[row][2] == player:

Here, I iterated through the range (1,3), placing(inserting) the iterated numbers to access a specific row.
Then, I use a simple if conditional to check if the **current** player has won by confirming that all the values in a particular row are the same.
(The winning condition will always be applied to the **current** player and is placed before the turn switch in order to prevent any unforeseen errors.)

Similarly for vertical, I used the following code:    

        for col in range(BOARD_COLS):
            if board[0][col] == board[1][col] == board[2][col] == player:

It works the same as for the horizontal but here I iterated through the nested list(columns) instead of the outer list(rows).

For the diagonals, I used a very simple logic:    

    if board[0][0] == board[1][1] == board[2][2] == player:
        print("diagonal 1")
    elif board[0][2] == board[1][1] == board[2][0] == player:
        print("diagonal 2")

For both, I just directly used the values of the required row and column, but I assume it's possible to iterate the same way as we did for the previous two conditions.  

tldr:
We can create logic for a horizontal combination of three by checking the values of all 3 rows until we satisfy our condition.
Similar logic works for both diagonals and verticals.

The game is "won" when a player manages to satisfy the above-mentioned winning condition(s).

### Control logic
For ease of controls, I/We shall use the built-in pygame "event" function to receive the values of mouse's horizontal and vertical coordinates.
With this, we can use the obtained values to check if the location where the mouse was pressed lies in any specific "box" on the board.
And so, we'll be able to use this knowledge to draw an "x" or an "o" upon the aforementioned "box".
(I'm not sure how to prevent the player from accidentally clicking on the grid lines and using their move yet. Perhaps an if/else conditional?)

## Organization of code
### Section 1: Importing of all used modules.
(As of [4/11/2025], Pygame, Pyinstaller, Sys and OS are being used.)

### Section 2: Constants and Variables
All the constants used in the code, for ease of access and preventing any discrepancies.    
    
They are arranged in the following order in these respective categories: Screen, Grid, Status and Setup variables
### Section 3: Functions
Defining of all functions to be used.    
   
In the following order: Setup, Game logic, Winning Conditionals
### Section 4: Loop logic
Logic and code to be used while "running == true" is active.


### Section 0: Explanation of Pyinstaller
Basically a bootloader, it bootstraps the code, i.e. creates an application such that the code is able to run without using a complier or an interpreter such as pycharm or vs code.
When running PyInstaller code, it does the following:
1) Downloads all imported modules, if any.
2) A Build folder is created
3) A dist folder is created which contains the newly created application/executable
(The executable will execute the code required to run the program.)
4) To convert the project into a single application, ran the following in my terminal:     
   pyinstaller --onefile --noconsole --name="TicTacToe" main.py
5) When running an executable created by pyinstaller, it stores data files within a temp folder,
hence the need to start the code by making sure we direct the code to the correct folder where the data file(in this case, font file) is stored.

## Resources used
Here are all the resources I used to create this project:
### Pygame Official Documentation
https://www.pygame.org/docs/
### Stack Overflow
https://stackoverflow.com/questions
### Geeksforgeeks
https://www.geeksforgeeks.org/
### Python Land
https://python.land/
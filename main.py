import pygame

#to initialize pygame

pygame.init()
#<----------------CONSTANTS BEGIN HERE--------------->

#Screen constants
BOARD_COLS = 3
BOARD_ROWS = 3

BG_COLOR = (255, 209, 102)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700

# Square constants
SQUARE_SIZE = SCREEN_WIDTH // BOARD_COLS
SPACE = SQUARE_SIZE // 4
COLOR_X = (17, 138, 178)
COLOR_O = (239, 71, 111)
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 25
CROSS_WIDTH = 25

#Status constants
LINE_COLOR = (6, 214, 160)
DRAW_COLOR = (144, 122, 214)
LINE_WIDTH = 15
TEXT_COLOR = COLOR_O
STATUS_COLOR = LINE_COLOR
FONT_NAME = 'comic-sans-bold.ttf'
#setup of screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")


#basic setup of screen
board = [[None, None, None],
         [None, None, None],
         [None, None, None]]
player = 1  # considering initial player to be X
winner = None
game_over = False
row = len(board)
col = len(board[0])
def test_controls():

    #MOVED TO CORRECT LOCATION

    pass


def draw_grid():
    #to draw grid lines
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (SCREEN_WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (SCREEN_WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, SCREEN_WIDTH), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, SCREEN_WIDTH), LINE_WIDTH)

def draw_horizontal_line(row, player):
    if player == 1:
        pygame.draw.line(screen, COLOR_X, (20, SQUARE_SIZE*row + SQUARE_SIZE//2), (SCREEN_WIDTH-20, SQUARE_SIZE*row + SQUARE_SIZE//2), LINE_WIDTH)
    else:
        pygame.draw.line(screen, COLOR_O, (20, SQUARE_SIZE*row + SQUARE_SIZE//2), (SCREEN_WIDTH-20, SQUARE_SIZE*row + SQUARE_SIZE//2), LINE_WIDTH)
def draw_vertical_line(col, player):
    if player == 1:
        pygame.draw.line(screen, COLOR_X, (SQUARE_SIZE*col + SQUARE_SIZE//2, 20), (SQUARE_SIZE*col + SQUARE_SIZE//2, SCREEN_WIDTH-20), LINE_WIDTH)
    else:
        pygame.draw.line(screen, COLOR_O, (SQUARE_SIZE*col + SQUARE_SIZE//2, 20), (SQUARE_SIZE*col + SQUARE_SIZE//2, SCREEN_WIDTH-20), LINE_WIDTH)

def draw_diagonal_line_1(player):
    if player == 1:
        pygame.draw.line(screen, COLOR_X, (25, 25), (SQUARE_SIZE*2 + SQUARE_SIZE-25, SQUARE_SIZE*2 + SQUARE_SIZE-25), LINE_WIDTH+5)
    else:
        pygame.draw.line(screen, COLOR_O, (25,25), (SQUARE_SIZE*2 + SQUARE_SIZE-25, SQUARE_SIZE*2 + SQUARE_SIZE-25), LINE_WIDTH+10)

def draw_diagonal_line_2(player):
    if player == 1:
        pygame.draw.line(screen, COLOR_X, (SCREEN_WIDTH-25, 25), (25, SQUARE_SIZE*2 + SQUARE_SIZE-25), LINE_WIDTH+5)
    else:
        pygame.draw.line(screen, COLOR_O, (SCREEN_WIDTH-25, 25), (25, SQUARE_SIZE*2 + SQUARE_SIZE-25), LINE_WIDTH+10)

def draw_status():
    #to know whose turn it is
    pygame.draw.rect(screen, STATUS_COLOR, (0, SCREEN_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT - SCREEN_WIDTH))

    font = pygame.font.Font('FONT_NAME', 40)
    if game_over:
        if winner and player == 1:
            text = "Player X Wins!"
            color = COLOR_X
        elif winner and player ==2:
            text = "Player O Wins!"
            color = COLOR_O
        else:
            text = "It's a Draw!"
            color = DRAW_COLOR
    elif player == 1:
        z = "X"
        color = COLOR_X
        text = "Player X's turn"
    else:
        z = "O"
        color = COLOR_O
        text = f"Player O's Turn"

    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_WIDTH + 25))
    screen.blit(text_surface, text_rect) #block transferring (blit) of the text
    # Restart instruction
    if game_over:
        text2 = "Press R to Restart!"
        font2 = pygame.font.Font('FONT_NAME', 40)
        text_surface2 = font2.render(text2, True, color)
        text_rect2 = text_surface2.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_WIDTH + 70))

        screen.blit(text_surface2, text_rect2)


# To create logic for gameplay
def draw_figures():
    #drawing of x's and o's
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                # To draw X
                start_x = (col * SQUARE_SIZE) + SPACE
                start_y = (row * SQUARE_SIZE) + SPACE
                end_x = (col * SQUARE_SIZE + SQUARE_SIZE) - SPACE
                end_y = (row * SQUARE_SIZE + SQUARE_SIZE) - SPACE
                pygame.draw.line(screen, COLOR_X, (start_x, start_y), (end_x, end_y), CROSS_WIDTH)
                pygame.draw.line(screen, COLOR_X, (start_x, end_y), (end_x, start_y), CROSS_WIDTH)

            elif board[row][col] == 2:
                # To draw O
                center_x = (col * SQUARE_SIZE) + SQUARE_SIZE // 2
                center_y = (row * SQUARE_SIZE) + SQUARE_SIZE // 2
                pygame.draw.circle(screen, COLOR_O, (center_x, center_y), CIRCLE_RADIUS, CIRCLE_WIDTH)
#to assign a square to the CURRENT player
def mark_square(row, col, player):
    board[row][col] = player
#to check if square is available
def available_square(row,col):
    if board[row][col] == None:
        return True
    return False
def is_board_full():
    """Check if the board is full (draw)"""
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                return False
    return True

def winning_conditionals(player):
    # horizontal
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] == player:
            draw_horizontal_line(row, player)
            return True
    # vertical
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] == player:
            draw_vertical_line(col, player)
            return True
    # diagonal
    if board[0][0] == board[1][1] == board[2][2] == player:
        draw_diagonal_line_1(player)
        return True
    elif board[0][2] == board[1][1] == board[2][0] == player:
        draw_diagonal_line_2(player)
        return True
    return False


def draw_init():
    screen.fill(BG_COLOR)

def restart():
    global player, board, game_over, winner
    game_over = False
    winner = None
    draw_init()
    draw_grid()
    player = 1
    board = [[None, None, None],
             [None, None, None],
             [None, None, None]]

#to check if game is running
running = True

# THIS WAS THE REASON FOR ERROR!!!!
# 1) screen was being drawn AFTER the event conditionals
# 2) because the initialization and grid creation were in the while loop
# the screen was constantly being refreshed THAT'S WHY the code was not working!
draw_init()
draw_grid()

while running:

    draw_status()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #to quit the program when clicked on "x"
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            if mouseY < SCREEN_WIDTH:
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE\

                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, player)

                    if winning_conditionals(player):
                        game_over = True
                        winner = player

                    elif is_board_full():
                        game_over = True
                        winner = None
                        draw_status()

                    if player == 1 and not winning_conditionals(player):
                        # Switch player
                        player = 2
                    elif player == 2 and not winning_conditionals(player):
                        player = 1
                    draw_figures()
        elif game_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()



    pygame.display.update()


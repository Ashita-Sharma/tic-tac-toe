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
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25

#Status constants
LINE_COLOR =  	(6, 214, 160)
LINE_WIDTH = 15
TEXT_COLOR = COLOR_O
STATUS_COLOR = LINE_COLOR
#setup of screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")


#basic setup of screen
board = [[None, None, None],
         [None, None, None],
         [None, None, None]]
player = 1  # considering initial player to be X
winner = None
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


def draw_status():
    #to know whose turn it is
    pygame.draw.rect(screen, STATUS_COLOR, (0, SCREEN_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT - SCREEN_WIDTH))

    font = pygame.font.Font('Comic Sans MS 400.ttf', 40)
    text = f"Player's Turn"
    color = TEXT_COLOR

    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_WIDTH + 25))
    screen.blit(text_surface, text_rect) #block transferring (blit) of the text


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





def draw_init():
    screen.fill(BG_COLOR)


#to check if game is running
clock = pygame.time.Clock()
running = True

# THIS WAS THE REASON FOR ERROR!!!!
# 1) screen was being drawn AFTER the event conditionals
# 2) because the initialization and grid creation were in the while loop
# the screen was constantly being refreshed THAT'S WHY the code was not working!
draw_init()
draw_grid()

while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT: #to quit the program when clicked on "x"
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and running:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            if mouseY < SCREEN_WIDTH:
                clicked_row = mouseY // SQUARE_SIZE
                clicked_col = mouseX // SQUARE_SIZE
                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, player)
                    draw_figures()

    draw_status()
    pygame.display.update()
    clock.tick(60)


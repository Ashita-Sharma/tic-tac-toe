import pygame

#to initialize pygame

pygame.init()
#constants
COLS = 3
ROWS = 3

BG_COLOR = (228, 193, 249)
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700
SQUARE_SIZE = SCREEN_WIDTH // COLS
LINE_COLOR =  	(255, 239, 159)
LINE_WIDTH = 15
TEXT_COLOR = (255, 153, 200)
STATUS_COLOR = (255, 239, 159)
#setup of screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")


#basic setup of screen
board = [[None, None, None],
         [None, None, None],
         [None, None, None]]
player = 1  # considering initial player to be X
winner = None
def test_controls():

    pass

def draw_lines():
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
#to check if game is running
running = True

def draw_init():
    screen.fill(BG_COLOR)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #to quit the program when clicked on "x"
            running = False
    draw_init()
    draw_lines()
    draw_status()
    pygame.display.update()


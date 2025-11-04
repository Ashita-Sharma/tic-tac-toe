import pygame

#to initialize pygame

pygame.init()

BG_COLOR = (196, 175, 224)
#setup of screen
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Tic Tac Toe")

#to check if game is running
running = True

def draw_init():
    screen.fill(BG_COLOR)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #to quit the program when clicked on "x"
            running = False
    draw_init()
    pygame.display.update()


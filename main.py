import pygame

#to initialize pygame

pygame.init()


#setup of screen
screen = pygame.display.set_mode((720, 720))
pygame.display.set_caption("Tic Tac Toe")

#to check if game is running
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #to quit the program when clicked on "x"
            running = False
    pygame.display.update()


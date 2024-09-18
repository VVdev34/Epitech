import pygame

# Pygame set up 
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
running = True
keys = pygame.key.get_pressed()


# Set the caption for the game window
pygame.display.set_caption("My game window")

# Load the image from the specified file path
#image = pygame.image.load('img/background_img.jpeg') 
#screen.blit(image, (0,0))
while running:
    #poll for events
    #pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 


#flip() the display to put your work on screen
    pygame.display.flip()
    
    


    pygame.draw.circle(screen, "white", (300,100), 50)#Tete
    pygame.draw.line(screen, "white", (300,150),(300,400), width = 8)#Corps
    pygame.draw.line(screen, "white", (200,300),(300,200), width = 8)#B.gauche
    pygame.draw.line(screen, "white", (300,200),(400,300), width = 8)#B.droite
    pygame.draw.line(screen, "white", (200,500),(300,400), width = 8)#J.droite
    pygame.draw.line(screen, "white", (300,400),(400,500), width = 8)#J.gauche



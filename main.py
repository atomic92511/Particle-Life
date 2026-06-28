import pygame 

running = True
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    
    clock.tick(FPS)
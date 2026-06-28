import pygame 

running = True
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
red = (255,0,0)
particles = []
def add_particle(x,y):
    particles.append([x,y])
add_particle(400,300)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    for p in particles:
        particle = pygame.draw.circle(screen,red,(p[0],p[1]),10)
    clock.tick(FPS)
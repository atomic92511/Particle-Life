
import pygame 
import math
import random
running = True
FPS = 120
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
red = (255,0,0)
blue = (0,0,255)
particles = []


effect_rad = 100
part_count = 250
force_sim_speed = 2
particle_rad = 5
friction = 0.8

def add_particle(x,y,color):
    particles.append([x,y,0,0,color])
def get_dist(p1,p2):
    return math.dist(p1,p2)
for i in range(part_count):
    color = random.randint(0,1)
    if color == 0:
        add_particle(random.randint(0,800),random.randint(0,600),"red")
    elif color == 1:
            add_particle(random.randint(0,800),random.randint(0,600),"blue")
while running:
    mx,my = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if pygame.mouse.get_pressed()[0]:
        add_particle(mx,my,"blue")
    for p in particles:
        p[2] = 0
        p[3] = 0
    for i in range(len(particles)):
        for j in range(i + 1,len(particles)):
            part1 = particles[i]
            part2 = particles[j]
            dist = get_dist((part1[0],part1[1]),(part2[0],part2[1]))
            if dist == 0:
                continue
            dx = part2[0] - part1[0]
            dy = part2[1] - part1[1]
            nx = dx / dist
            ny = dy / dist
            if dist < effect_rad and not dist < particle_rad + 10:
                if part1[4] == "red":
                    if part2[4] != "blue":
                        part1[2] = nx * force_sim_speed
                        part1[3] = ny * force_sim_speed
                        part2[2] = nx * force_sim_speed
                        part2[3] = ny * force_sim_speed
                    elif part2[4] == "blue":
                        part1[2] = nx * force_sim_speed
                        part1[3] = ny * force_sim_speed
                        part2[2] = nx * force_sim_speed
                        part2[3] = ny * force_sim_speed
                elif part1[4] == "blue":
                        if part2[4] != "blue":
                            part1[2] = -nx * force_sim_speed
                            part1[3] = -ny * force_sim_speed
                            part2[2] = -nx * force_sim_speed
                            part2[3] = -ny * force_sim_speed
                        if part2[4] == "blue":
                            part1[2] = nx * force_sim_speed
                            part1[3] = ny * force_sim_speed
                            part2[2] = nx * force_sim_speed
                            part2[3] = nx * force_sim_speed
                                        
            elif dist < effect_rad and dist < particle_rad + 10:
                part1[2] = nx * force_sim_speed
                part1[3] = ny * force_sim_speed
                part2[2] = nx * force_sim_speed
                part2[3] = ny * force_sim_speed
                min_dist = (particle_rad * 2) - 1
                if dist < min_dist:
                    overlap = min_dist - dist
                    push_x = (dx / dist) * overlap * 0.9
                    push_y = (dy / dist) * overlap * 0.9
                    
                    part1[0] -= push_x
                    part1[1] -= push_y
                    part2[0] += push_x
                    part2[1] += push_y
    for p in particles:
        p[0] += p[2]
        p[1] += p[3]
        p[2] *= friction
        p[3] *= friction
        if p[0] > 800:
            p[0] = 0
        if p[0] < 0:
            p[0] = 800
        if p[1] < 0:
            p[1] = 600
        if p[1] > 600:
            p[1] = 0
    screen.fill((0,0,0))
    for p in particles:
        if p[4] == "red":
            particle = pygame.draw.circle(screen,red,(p[0],p[1]),particle_rad)
        elif p[4] == "blue":
            particle = pygame.draw.circle(screen,blue,(p[0],p[1]),particle_rad)
    pygame.display.flip()
    clock.tick(FPS)
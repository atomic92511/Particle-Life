import pygame 
import math
import random
running = True
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
red = (255,0,0)
particles = []


effect_rad = 100
part_count = 500
force_sim_speed = 0.05
particle_rad = 5

def add_particle(x,y):
    particles.append([x,y,0,0])
def get_dist(p1,p2):
    return math.dist(p1,p2)
for i in range(part_count):
    add_particle(random.randint(0,800),random.randint(0,600))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in range(len(particles) - 1):
        for j in range(i + 1,len(particles) - 1):
            part1 = particles[i]
            part2 = particles[j]
            dist = get_dist((part1[0],part1[1]),(part2[0],part2[1]))
            if dist == 0:
                continue
            dx = part2[0] - part1[0]
            dy = part2[1] - part1[1]
            if dist < effect_rad and not dist < particle_rad + 10:
                part1[2] = (part2[0] - part1[0]) * force_sim_speed
                part1[3] = (part2[1] - part1[1]) * force_sim_speed
                part2[2] = (part1[0] - part2[0]) * force_sim_speed
                part2[3] = (part1[1] - part2[1]) * force_sim_speed
            elif dist < effect_rad and dist < particle_rad + 10:
                part1[2] = (part1[0] - part2[0]) * force_sim_speed
                part1[3] = (part1[1] - part2[1]) * force_sim_speed
                part2[2] = (part2[0] - part1[0]) * force_sim_speed
                part2[3] = (part2[1] - part1[1]) * force_sim_speed
                min_dist = particle_rad * 2
                if dist < min_dist:
                    overlap = min_dist - dist
                    push_x = (dx / dist) * overlap * 0.5
                    push_y = (dy / dist) * overlap * 0.5
                    
                    part1[0] -= push_x
                    part1[1] -= push_y
                    part2[0] += push_x
                    part2[1] += push_y
    for p in particles:
        p[0] += p[2]
        p[1] += p[3]
    pygame.display.flip()
    screen.fill((0,0,0))
    for p in particles:
        particle = pygame.draw.circle(screen,red,(p[0],p[1]),particle_rad)
    clock.tick(FPS)
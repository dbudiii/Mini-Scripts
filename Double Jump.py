import pygame, sys


def gravity(): 
    global gravity_force, jump_count
    ball.y += gravity_force

    #Prevent ball from falling offscreen
    if ball.bottom >= screen_height:
        ball.bottom = screen_height
    
    #Reset jump count when ball touches floor 
    if ball.bottom == screen_height:
        jump_count = 0

def reset_jump():
    global gravity_force
    gravity_force = 10

def jump():
    global gravity_force, jump_count
    if jump_count <= max_jumps:
        gravity_force = jump_force
        jump_count += 1

pygame.init()

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

#colors
bg_color = "grey12"
light_grey = (200, 200, 200)

#surfaces
ball = pygame.Rect(screen_width/2, screen_height/2, 30, 30)

#speed
gravity_force = 10
jump_force = -10

#adjust jump timing
jump_timer = 0
jump_duration = 240

jump_count = 0
max_jumps = 2

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #Jumping
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump()

    screen.fill(bg_color)
    pygame.draw.ellipse(screen, light_grey, ball)

    gravity()

    if gravity_force != 10:
        jump_timer += 10
        if jump_timer >= jump_duration:
            reset_jump()
            jump_timer = 0


    pygame.display.flip()
    clock.tick(60)

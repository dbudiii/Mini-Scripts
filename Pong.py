# Pseudo Code
# Screen [DONE]
# Game set up [DONE]
# ball render and movement [DONE] 
# player paddle movement [DONE]
# opponent paddle movement 
# collision
# score keep

import pygame, sys, random 

def ball_movement():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.right >= screen_width or ball.left <= 0:
        ball_speed_x *= -1
    
    if ball.bottom >= screen_height or ball.top <= 0:
        ball_speed_y *= -1

def player_movement():
    player.y += player_speed

pygame.init() 

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

bg_color = "grey12"
light_grey = (200, 200, 200)

ball = pygame.Rect(screen_width/2,screen_height/2, 30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 30, 10, 125)
opponent = pygame.Rect(10, screen_height/2 - 30, 10, 125)

ball_speed_x = 7
ball_speed_y = 7
player_speed = 0

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
            

    screen.fill(bg_color)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)

    ball_movement()
    player_movement()

    pygame.display.flip()
    clock.tick(60)
    

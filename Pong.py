# Pseudo Code
# Screen [DONE]
# Game set up [DONE]
# ball render and movement [DONE] 
# player paddle movement [DONE]
# opponent paddle movement [DONE]
# collision [DONE]
# score keep [DONE]
# ball restart
# timer 

import pygame, sys, random 

def ball_movement():
    global ball_speed_x, ball_speed_y, opponent_score, player_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.x >= screen_width:
        opponent_score += 1
    
    if ball.x <= 0:
        player_score += 1

    if ball.bottom >= screen_height or ball.top <= 0:
        ball_speed_y *= -1

    if pygame.Rect.colliderect(ball, player):
        ball_speed_x *= -1
    
    if pygame.Rect.colliderect(ball, opponent):
        ball_speed_x *= -1

def player_movement():
    player.y += player_speed
    
    if player.bottom >= screen_height:
        player.bottom = screen_height
    
    if player.top <= 0:
        player.top = 0

def opponent_movement():
    if opponent.bottom <= ball.bottom:
        opponent.y += opponent_speed
    
    if opponent.top >= ball.top:
        opponent.y -= opponent_speed

def ball_start():


pygame.init() 

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

# colors
bg_color = "grey12"
light_grey = (200, 200, 200)

# surfaces 
ball = pygame.Rect(screen_width/2,screen_height/2, 30,30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 30, 10, 125)
opponent = pygame.Rect(10, screen_height/2 - 30, 10, 125)
game_font = pygame.font.SysFont("comicsansm", 45, False, False)

# speeds
ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 7

# score count 
player_score = 0
opponent_score = 0

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
    pygame.draw.aaline(screen, light_grey, [screen_width/2, 0], [screen_width/2, screen_height])
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)

    ball_movement()
    player_movement()
    opponent_movement()

    player_score_text = game_font.render(str(player_score), True, light_grey)
    screen.blit(player_score_text, (screen_width/2 + 10,screen_height/2))
    
    opponent_score_text = game_font.render(str(opponent_score), True, light_grey)
    screen.blit(opponent_score_text, (screen_width/2 - 27,screen_height/2))
    
    pygame.display.flip()
    clock.tick(60)
    

import pygame

#initializing pygame
pygame.init()

#setting window display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("Font/Pixeltype.ttf",50)

#surfaces
sky_surf = pygame.image.load("Graphics/Sky.png").convert()
ground_surf = pygame.image.load("Graphics/ground.png").convert()

score_surf = test_font.render("My Game", False, "Black")
score_rect = score_surf.get_rect(center = (400,100))

snail_surf = pygame.image.load("Graphics/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (800,300))

player_surf = pygame.image.load("Graphics/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

#running the display 
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEMOTION:
      if player_rect.collidepoint(event.pos):
        print("collision")
  
  screen.blit(sky_surf,(0,0))
  screen.blit(ground_surf,(0,300))
  screen.blit(score_surf, score_rect)
  snail_rect.x -= 4
  if snail_rect.right <+ 0: 
    snail_rect.left = 800
  screen.blit(snail_surf, snail_rect)
  screen.blit(player_surf,player_rect)

  #check collision
#  mouse_pos = pygame.mouse.get_pos()
#  if player_rect.collidepoint(mouse_pos):
#    print("Collision")
  
  pygame.display.update()    
  screen.fill("black")
  clock.tick(60)
  
pygame.quit()

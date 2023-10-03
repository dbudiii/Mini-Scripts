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
sky_surface = pygame.image.load("Graphics/Sky.png")
ground_surface = pygame.image.load("Graphics/ground.png")
text_surface = test_font.render("My Game", False, "Black")

snail_surface = pygame.image.load("Graphics/snail1.png")
snail_x_pos = 550

#running the display 
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.blit(sky_surface,(0,0))
  screen.blit(ground_surface,(0,300))
  screen.blit(text_surface, (200,100))
  snail_x_pos -= 1
  screen.blit(snail_surface, (snail_x_pos,275))
  
  pygame.display.update()    
  screen.fill("black")
  clock.tick(60)
  
pygame.quit()

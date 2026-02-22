import pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game Screen")
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
rect_x = 350
rect_y = 250
rect_width = 100
rect_height = 100
speed = 5
font = pygame.font.SysFont("Arial", 36)
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rect_x -= speed
    if keys[pygame.K_RIGHT]:
        rect_x += speed
    if keys[pygame.K_UP]:
        rect_y -= speed
    if keys[pygame.K_DOWN]:
        rect_y += speed
    pygame.draw.rect(screen, BLUE, (rect_x, rect_y, rect_width, rect_height))
    text = font.render("Move the box using arrow keys", True, BLACK)
    screen.blit(text, (180, 50))
    pygame.display.flip()
pygame.quit()

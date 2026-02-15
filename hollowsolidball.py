import pygame
pygame.init()
window = pygame.display.set_mode((400,400))
window.fill((255,255,255))
green = (0,255,0)
pygame.draw.circle(window,green,(300,300),50)
pygame.draw.circle(window,green,(100,100),50,3)
pygame.display.update()
Running = True
while Running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
pygame.quit()


import pygame

pygame.init()
screenwidth = 640
screenheight = 480
screen = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption("My first game screen")

white = (255, 255, 255)
purple = (128, 0 ,128)
black = (0, 0, 0)

font = pygame.font.SysFont("Verdana", 30)
textsurface = font.render("Python Graphics", True, black)


running = True
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
screen.fill(white)
pygame.draw.rect(screen, purple. myrect)
pygame.display.flip()
pygame.quit()
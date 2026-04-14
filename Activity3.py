import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Color changing sprite")
    colors = {"Red":pygame.Color("Red"), 
              "Green":pygame.Color("Green"),
              "Blue":pygame.Color("Blue"),
              "Yellow":pygame.Color("Yellow"),
              "White":pygame.Color("White")}
    current_colors = colors['White']
    x, y = 30, 30
    sprite_width, sprite_height = 60, 60
    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            x -= 3
        if pressed[pygame.K_RIGHT]:
            x += 3
        if pressed[pygame.K_DOWN]:
            y += 3
        if pressed[pygame.K_UP]:
            y -= 3
        x = min(max(0, x), 500 - sprite_width)
        y = min(max(0, y), 500 - sprite_height)
        if x == 0:
            current_colors = colors["Blue"]
        elif x == 500 - sprite_width:
            current_colors = colors["Yellow"]
        elif y==0:
            current_colors = colors["Red"]
        elif y==500 - sprite_height:
            current_colors = colors["Green"]
        else:
            current_colors = colors["White"]
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_colors, (x, y, sprite_width, sprite_height))
        pygame.display.flip()
        clock.tick(90)
    pygame.quit()
main()


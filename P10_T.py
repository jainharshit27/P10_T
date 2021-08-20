import pygame, pymunk
import pymunk.pygame_util

pygame.init()

height = 600
width = 300
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#pymunk space
gravity = 100
wind = 0
# Create pymunk space
# assign wind and gravity to the space.gravity
draw_options = pymunk.pygame_util.DrawOptions(screen)

body1 = pymunk.Body(1,200)
shape1 = pymunk.Circle(body1, 25)
body1.position = 50, 0
space.add(body1, shape1)

'''Create body 2 and body 3
at different position with different radius
and add them to space.
Take reference from body1 & shape1 above'''

while True:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    space.debug_draw(draw_options)
    pygame.display.update()
    
    #space reload
    space.step(1/60)
    clock.tick(60)
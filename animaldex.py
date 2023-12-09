import pygame

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

image = pygame.image.load('pokedex.png')

def Background_sky(image):
	size = pygame.transform.scale(image, (screen_width, screen_height))
	screen.blit(size, (0,0))

run = True
while run:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

screen.fill((0, 255, 0))
Background_sky(image)

pygame.quit()

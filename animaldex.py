import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Start Menu')

def draw_button():
    button_width = 200
    button_height = 50
    button_color = (255, 0, 0)
    button_x = (screen_width - button_width) // 2
    button_y = (screen_height - button_height) // 2

    pygame.draw.rect(screen, button_color, (button_x, button_y, button_width, button_height))

    return pygame.Rect(button_x, button_y, button_width, button_height)

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    next_page()

        screen.fill((0, 255, 0))
        button_rect = draw_button()

        pygame.display.flip()

def next_page():
	screen.fill((0, 0, 255))
	pygame.display.flip()
	pygame.time.delay(1000000)

if __name__ == "__main__":
	main_menu()

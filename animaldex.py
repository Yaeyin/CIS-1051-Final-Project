import pygame
import sys
from pygame import mixer

pygame.init()

screen_width, screen_height = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

mixer.music.load('combat.wav')
mixer.music.play(-1)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pokedex Start Menu")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

def draw_start_menu():
    screen.fill(WHITE)
    
    text = font.render("Pokedex", True, BLACK)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 3))
    screen.blit(text, text_rect)

    pygame.draw.rect(screen, BLACK, (screen_width // 2 - 100, screen_height // 2, 200, 50))
    button_text = font.render("Go to Pokedex", True, WHITE)
    button_text_rect = button_text.get_rect(center=(screen_width // 2, screen_height // 2 + 25))
    screen.blit(button_text, button_text_rect)

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if screen_width // 2 - 100 <= x <= screen_width // 2 + 100 and screen_height // 2 <= y <= screen_height // 2 + 50:
                    running = False  # replace to goto pokedex page

        draw_start_menu()
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

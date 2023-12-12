import pygame
import sys

pygame.init()

screen_width, screen_height = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pokedex Start Menu")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

pos = pygame.mouse.get_pos()

class Character:
    def __init__(self, x, y, health, stamina, image_path):
        self.rect = pygame.Rect(x, y, 100, 20)
        self.health = health
        self.stamina = stamina
        self.image = pygame.image.load(image_path)

    def draw(self):
        pygame.draw.rect(screen, BLACK, self.rect)
        health_text = font.render(f"Health: {self.health}/100", True, BLACK)
        stamina_text = font.render(f"Stamina: {self.stamina}/100", True, BLACK)
        screen.blit(health_text, (self.rect.x + 120, self.rect.y))
        screen.blit(stamina_text, (self.rect.x + 120, self.rect.y + 30))
        screen.blit(self.image, self.rect.topleft)

class PokedexPage:
    def __init__(self):
        self.background = pygame.image.load("background.png").convert()
        self.characters = [
            Character(50, 50, 100, 80, "8bit_elephant.png"),
            Character(450, 350, 80, 100, "8biteagle.png"),
            Character(50, 350, 80, 100, "8bitporcupine.png"),
            Character(450, 50, 80, 100, "8bitBear.png"),
        ]

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def draw(self):
        screen.blit(self.background, (0, 0))

        for character in self.characters:
            character.draw()

def draw_start_menu():
    pos = pygame.mouse.get_pos()
    screen.fill(RED)
    
    text = font.render("Pokedex", True, WHITE)
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 3))
    screen.blit(text, text_rect)

    pygame.draw.rect(screen, BLACK, (screen_width // 2 - 100, screen_height // 2, 200, 50))
    button_text = font.render("Go to Pokedex", True, WHITE)
    button_text_rect = button_text.get_rect(center=(screen_width // 2, screen_height // 2 + 25))
    screen.blit(button_text, button_text_rect)

    if button_text_rect.collidepoint(pos):
        pygame.draw.rect(screen, WHITE, button_text_rect)
        screen.blit(font.render("Go to Pokedex", True, BLACK), button_text_rect)    

def main():
    current_state = "StartMenu"

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if current_state == "StartMenu":
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if screen_width // 2 - 100 <= x <= screen_width // 2 + 100 and screen_height // 2 <= y <= screen_height // 2 + 50:
                        current_state = "PokedexPage"

            draw_start_menu()

        elif current_state == "PokedexPage":
            pokedex_page = PokedexPage()
            pokedex_page.handle_events(events)
            pokedex_page.draw()

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

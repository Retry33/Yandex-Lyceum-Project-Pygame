import pygame
from settings import WINDOW_SIZE


class MainMenu:
    def __init__(self, screen):
        self.background_image = pygame.image.load("img/306.jpg")
        self.background_image = pygame.transform.scale(self.background_image, WINDOW_SIZE)
        self.screen = screen
        self.font_title = pygame.font.Font(None, 72)
        self.font_buttons = pygame.font.Font(None, 96)
        self.title = self.font_title.render("Здесь будет название", True, (255, 255, 255))
        self.selected_button = 0

    def draw_text_with_border(self, text, font, color, position, selected=False):
        border_color = (255, 0, 0) if selected else (255, 255, 255)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=position)

        if not selected:  # Рисуем рамку только если кнопка не выбрана
            pygame.draw.rect(self.screen, border_color, text_rect, 2)
        self.screen.blit(text_surface, text_rect.topleft)

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))

        # Отрисовка заголовка без рамки
        title_position = (WINDOW_SIZE[0] // 2, 100)
        self.draw_text_with_border("Здесь будет название", self.font_title, (255, 255, 255), title_position, True)

        # Определение положения кнопок
        button_spacing = 100
        vertical_center = WINDOW_SIZE[1] // 2
        play_button_position = (WINDOW_SIZE[0] // 2, vertical_center - button_spacing // 2)
        quit_button_position = (WINDOW_SIZE[0] // 2, vertical_center + button_spacing // 2)

        # Отрисовка кнопок
        self.draw_text_with_border("Play", self.font_buttons, (255, 255, 255), play_button_position,
                                   self.selected_button == 1)
        self.draw_text_with_border("Quit", self.font_buttons, (255, 255, 255), quit_button_position,
                                   self.selected_button == 0)

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected_button = (self.selected_button - 1) % 2
                elif event.key == pygame.K_DOWN:
                    self.selected_button = (self.selected_button + 1) % 2
                elif event.key == pygame.K_RETURN:
                    if self.selected_button == 0:
                        return "play"
                    elif self.selected_button == 1:
                        pygame.quit()
                        exit()
        return None

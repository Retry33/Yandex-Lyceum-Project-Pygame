import pygame
from settings import WINDOW_SIZE


class MainMenu:
    def __init__(self, screen):
        self.background_image = pygame.image.load("img/wall1.jpg")
        self.background_image = pygame.transform.scale(self.background_image, WINDOW_SIZE)
        self.screen = screen
        self.font_title = pygame.font.Font("fonts/SquaredanceFontV1-Regular.ttf", 96)
        self.font_buttons = pygame.font.Font("fonts/SquaredanceFontV1-Regular.ttf", 96)
        self.title = self.font_title.render("Escape from the Devil", True, (255, 255, 255))
        self.selected_button = 0
        self.flag = False

    def draw_text_with_border(self, text, font, color, position, selected=False):
        text_surface = font.render(text, True, color if selected else (255, 36, 0))
        text_rect = text_surface.get_rect(center=position)
        self.screen.blit(text_surface, text_rect.topleft)

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))

        # Отрисовка заголовка без рамки
        title_position = (WINDOW_SIZE[0] // 2, 160)
        self.draw_text_with_border("Escape from the Devil", self.font_title, (255, 255, 255), title_position, True)

        # Определение положения кнопок
        button_spacing = 100
        vertical_center = WINDOW_SIZE[1] // 2
        play_button_position = (WINDOW_SIZE[0] // 2, vertical_center - button_spacing // 2)
        quit_button_position = (WINDOW_SIZE[0] // 2, vertical_center + button_spacing // 2)

        # Отрисовка кнопок
        if not self.flag:
            self.draw_text_with_border("PLAY", self.font_buttons, (255, 255, 255), play_button_position,
                                       self.selected_button == 1)
            self.draw_text_with_border("QUIT", self.font_buttons, (255, 255, 255), quit_button_position,
                                       self.selected_button == 0)
        else:
            self.draw_text_with_border("EASY", self.font_buttons, (255, 255, 255), play_button_position,
                                       self.selected_button == 1)
            self.draw_text_with_border("HARD", self.font_buttons, (255, 255, 255), quit_button_position,
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
                    if not self.flag:
                        if self.selected_button == 0:
                            self.flag = True
                        elif self.selected_button == 1:
                            pygame.quit()
                            exit()
                    else:
                        if self.selected_button == 0:
                            return "EASY"
                        elif self.selected_button == 1:
                            return "HARD"
        return None


class FinalMenu:
    def __init__(self, screen):
        self.background_image = pygame.image.load("img/wall1.jpg")
        self.background_image = pygame.transform.scale(self.background_image, WINDOW_SIZE)
        self.screen = screen
        self.font = pygame.font.Font("fonts/SquaredanceFontV1-Regular.ttf", 96)
        self.text_color = pygame.Color("White")

    def draw(self):
        self.screen.blit(self.background_image, (0, 0))
        self.draw_text("Congratulations!", WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 - 40)
        self.draw_text("YOUR SCORE 1000", WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2 + 40)

    def draw_text(self, text, x, y):
        text_surface = self.font.render(text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(x, y))
        self.screen.blit(text_surface, text_rect)
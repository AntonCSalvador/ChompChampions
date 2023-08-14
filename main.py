"""
main file for Chomp Champions
"""
import pygame, sys


def main():

    # initialization of the pygame, screensize, and caption
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('ChompChampions')
    main_menu(screen)


def main_menu(screen):

    # Setting up screen
    screen.fill((0, 0, 0))
    screen.blit(screen, (0, 0))
    pygame.display.update()

    # font type for the main menu buttons
    font_type = pygame.font.Font(None, 40)

    # start button initialization
    start_button_surface = font_type.render("Start", 0, (255, 255, 255))
    start_button_rectangle = start_button_surface.get_rect(center=(1280 // 3, 480))
    screen.blit(start_button_surface, start_button_rectangle)

    # instructions button initialization
    instructions_button_surface = font_type.render("Start", 0, (255, 255, 255))
    instructions_button_rectangle = instructions_button_surface.get_rect(center=((1280 // 3) * 2, 480))

    screen.blit(instructions_button_surface, instructions_button_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()


if __name__ == "__main__":
    main()
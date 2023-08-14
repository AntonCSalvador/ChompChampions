"""
main file for Chomp Champions
"""
import pygame
import sys


def main():

    # initialization of the pygame, screensize, and caption
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('ChompChampions')
    main_menu_output = main_menu(screen)
    if main_menu_output == "instructions":
        # brings user to instructions menu
        print(main_menu_output)
    elif main_menu_output == "start":
        # brings user to start menu
        print(main_menu_output)


def main_menu(screen):

    # Setting up screen
    screen.fill((0, 0, 0))
    start_menu_screen = pygame.image.load("static/chompChampionsTitlev1.png")
    screen.blit(start_menu_screen, (0, 0))
    pygame.display.update()

    # font type for the main menu buttons
    font_type = pygame.font.Font(None, 40)

    # start button initialization
    start_button_surface = font_type.render("Start", 0, (255, 255, 255), (51, 51, 51))
    start_button_rectangle = start_button_surface.get_rect(center=(1280 // 3, 480))
    screen.blit(start_button_surface, start_button_rectangle)

    # instructions button initialization
    instructions_button_surface = font_type.render("Instructions", 0, (255, 255, 255), (51, 51, 51))
    easy_surface = pygame.Surface((20, 20))
    easy_surface.fill((255, 255, 255))
    easy_surface.blit(instructions_button_surface, (10, 10))
    instructions_button_rectangle = instructions_button_surface.get_rect(center=((1280 // 3) * 2, 480))
    screen.blit(instructions_button_surface, instructions_button_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if instructions_button_rectangle.collidepoint(event.pos):
                    return "instructions"
                elif start_button_rectangle.collidepoint(event.pos):
                    return "start"
        pygame.display.update()


if __name__ == "__main__":
    main()

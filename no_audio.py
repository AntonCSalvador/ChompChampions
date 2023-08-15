"""
main file for Chomp Champions
"""
import pygame
import sys
import os


def main():

    # initialization of the pygame, screensize, and caption
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('ChompChampions')
    while True:
        main_menu_output = main_menu(screen)
        if main_menu_output == "instructions":
            # brings user to instructions menu
            if instructions(screen) == "back":
                continue
        elif main_menu_output == "start":
            # brings user to start menu
            if start_screen(screen) == "back":
                continue


def main_menu(screen):

    # Setting up screen
    screen.fill((0, 0, 0))
    start_menu_screen = pygame.image.load("static/chompChampionsTitlev1.png")
    screen.blit(start_menu_screen, (0, 0))
    pygame.display.update()

    # font type for the main menu buttons
    font_type = pygame.font.SysFont("impact", 40)

    # start button initialization
    start_button_surface = font_type.render("Start", 0, (255, 255, 255), (51, 51, 51))
    start_button_rectangle = start_button_surface.get_rect(center=(1280 // 3, 480))
    screen.blit(start_button_surface, start_button_rectangle)
    start_button_collide = False

    # instructions button initialization
    instructions_button_surface = font_type.render("Instructions", 0, (255, 255, 255), (51, 51, 51))
    instructions_button_rectangle = instructions_button_surface.get_rect(center=((1280 // 3) * 2, 480))
    screen.blit(instructions_button_surface, instructions_button_rectangle)
    instructions_button_collide = False

    while True:
        for event in pygame.event.get():

            # Allows user to exit game
            if event.type == pygame.QUIT:
                sys.exit()

            # Events for when user clicks with mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                if instructions_button_rectangle.collidepoint(event.pos):
                    return "instructions"
                elif start_button_rectangle.collidepoint(event.pos):
                    return "start"

            # When user hovers over instructions, changes to red, else returns to normal
            instructions_button_collide_old = instructions_button_collide
            instructions_button_collide = instructions_button_rectangle.collidepoint(pygame.mouse.get_pos())

            if instructions_button_collide_old != instructions_button_collide:
                if instructions_button_collide:
                    instructions_button_surface = font_type.render("Instructions", 0, (255, 0, 0), (51, 51, 51))
                    instructions_button_rectangle = instructions_button_surface.get_rect(center=((1280 // 3) * 2, 480))
                    screen.blit(instructions_button_surface, instructions_button_rectangle)

                else:
                    instructions_button_surface = font_type.render("Instructions", 0, (255, 255, 255), (51, 51, 51))
                    instructions_button_rectangle = instructions_button_surface.get_rect(center=((1280 // 3) * 2, 480))
                    screen.blit(instructions_button_surface, instructions_button_rectangle)

            # When user hovers over start, changes to red, else returns to normal
            start_button_collide_old = start_button_collide
            start_button_collide = start_button_rectangle.collidepoint(pygame.mouse.get_pos())

            if start_button_collide_old != start_button_collide:
                if start_button_collide:
                    start_button_surface = font_type.render("Start", 0, (255, 0, 0), (51, 51, 51))
                    start_button_rectangle = start_button_surface.get_rect(center=((1280 // 3), 480))
                    screen.blit(start_button_surface, start_button_rectangle)
                else:
                    start_button_surface = font_type.render("Start", 0, (255, 255, 255), (51, 51, 51))
                    start_button_rectangle = start_button_surface.get_rect(center=((1280 // 3), 480))
                    screen.blit(start_button_surface, start_button_rectangle)

        pygame.display.update()


def instructions(screen):

    # Setting up screen
    screen.fill((0, 0, 0))
    pygame.display.update()
    back_arrow_font = pygame.font.SysFont("webdings", 40)

    # start button initialization
    back_button_surface = back_arrow_font.render("3", 0, (255, 255, 255), (51, 51, 51))
    back_button_rectangle = back_button_surface.get_rect(center=(20, 20))
    screen.blit(back_button_surface, back_button_rectangle)

    while True:
        for event in pygame.event.get():

            # Allows user to exit game
            if event.type == pygame.QUIT:
                sys.exit()

            # If user clicks back, returns to main menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rectangle.collidepoint(event.pos):
                    return "back"

        pygame.display.update()


def start_screen(screen):

    # Setting up screen
    screen.fill((0, 0, 0))
    pygame.display.update()
    back_arrow_font = pygame.font.SysFont("webdings", 40)

    # start button initialization
    back_button_surface = back_arrow_font.render("3", 0, (255, 255, 255), (51, 51, 51))
    back_button_rectangle = back_button_surface.get_rect(center=(20, 20))
    screen.blit(back_button_surface, back_button_rectangle)

    while True:
        for event in pygame.event.get():

            # Allows user to exit game
            if event.type == pygame.QUIT:
                sys.exit()

            # If user clicks back, returns to main menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rectangle.collidepoint(event.pos):
                    return "back"

        pygame.display.update()


if __name__ == "__main__":
    main()

"""
main file for Chomp Champions
"""
import pygame
import sys
import os


def main():

    # initialization of the pygame, screensize, and caption
    pygame.init()
    pygame.mixer.init()
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
    font_type = pygame.font.SysFont("impact", 40)

    # setting up audio for button hover and main menu audio (can be changed later)
    button_click_sound = 'audio'
    main_menu_sound = pygame.mixer.Sound("audio/main_menu_audio.mp3")
    pygame.mixer.Sound.set_volume(main_menu_sound, 0.25)
    pygame.mixer.Sound.play(main_menu_sound, loops=-1)

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

            # When user hovers over instructions, changes to red, else returns to normal, click noise on button contact
            instructions_button_collide_old = instructions_button_collide
            instructions_button_collide = instructions_button_rectangle.collidepoint(pygame.mouse.get_pos())

            if instructions_button_collide_old != instructions_button_collide:
                if instructions_button_collide:
                    instructions_button_surface = font_type.render("Instructions", 0, (255, 0, 0), (51, 51, 51))
                    instructions_button_rectangle = instructions_button_surface.get_rect(center=((1280 // 3) * 2, 480))
                    screen.blit(instructions_button_surface, instructions_button_rectangle)
                    clicky = pygame.mixer.Sound(os.path.join(button_click_sound, 'hoverClick.mp3'))
                    pygame.mixer.Sound.play(clicky)

                else:
                    instructions_button_surface = font_type.render("Instructions", 0, (255, 255, 255), (51, 51, 51))
                    instructions_button_rectangle = instructions_button_surface.get_rect(center=((1280 // 3) * 2, 480))
                    screen.blit(instructions_button_surface, instructions_button_rectangle)

            # When user hovers over start, changes to red, else returns to normal, click noise on button contact
            start_button_collide_old = start_button_collide
            start_button_collide = start_button_rectangle.collidepoint(pygame.mouse.get_pos())

            if start_button_collide_old != start_button_collide:
                if start_button_collide:
                    start_button_surface = font_type.render("Start", 0, (255, 0, 0), (51, 51, 51))
                    start_button_rectangle = start_button_surface.get_rect(center=((1280 // 3), 480))
                    screen.blit(start_button_surface, start_button_rectangle)
                    clicky = pygame.mixer.Sound(os.path.join(button_click_sound, 'hoverClick.mp3'))
                    pygame.mixer.Sound.play(clicky)
                else:
                    start_button_surface = font_type.render("Start", 0, (255, 255, 255), (51, 51, 51))
                    start_button_rectangle = start_button_surface.get_rect(center=((1280 // 3), 480))
                    screen.blit(start_button_surface, start_button_rectangle)

        pygame.display.update()


if __name__ == "__main__":
    main()

import pygame
class Audio:

    def __init__(self, volume, music_type, mute, screen, file_location):
        pygame.mixer.init()
        self.volume = volume
        self.music_type = music_type
        self.mute = mute
        self.screen = screen
        self.file_location = file_location
        self.music = pygame.mixer.Sound(self.file_location)
        self.button_surface = ""
        self.button_rectangle = ""

    def draw_music_audio(self, screen, font_type, font_size, text, text_color, background_color, button_center):
        icon = pygame.font.SysFont(font_type, font_size)
        self.button_surface = icon.render(text, 0, text_color, background_color)
        self.button_rectangle = self.button_surface.get_rect(center=button_center)
        screen.blit(self.button_surface, self.button_rectangle)

    def set_volume(self, volume):
        self.volume = volume
        self.music.set_volume(volume)

    def play_music(self, duration):
        pygame.mixer.Sound.play(self.music, duration)

    def mute_change(self):
        if self.mute:
            self.mute = False
            pygame.mixer.Sound.play(self.music)
        else:
            self.mute = True
            pygame.mixer.Sound.stop(self.music)

class AudioList:

    def __init__(self):
        self.all_list = []
        self.music_list = []
        self.sound_fx_list = []
        self.voice_line_list = []
        self.character_sound_list = []

    def add_all(self, audio_class_object):
        self.all_list = self.all_list + audio_class_object




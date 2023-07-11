import pygame
from pygame.locals import *
import sys




class WinScreen:
    def __init__(self, ANCHO_VENTANA, ALTO_VENTANA):
        self.window_width = ANCHO_VENTANA
        self.window_height = ALTO_VENTANA
        self.font = pygame.font.Font(None, 36)
        self.text_surface = self.font.render("YOU WIN", True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect(center=(self.window_width/2, self.window_height/2))
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        
        pygame.display.set_caption("Ejemplo de Pygame")
        

        self.button_rect = pygame.Rect(self.window_width/2 - 50, self.window_height/2 + 50, 200, 50)  # Rectángulo del botón
        self.button_text = self.font.render("Volver al menú", True, (255, 255, 255))
        
        self.youwin_sound = pygame.mixer.Sound("street-fighter-ii-you-win-perfect.mp3")
        self.youwin_sound.set_volume(0.1)
    
    

    def show(self):
        
        self.youwin_sound.play()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if self.button_rect.collidepoint(event.pos):
                        print("volver al menu")
                        pass


            self.window.fill((0, 0, 0))
            self.window.blit(self.text_surface, self.text_rect)
            pygame.draw.rect(self.window, (255, 0, 0), self.button_rect)  # Dibuja el rectángulo del botón
            self.window.blit(self.button_text, self.button_rect.move(10, 10))  # Posiciona el texto en el botón
            pygame.display.update()

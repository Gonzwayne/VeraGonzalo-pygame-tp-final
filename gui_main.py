import pygame
from pygame.locals import *
import sys
from constantes import *
from gui_form import Form
from gui_form_menu_A import FormMenuA
from gui_form_menu_B import FormMenuB 
from gui_form_menu_C import FormMenuC
from gui_form_menu_game_l1 import FormGameLevel1
from gui_form_menu_game_l2 import FormGameLevel2
from gui_form_menu_game_l3 import FormGameLevel3

flags = DOUBLEBUF
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA), flags, 16)
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

pygame.mixer.music.load(r"C:\Users\gonza\OneDrive\Documentos\ejercicios python\CLASE_23_inicio_juego\1000-Year-Old Sacred Tree.mp3")
pygame.mixer.music.set_volume(0.02)

form_menu_A = FormMenuA(name="form_menu_A", master_surface=screen, x=300, y=200, w=500, h=400, color_background=C_BLACK, color_border=(255, 0, 255), active=True)
form_menu_B = FormMenuB(name="form_menu_B", master_surface=screen, x=300, y=200, w=500, h=400, color_background=C_BLACK, color_border=(255, 0, 255), active=False)
form_menu_C = FormMenuC(name="form_menu_C", master_surface=screen, x=0, y=0, w=ANCHO_VENTANA, h=ALTO_VENTANA, color_background=C_BLACK, color_border=(255, 0, 255), active=False,screen= screen)

form_game_L1 = FormGameLevel1(name="form_game_L1", master_surface=screen, x=0, y=0, w=ANCHO_VENTANA, h=ALTO_VENTANA, color_background=(0, 255, 255), color_border=(255, 0, 255), active=False)
form_game_L2 = FormGameLevel2(name="form_game_L2", master_surface=screen, x=0, y=0, w=ANCHO_VENTANA, h=ALTO_VENTANA, color_background=(0, 255, 255), color_border=(255, 0, 255), active=False)
form_game_L3 = FormGameLevel3(name="form_game_L3", master_surface=screen, x=0, y=0, w=ANCHO_VENTANA, h=ALTO_VENTANA, color_background=(0, 255, 255), color_border=(255, 0, 255), active=False)

pygame.mixer.music.play(loops=-1)
game_over = False
game_over_time = 0
reset_game = False




while True:
    
    lista_eventos = pygame.event.get()
    for event in lista_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    delta_ms = clock.tick(FPS)

    aux_form_active = Form.get_active()
    if aux_form_active is not None:
        aux_form_active.update(lista_eventos, keys, delta_ms)
        aux_form_active.draw()

    vidas = form_game_L1.player_1.lives 
    vidas2 = form_game_L2.player_1.lives
    vidas3 = form_game_L3.player_1.lives 
    
    
    if vidas == 0 or vidas2 == 0 or vidas3 == 0:
        if not game_over:
            game_over = True
            game_over_time = pygame.time.get_ticks()

    

    if game_over:
        current_time = pygame.time.get_ticks()
        if current_time - game_over_time < 5000:
            font = pygame.font.Font(None, 80)
            game_over_text = font.render("Game Over", True, (255, 0, 0))
            game_over_rect = game_over_text.get_rect(center=(ANCHO_VENTANA // 2, ALTO_VENTANA // 2))
            screen.blit(game_over_text, game_over_rect)
        elif current_time - game_over_time < 10000:
            if not reset_game:
                form_menu_A = FormMenuA(name="form_menu_A", master_surface=screen, x=300, y=200, w=500, h=400, color_background=(255, 255, 0), color_border=(255, 0, 255), active=True)
                form_menu_B = FormMenuB(name="form_menu_B", master_surface=screen, x=300, y=200, w=500, h=400, color_background=(0, 255, 255), color_border=(255, 0, 255), active=False)
                form_menu_C = FormMenuC(name="form_menu_C", master_surface=screen, x=0, y=0, w=ANCHO_VENTANA, h=ALTO_VENTANA, color_background=(0, 255, 255), color_border=(255, 0, 255), active=False,screen=screen)

                pygame.mixer.music.play(loops=-1)
                reset_game = False
            game_over = False

    

    pygame.display.flip()

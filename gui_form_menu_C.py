import pygame
import math
from pygame.locals import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from gui_graph import Graph
from gui_label import Label
from constantes import *
from gui_form_menu_game_l1 import FormGameLevel1
from gui_form_menu_game_l2 import FormGameLevel2
from gui_form_menu_game_l3 import FormGameLevel3


class FormMenuC(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active,screen):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.boton1 = Button(master=self,x=0,y=150,w=200,h=40,color_background=C_GREEEN_2,color_border=C_YELLOW_2,on_click=self.on_click_boton1,on_click_param="form_menu_A",text="BACK",font="Verdana",font_size=30,font_color=C_BLACK)
        self.boton2 = Button(master=self,x=0,y=200,w=200,h=40,color_background=C_PINK,color_border=C_RED,on_click=self.on_click_boton2,on_click_param="form_game_L1",text="Nivel 1",font="Verdana",font_size=30,font_color=C_BLACK)
        self.boton3 = Button(master=self,x=0,y=250,w=200,h=40,color_background=C_PINK,color_border=C_RED,on_click=self.on_click_boton3,on_click_param="form_game_L2",text="Nivel 2",font="Verdana",font_size=30,font_color=C_BLACK)
        self.boton4 = Button(master=self,x=0,y=300,w=200,h=40,color_background=C_PINK,color_border=C_RED,on_click=self.on_click_boton4,on_click_param="form_game_L3",text="Nivel 3",font="Verdana",font_size=30,font_color=C_BLACK)
        
        
        self.lista_widget = [   self.boton1,self.boton2,self.boton3,self.boton4
                            ]
        
        self.screen = screen
  
                   
        

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def on_click_boton2(self, parametro):
        #accedo nivel 1
        self.set_active(parametro)
        

    def on_click_boton3(self, parametro):
        #accedo nivel 2
        self.set_active(parametro)
        

    def on_click_boton4(self, parametro):
        #accedo nivel 3
        self.set_active(parametro)
       

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        
        super().draw()
        for aux_widget in self.lista_widget:    
            aux_widget.draw()

        

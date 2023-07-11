import pygame
from pygame.locals import *
from constantes import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from player import Player
from enemigo import Enemy
from plataforma import Plataform
from background import Background
from bullet import Bullet
from botin import Botin

class FormGameLevel2(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        #widget
        self.boton1 = Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="BACK",font="Verdana",font_size=30,font_color=C_WHITE)
        self.boton2 = Button(master=self,x=200,y=0,w=140,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Buttons/Button_M_02.png",on_click=self.on_click_boton1,on_click_param="form_menu_B",text="PAUSE",font="Verdana",font_size=30,font_color=C_WHITE)
       
        self.pb_lives = ProgressBar(master=self,x=1100,y=20,w=240,h=50,color_background=None,color_border=None,image_background="images/gui/set_gui_01/Comic_Border/Bars/Bar_Background01.png",image_progress="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",value = 5, value_max=5)
        self.widget_list = [self.boton1,self.boton2,self.pb_lives]

        #elementos                                                        
        self.static_background = Background(x=0,y=0,width=w,height=h,path="images/fondos_dbz/6.png")
        self.player_1 = Player(x=50,y=400,speed_walk=6,speed_run=12,gravity=12,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.8,interval_time_jump=300)

        self.enemy_list = []
        self.enemy_list.append (Enemy(x=450,y=400,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300))
        self.enemy_list.append (Enemy(x=250,y=400,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300))
        self.enemy_list.append (Enemy(x=900,y=400,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300))
        self.enemy_list.append (Enemy(x=600,y=400,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300))
        self.enemy_list.append (Enemy(x=1100,y=400,speed_walk=6,speed_run=5,gravity=14,jump_power=30,frame_rate_ms=150,move_rate_ms=50,jump_height=140,p_scale=0.08,interval_time_jump=300))
        
        
        self.plataform_list = []
        self.plataform_list.append(Plataform(x=400,y=500,width=50,height=50,type=0))
        self.plataform_list.append(Plataform(x=450,y=500,width=50,height=50,type=1))
        self.plataform_list.append(Plataform(x=500,y=500,width=50,height=50,type=2))   
        self.plataform_list.append(Plataform(x=600,y=430,width=50,height=50,type=12))
        self.plataform_list.append(Plataform(x=650,y=430,width=50,height=50,type=14))
        self.plataform_list.append(Plataform(x=750,y=360,width=50,height=50,type=12))
        self.plataform_list.append(Plataform(x=800,y=360,width=50,height=50,type=13))
        self.plataform_list.append(Plataform(x=850,y=360,width=50,height=50,type=13))
        self.plataform_list.append(Plataform(x=900,y=360,width=50,height=50,type=14))
        self.plataform_list.append(Plataform(x=1150,y=360,width=50,height=50,type=12))
        self.plataform_list.append(Plataform(x=1200,y=360,width=50,height=50,type=13))
        self.plataform_list.append(Plataform(x=1250,y=360,width=50,height=50,type=13))
        self.plataform_list.append(Plataform(x=1300,y=360,width=50,height=50,type=14))
        self.plataform_list.append(Plataform(x=150,y=360,width=50,height=50,type=12))
        self.plataform_list.append(Plataform(x=200,y=360,width=50,height=50,type=13))
        self.plataform_list.append(Plataform(x=250,y=360,width=50,height=50,type=13))
        self.plataform_list.append(Plataform(x=300,y=360,width=50,height=50,type=14))
        self.plataform_list.append(Plataform(x=1050,y=450,width=50,height=50,type=13))
        self.plataform_list.append(Plataform(x=1100,y=450,width=50,height=50,type=14))

        self.botin_list = []
        self.botin_list.append(Botin(x=410,y=450,width=50,height=50,type=0))
        self.botin_list.append(Botin(x=620,y=380,width=50,height=50,type=0))
        self.botin_list.append(Botin(x=470,y=450,width=50,height=50,type=0))
        self.botin_list.append(Botin(x=800,y=310,width=50,height=50,type=0))
        self.botin_list.append(Botin(x=880,y=310,width=50,height=50,type=0))
        self.botin_list.append(Botin(x=1050,y=400,width=50,height=50,type=0))
        self.botin_list.append(Botin(x=1100,y=400,width=50,height=50,type=0))
        self.botin_list.append(Botin(x=150,y=310,width=50,height=50,type=0))
        self.botin_list.append(Botin(x=200,y=310,width=50,height=50,type=0))
        self.botin_list.append(Botin(x=1200,y=310,width=50,height=50,type=0))
        self.botin_list.append(Botin(x=1250,y=310,width=50,height=50,type=0))

        self.bullet_list = []

        self.timer_3s = pygame.USEREVENT +1
        pygame.time.set_timer(self.timer_3s,3000)

        self.shoot_sound = pygame.mixer.Sound("aagun3.wav")
        self.shoot_sound.set_volume(0.1)
        self.level_sound = pygame.mixer.Sound("reload.wav")
        self.level_sound.set_volume(0.1)
        



    def on_click_boton1(self, parametro):
        self.set_active(parametro)



    def shoot_enemy(self):
        
        pygame.time.set_timer(self.timer_3s,3000)
        for enemy_element in self.enemy_list:
            self.bullet_list.append(Bullet(enemy_element,enemy_element.rect.centerx,enemy_element.rect.centery,self.player_1.rect.centerx,self.player_1.rect.centery,5,path="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",frame_rate_ms=100,move_rate_ms=20,width=5,height=5))
            self.shoot_sound.play()
        

    def update(self, lista_eventos,keys,delta_ms):
        for aux_widget in self.widget_list:
            aux_widget.update(lista_eventos)

        for bullet_element in self.bullet_list:
            bullet_element.update(delta_ms,self.plataform_list,self.enemy_list,self.player_1)

        for bullet_element in self.player_1.bullet_list:
            bullet_element.update(delta_ms,self.plataform_list,self.enemy_list,self.player_1)

        for enemy_element in self.enemy_list:
            enemy_element.update(delta_ms,self.plataform_list)

        for evento in lista_eventos:
            if evento.type == self.timer_3s:
                self.shoot_enemy()

        if self.player_1.score >= 1100:
            self.set_active("form_game_L3")
            self.level_sound.play()
                 

        self.player_1.events(delta_ms,keys)
        self.player_1.update(delta_ms,self.plataform_list,self.botin_list)

        self.pb_lives.value = self.player_1.lives 
        


    def draw(self): 
        super().draw()
        self.static_background.draw(self.surface)

        for aux_widget in self.widget_list:    
            aux_widget.draw()

        for plataforma in self.plataform_list:
            plataforma.draw(self.surface)

        for botin in self.botin_list:
            botin.draw(self.surface)

        for enemy_element in self.enemy_list:
            enemy_element.draw(self.surface)
        
        self.player_1.draw(self.surface)

        for bullet_element in self.bullet_list:
            bullet_element.draw(self.surface)

        for bullet_element in self.player_1.bullet_list:
            bullet_element.draw(self.surface)
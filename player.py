import pygame
from constantes import *
from auxiliar import Auxiliar
from bullet import Bullet
from botin import Botin
from pygame import mixer
class Player:
    def __init__(self,x,y,speed_walk,speed_run,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,p_scale=1,interval_time_jump=100) -> None:


        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/pirate_02/Idle ({0}).png",1,7,flip=False,scale=0.12)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/pirate_02/Idle ({0}).png",1,7,flip=True,scale=0.12)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/pirate_02/Jump ({0}).png",1,7,flip=False,scale=0.12)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/pirate_02/Jump ({0}).png",1,7,flip=True,scale=0.12)
        self.walk_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/pirate_02/Run ({0}).png",1,7,flip=False,scale=0.12)
        self.walk_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/pirate_02/Run ({0}).png",1,7,flip=True,scale=0.12)
        self.shoot_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/pirate_02/Shoot ({0}).png",1,7,flip=False,scale=0.12,repeat_frame=1)
        self.shoot_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/pirate_02/Shoot ({0}).png",1,7,flip=True,scale=0.12,repeat_frame=1)
        self.knife_r = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/pirate_02/Melee ({0}).png",1,7,flip=False,scale=0.12,repeat_frame=1)
        self.knife_l = Auxiliar.getSurfaceFromSeparateFiles("images/caracters/players/pirate_02/Melee ({0}).png",1,7,flip=True,scale=0.12,repeat_frame=1)

        self.bullet_list = []
        self.frame = 0
        self.lives = 5
        self.score = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect(topleft = (x,y+15))
        #self.rect.x = x
        #self.rect.y = y
        self.collition_rect = pygame.Rect(x+self.rect.width/3,y,self.rect.width/3,self.rect.height)
        self.ground_collition_rect = pygame.Rect(self.collition_rect)
        self.ground_collition_rect.height = GROUND_COLLIDE_H
        self.ground_collition_rect.y = y + self.rect.height - GROUND_COLLIDE_H

        self.is_jump = False
        self.is_fall = False
        self.is_shoot = False
        self.is_knife = False

        self.tiempo_transcurrido_animation = 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height

        self.tiempo_transcurrido = 0
        self.tiempo_last_jump = 0 
        self.interval_time_jump = interval_time_jump
        self.score = 0
        self.shoot_sound = pygame.mixer.Sound("aagun.wav")
        self.shoot_sound.set_volume(0.1)
        self.muere_sound = pygame.mixer.Sound("human1.wav")
        self.muere_sound.set_volume(0.1)


        

    def walk(self,direction):
        if(self.is_jump == False and self.is_fall == False):
            if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
                self.frame = 0
                self.direction = direction
                if(direction == DIRECTION_R):
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                else:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l

    def shoot(self,on_off = True):
        self.is_shoot = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            self.shoot_sound.play()

            if(self.animation != self.shoot_r and self.animation != self.shoot_l):
                self.frame = 0
                self.is_shoot = True
                if(self.direction == DIRECTION_R):
                    self.animation = self.shoot_r
                else:
                    self.animation = self.shoot_l       

    def receive_shoot(self):
        self.lives -= 1
        if self.lives <= 0:
            print("player muere")
            self.muere_sound.play()
            
        

    def knife(self,on_off = True):
        self.is_knife = on_off
        if(on_off == True and self.is_jump == False and self.is_fall == False):
            if(self.animation != self.knife_r and self.animation != self.knife_l):
                self.frame = 0
                if(self.direction == DIRECTION_R):
                    self.animation = self.knife_r
                else:
                    self.animation = self.knife_l      

    def jump(self,on_off = True):
        if(on_off and self.is_jump == False and self.is_fall == False):
            self.y_start_jump = self.rect.y
            if(self.direction == DIRECTION_R):
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_r
            else:
                self.move_x = int(self.move_x / 2)
                self.move_y = -self.jump_power
                self.animation = self.jump_l
            self.frame = 0
            self.is_jump = True
        if(on_off == False):
            self.is_jump = False
            self.stay()

    def stay(self):
        if(self.is_knife or self.is_shoot):
            return

        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def change_x(self,delta_x):
        self.rect.x += delta_x
        self.collition_rect.x += delta_x
        self.ground_collition_rect.x += delta_x

    def change_y(self,delta_y):
        self.rect.y += delta_y
        self.collition_rect.y += delta_y
        self.ground_collition_rect.y += delta_y

    def do_movement(self,delta_ms,plataform_list):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0

            if(abs(self.y_start_jump - self.rect.y) > self.jump_height and self.is_jump):
                self.move_y = 0
          
            self.change_x(self.move_x)
            self.change_y(self.move_y)

            if(not self.is_on_plataform(plataform_list)):
                if(self.move_y == 0):
                    self.is_fall = True
                    self.change_y(self.gravity)
            else:
                if (self.is_jump): 
                    self.jump(False)
                self.is_fall = False            

    def is_on_plataform(self,plataform_list):
        retorno = False
        
        if(self.ground_collition_rect.bottom >= GROUND_LEVEL):
            retorno = True     
        else:
            for plataforma in  plataform_list:
                if(self.ground_collition_rect.colliderect(plataforma.ground_collition_rect)):
                    retorno = True
                    break       
        return retorno                 

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
                
            else: 
                self.frame = 0
 
    def update(self,delta_ms,plataform_list,botin_list):
        self.do_movement(delta_ms,plataform_list)
        self.do_animation(delta_ms)
        for botin in botin_list:
            if self.collition_rect.colliderect(botin.rect):
                botin_list.remove(botin)
                self.score += 100
                self.lives += 1
    
    def draw(self,screen):
        
        if(DEBUG):
            pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            pygame.draw.rect(screen,color=(255,255,0),rect=self.ground_collition_rect)
        
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        

    def events(self,delta_ms,keys):
        self.tiempo_transcurrido += delta_ms


        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_L)

        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_R)

        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()
        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()  

        if(keys[pygame.K_SPACE]):
            if((self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump):
                self.jump(True)
                self.tiempo_last_jump = self.tiempo_transcurrido

        if(not keys[pygame.K_a]):
            self.shoot(False)
  

        if(not keys[pygame.K_a]):
            self.knife(False)  

        if(keys[pygame.K_s] and not keys[pygame.K_a]):
            self.shoot()   
            if self.direction == DIRECTION_R:
                sentido = 1
            else :
                sentido = -1
                
            self.bullet_list.append(Bullet(self,self.rect.centerx,self.rect.centery,sentido * self.rect.centerx,self.rect.centery,20,path="images/gui/set_gui_01/Comic_Border/Bars/Bar_Segment05.png",frame_rate_ms=10000,move_rate_ms=20,width=5,height=5))

        
        if(keys[pygame.K_a] and not keys[pygame.K_s]):
            self.knife()   

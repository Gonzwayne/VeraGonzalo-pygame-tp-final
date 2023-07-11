from player import *
from constantes import *
from auxiliar import Auxiliar
import math

class Bullet():
    
    def __init__(self,owner,x_init,y_init,x_end,y_end,speed,path,frame_rate_ms,move_rate_ms,width=5,height=5) -> None:
        self.tiempo_transcurrido_move = 0
        self.tiempo_transcurrido_animation = 0
        self.image = pygame.image.load(path).convert()
        self.image = pygame.transform.scale(self.image,(width*2,height*2))
        self.rect = self.image.get_rect()
        self.x = x_init
        self.y = y_init
        self.owner = owner
        self.rect.x = x_init
        self.rect.y = y_init
        self.frame_rate_ms = frame_rate_ms
        self.move_rate_ms = move_rate_ms
        angle = math.atan2(y_end - y_init, x_end - x_init)
        

        self.move_x = math.cos(angle)*speed
        self.move_y = math.sin(angle)*speed
        
        self.is_active = True 
        self.muere_sound = pygame.mixer.Sound("human3.wav")
        self.muere_sound.set_volume(0.1)
        
        
        
   
    def change_x(self,delta_x):
        self.x = self.x + delta_x
        self.rect.x = int(self.x)   

    def change_y(self,delta_y):
        self.y = self.y + delta_y
        self.rect.y = int(self.y)

    def do_movement(self,delta_ms,plataform_list,enemy_list,player):
        self.tiempo_transcurrido_move += delta_ms
        if(self.tiempo_transcurrido_move >= self.move_rate_ms):
            self.tiempo_transcurrido_move = 0
            self.change_x(self.move_x)
            self.change_y(self.move_y)
            self.check_impact(plataform_list,enemy_list,player)

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            pass
    
    

    def check_impact(self, plataform_list, enemy_list, player):
        if self.is_active and self.owner != player and self.rect.colliderect(player.rect):
            print("IMPACTO PLAYER")
            player.receive_shoot()
            self.is_active = False

        
        for aux_enemy in enemy_list:
            if self.is_active and self.owner != aux_enemy and self.rect.colliderect(aux_enemy.rect):
                print("IMPACTO ENEMY")
                self.is_active = False
                if self.owner == player:
                    
                    if aux_enemy.impactos <= 2:
                        aux_enemy.impactos += 1
                    else:
                        self.muere_sound.play()
                        enemy_list.remove(aux_enemy)
                    
                elif aux_enemy.can_be_shot:
                    aux_enemy.receive_shoot()

        for aux_plataform in plataform_list:
            if self.is_active and self.rect.colliderect(aux_plataform.rect):
                print("IMPACTO CON PLATAFORMA")
                self.is_active = False

            

    def update(self,delta_ms,plataform_list,enemy_list,player):
        self.do_movement(delta_ms,plataform_list,enemy_list,player)
        
        self.do_animation(delta_ms) 

    def draw(self,screen):
        if(self.is_active):
            #if(DEBUG):
             #   pygame.draw.rect(screen,color=(255,0 ,0),rect=self.collition_rect)
            screen.blit(self.image,self.rect)

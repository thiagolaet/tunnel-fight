from PPlay.window import *
from PPlay.gameimage import *
from PPlay.gameobject import *
from PPlay.animation import *
import globals

#class Enemys():


class Enemy1():
    def __init__(self, janela, enemy, x, y):
        self.janela = janela
        self.enemy = enemy

        self.enemy = Animation("assets/enemy1-medium.png", 70)
        self.enemy.set_position(x, y)
        self._set_seq_time()
        
        #1 = direita / 2 = esquerda
        self.direcao = 2

        #1 - idleRight / 1.5 - idleLeft / 2 - walkRight / 2.5 - walkLeft / 3 3.5 - attack1 / 4 4.5 - attack2 / 5 5.5 - attack3 / 6 6.5 - attack4  
        self.enemy_state = 1
        self.contadorAnimacao = 0
        self.enemy.set_sequence(0, 4)


    def _set_seq_time(self):
        self.enemy.set_sequence_time(0, 4, 130) #IDLE
        self.enemy.set_sequence_time(4, 8, 130) #IDLE
        self.enemy.set_sequence_time(8, 14, 100) #WALK
        self.enemy.set_sequence_time(14, 20, 100) #WALK
        self.enemy.set_sequence_time(20, 25, 220) #attack1
        self.enemy.set_sequence_time(25, 30, 220) #attack1
        self.enemy.set_sequence_time(30, 33, 200) #hit 1
        self.enemy.set_sequence_time(33, 36, 200) #hit 1
        self.enemy.set_sequence_time(36, 39, 200) #hit 2
        self.enemy.set_sequence_time(39, 42, 200) #hit 2
        self.enemy.set_sequence_time(42, 56, 200) #die
        self.enemy.set_sequence_time(56, 69, 200) #die

    def idleRight(self):
        if self.enemy_state != 1:
            self.enemy.set_sequence(0, 4)
            self.enemy_state = 1

    def idleLeft(self):
        if self.enemy_state != 1.5:
            self.enemy.set_sequence(4, 8)
            self.enemy_state = 1.5

    def walkRight(self):
        if self.enemy_state != 2: 
            self.enemy.set_sequence(8, 14)
            self.enemy_state = 2
            self.enemy.y -= 0.2
            self.enemy.y += 0.2
        self.enemy.x += 2 * self.janela.delta_time() * globals.frame_per_SECOND
        self.direcao = 1

    def walkRightUp(self):
        if self.enemy_state != 2: 
            self.enemy.set_sequence(8, 14)
            self.enemy_state = 2
        self.enemy.y -= 0.2        
        self.enemy.x += 2 * self.janela.delta_time() * globals.frame_per_SECOND
        self.direcao = 1

    def walkRightDown(self):
        if self.enemy_state != 2: 
            self.enemy.set_sequence(8, 14)
            self.enemy_state = 2
        self.enemy.y += 0.2
        self.enemy.x += 2 * self.janela.delta_time() * globals.frame_per_SECOND
        self.direcao = 1

    def walkLeft(self):
        if self.enemy_state != 2.5:
            self.enemy.set_sequence(14, 20)
            self.enemy_state = 2.5
        self.enemy.x -= 2 * self.janela.delta_time() * globals.frame_per_SECOND
        self.direcao = 2
    
    def walkLeftUp(self):
        if self.enemy_state != 2.5:
            self.enemy.set_sequence(14, 20)
            self.enemy_state = 2.5
        self.enemy.y -= 0.2
        self.enemy.x -= 2 * self.janela.delta_time() * globals.frame_per_SECOND
        self.direcao = 2

    def walkLeftDown(self):
        if self.enemy_state != 2.5:
            self.enemy.set_sequence(14, 20)
            self.enemy_state = 2.5
        self.enemy.y += 0.2
        self.enemy.x -= 2 * self.janela.delta_time() * globals.frame_per_SECOND
        self.direcao = 2

    def walkUp(self):
        if self.direcao == 1:
            self.enemy.y -= 0.2
            if self.enemy_state != 2: 
                self.enemy.set_sequence(8, 14)
                self.enemy_state = 2
        if self.direcao == 2:
            self.enemy.y -= 0.2
            if self.enemy_state != 2.5: 
                self.enemy.set_sequence(14, 20)
                self.enemy_state = 2.5

    def walkDown(self):
        if self.direcao == 1:
            self.enemy.y += 0.2
            if self.enemy_state != 2: 
                self.enemy.set_sequence(8, 14)
                self.enemy_state = 2
        if self.direcao == 2:
            self.enemy.y += 0.2
            if self.enemy_state != 2.5: 
                self.enemy.set_sequence(14, 20)
                self.enemy_state = 2.5

    def attack(self):
        if self.direcao == 1:
            if self.enemy_state != 3:
                self.enemy.set_sequence(20, 25)
                self.enemy.set_curr_frame(20)
                self.enemy_state = 3
                self.contadorAnimacao = 0
        elif self.direcao == 2:
            if self.enemy_state != 3.5:
                self.enemy.set_sequence(25, 30)
                self.enemy.set_curr_frame(25)
                self.enemy_state = 3.5
                self.contadorAnimacao = 0

    def checarcontadorAnimacao(self):
        if self.enemy_state == 3 or self.enemy_state == 3.5:
            return 1.4
        elif self.enemy_state == 4 or self.enemy_state == 4.5:
            return 1.4
        elif self.enemy_state == 5 or self.enemy_state == 5.5:
            return 1.9
        elif self.enemy_state == 6 or self.enemy_state == 6.5:
            return 1.9        
        else: return 0

    def run(self):
        tempocontadorAnimacao = self.checarcontadorAnimacao()

        if self.contadorAnimacao >= tempocontadorAnimacao:
            if self.direcao == 1:
                self.idleRight()
            elif self.direcao == 2:
                self.idleLeft()

        self.contadorAnimacao += self.janela.delta_time()
        self.enemy.draw()
        self.enemy.play()
        self.enemy.update()
        self.contadorAnimacao += self.janela.delta_time()
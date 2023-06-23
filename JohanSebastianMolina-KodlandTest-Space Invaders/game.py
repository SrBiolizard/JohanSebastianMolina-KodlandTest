import pygame
import random

from pygame.sprite import AbstractGroup

pygame.init()
pygame.mixer.init()

fondo=pygame.image.load('imagenes/fondo1.jpg')
laser_sonido = pygame.mixer.Sound('laser.wav')
explosion_sonido = pygame.mixer.Sound('explosion.wav')
golpe_sonido = pygame.mixer.Sound('golpe.wav')

animacion_Arr=[]
for i in range(1,13):
    explosion=pygame.image.load(f'explosion/{i}.png')
    animacion_Arr.append(explosion)

width = fondo.get_width()
height= fondo.get_height()
window= pygame.display.set_mode((width,height))
pygame.display.set_mode((width,height))
pygame.display.set_caption('KodLand SpaceInvaders By JohanSebastianMolina')

run=True
fps=60
clock=pygame.time.Clock()
score=0
vida=100
white=(255,255,255)
black=(0,0,0)
pausado = False
tiempo_entre_disparos=0  
font=pygame.font.SysFont('Small Fonts', 30, bold=True)

def mostrar_mensaje_final(score):
    run_mensaje = True
    while run_mensaje:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        window.fill(black)
        texto_puntuación(window, '¡Felicidades!', 50, width // 2, height // 2 - 50)
        texto_puntuación(window, 'PUNTUACION:', 40, width // 2, height // 2 + 50)
        texto_puntuación(window, str(score), 60, width // 2, height // 2 + 120)
        texto_puntuación(window, 'Suerte en tu próximo intento!', 30, width // 2, height // 2 + 220)

        pygame.display.update()

def texto_puntuación(frame,text,size,x,y):
    font=pygame.font.SysFont('Small Fonts', size, bold=True)
    text_frame=font.render(text,True,white,black)
    text_rect=text_frame.get_rect()
    text_rect.midtop=(x,y)
    frame.blit(text_frame, text_rect)

def barra_vida(frame,x,y, nivel):
    longitud=100
    alto=20
    fill= int((nivel/100)*longitud)
    border=pygame.Rect(x,y, longitud, alto)
    fill=pygame.Rect(x,y,fill, alto)
    pygame.draw.rect(frame, (255,0,255), fill)
    pygame.draw.rect(frame, black,border,4)
####################################################################################################################
class Balas(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image=pygame.image.load('imagenes/thunder.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.y=y
        self.velocidad=-5
    
    def update(self):
        self.rect.y += self.velocidad
        if self.rect.bottom<0:
            self.kill()
####################################################################################################################
class Jefe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('imagenes/jefe.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = width // 2
        self.rect.centery = -100  # Empieza arriba de la pantalla
        self.velocidad_y = 2
        self.vida = 500

    def update(self):
        self.rect.y += 1
        if self.rect.top >height:
            self.kill()

    def disparar_jefe(self):
        bala = Balas_enemigos(self.rect.centerx, self.rect.bottom)
        grupo_jugador.add(bala)
        grupo_balas_enemigos.add(bala)
        laser_sonido.play()

    def recibir_danio(self, danio):
        self.vida -= danio
        if self.vida <= 0:
            global score
            score += 100
            explo = Explosion(self.rect.center)
            grupo_jugador.add(explo)
            explosion_sonido.play()
            self.rect.y = -100  # Reiniciar su posición arriba de la pantalla
            self.vida = 500
            # Volver a generar los enemigos pequeños
            for _ in range(10):
                enemigo = Enemigos(10, 10)
                grupo_enemigos.add(enemigo)
                grupo_jugador.add(enemigo)
####################################################################################################################
class Balas_enemigos(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load('imagenes/booger.png').convert_alpha()
        self.image= pygame.transform.rotate(self.image, 180)
        self.rect=self.image.get_rect()
        self.rect.centerx=x
        self.rect.y=random.randrange(10,width)
        self.velocidad_y=4

    def update(self):
        self.rect.y += self.velocidad_y 
        if self.rect.bottom > height:
            self.kill()
####################################################################################################################
class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('imagenes/nave.png').convert_alpha()
        pygame.display.set_icon(self.image)
        self.rect= self.image.get_rect()
        self.rect.centerx=width//2
        self.rect.centery=height-50
        self.velocidad_x=0
        self.vida=100

    def update(self):
        self.velocidad_x = 0
        self.velocidad_y = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.velocidad_x = -5
        elif keystate[pygame.K_RIGHT]:
            self.velocidad_x = 5
        if keystate[pygame.K_UP]:
            self.velocidad_y = -5
        elif keystate[pygame.K_DOWN]:
            self.velocidad_y = 5
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        if self.rect.right > width:
            self.rect.right = width
        elif self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > height:
            self.rect.bottom = height
        elif self.rect.top < 0:
            self.rect.top = 0
    # Controlamos el disparo
       # if keystate[pygame.K_DOWN]:
        #    self.disparar()

    def disparar(self):
        bala=Balas(self.rect.centerx, self.rect.top)
        grupo_jugador.add(bala)
        grupo_balas_jugador.add(bala)
        laser_sonido.play()
####################################################################################################################
class Enemigos(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('imagenes/alien.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1, width - 50)
        self.rect.y = random.randrange(-height, -50)  # Empiezan fuera de la pantalla


    def update(self):
        self.rect.y += 1  # Velocidad vertical de movimiento de los enemigos
        if self.rect.top > height:  # Si los enemigos salen de la pantalla
            self.rect.x = random.randrange(1, width - 50)
            self.rect.y = random.randrange(-height, -50)  # Reiniciar su posición fuera de la pantalla
           # self.kill()
    def disparar_enemigos(self):
        global tiempo_entre_disparos
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - tiempo_entre_disparos > delay:  # Esperar 1 segundo entre disparos
            tiempo_entre_disparos = tiempo_actual
            bala = Balas_enemigos(self.rect.centerx, self.rect.bottom)
            grupo_jugador.add(bala)
            grupo_balas_enemigos.add(bala)
            laser_sonido.play()
####################################################################################################################
class Explosion(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__()
        self.image = animacion_Arr[0]
        img_scala = pygame.transform.scale(self.image,(20,20))
        self.rect = img_scala.get_rect()
        self.rect.center = position
        self.time = pygame.time.get_ticks()
        self.velocidad_explo=30
        self.frames=0

    def update(self):
        tiempo=pygame.time.get_ticks()
        if tiempo-self.time>self.velocidad_explo:
            self.time=tiempo
            self.frames+=1
            if self.frames == len(animacion_Arr):
                self.kill()
            else:
                position = self.rect.center
                self.image = animacion_Arr[self.frames]
                self.rect=self.image.get_rect()
                self.rect.center=position
####################################################################################################################
grupo_jugador=pygame.sprite.Group()
grupo_enemigos=pygame.sprite.Group()
grupo_balas_jugador=pygame.sprite.Group()
grupo_balas_enemigos=pygame.sprite.Group()
player=Jugador()
grupo_jugador.add(player)

for x in range(10):
    enemigo=Enemigos(10,10)
    grupo_enemigos.add(enemigo)
    grupo_jugador.add(enemigo)
    
jefe = None
contador_jefes = 0
PUNTOS_PARA_JEFE = 7

def cambiar_dificultad(nueva_dificultad):
    global delay
    if nueva_dificultad == 'facil':
        delay = 2000
    elif nueva_dificultad == 'medio':
        delay= 1000
    elif nueva_dificultad == 'dificil':
        delay= 300

# Función para mostrar el menú de dificultad
def mostrar_menu_dificultad():
    run_menu = True
    while run_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run_menu = False

        window.blit(fondo, (0, 0))
        texto_puntuación(window, 'PUNTUACION: ' + str(score), 30, width - 85, 2)

        texto_dificultad = font.render('Selecciona la dificultad:', True, white)
        texto_facil = font.render('Fácil (2 segundos)', True, white)
        texto_medio = font.render('Medio (1 segundo)', True, white)
        texto_dificil = font.render('Difícil (0.3 segundos)', True, white)

        window.blit(texto_dificultad, (width // 2 - texto_dificultad.get_width() // 2, height // 2 - 100))
        window.blit(texto_facil, (width // 2 - texto_facil.get_width() // 2, height // 2 - 50))
        window.blit(texto_medio, (width // 2 - texto_medio.get_width() // 2, height // 2))
        window.blit(texto_dificil, (width // 2 - texto_dificil.get_width() // 2, height // 2 + 50))

        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if width // 2 - texto_facil.get_width() // 2 < mouse_pos[0] < width // 2 + texto_facil.get_width() // 2 \
                and height // 2 - 50 < mouse_pos[1] < height // 2 - 50 + texto_facil.get_height():
            if click[0] == 1:
                cambiar_dificultad('facil')
                run_menu = False

        if width // 2 - texto_medio.get_width() // 2 < mouse_pos[0] < width // 2 + texto_medio.get_width() // 2 \
                and height // 2 < mouse_pos[1] < height // 2 + texto_medio.get_height():
            if click[0] == 1:
                cambiar_dificultad('medio')
                run_menu = False

        if width // 2 - texto_dificil.get_width() // 2 < mouse_pos[0] < width // 2 + texto_dificil.get_width() // 2 \
                and height // 2 + 50 < mouse_pos[1] < height // 2 + 50 + texto_dificil.get_height():
            if click[0] == 1:
                cambiar_dificultad('dificil')
                run_menu = False

        pygame.display.update()

# Mostrar el menú de dificultad antes de iniciar el bucle principal del juego
mostrar_menu_dificultad()

while True:
    clock.tick(fps)
    window.blit(fondo, (0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            mostrar_mensaje_final(score)  # Mostrar mensaje final antes de cerrar la ventana
            
            quit()   
        elif event.type==pygame.KEYDOWN:
            player.disparar()

    
    grupo_jugador.update()
    grupo_enemigos.update()
    grupo_balas_jugador.update()
    grupo_balas_enemigos.update()

    grupo_jugador.draw(window)

    #Coliciones balas_jugador - enemigo
    colicion1=pygame.sprite.groupcollide(grupo_balas_jugador,grupo_enemigos,True,True)
    contador_jefes += len(colicion1)
    if contador_jefes >= PUNTOS_PARA_JEFE:
        jefe = Jefe()
        grupo_jugador.add(jefe)
        grupo_enemigos.add(jefe)
        contador_jefes = 0  # Reiniciar el contador de jefes
    for i in colicion1:
        score+=10
        enemigo.disparar_enemigos()
        enemigo=Enemigos(300,10)
        grupo_enemigos.add(enemigo)
        grupo_jugador.add(enemigo)

        explo = Explosion(enemigo.rect.center)
        grupo_jugador.add(explo)
        explosion_sonido.set_volume(0.3)
        explosion_sonido.play() 

    #Coliciones jugador - balas enemigo
    colicion2 = pygame.sprite.spritecollide(player,grupo_balas_enemigos,True)
    for j in colicion2:
        player.vida-=10
        if player.vida<=0:
            mostrar_mensaje_final(score)  # Mostrar mensaje final antes de cerrar la ventana
            pygame.quit()
            quit()
            run = False
        explo1 = Explosion(j.rect.center)
        grupo_jugador.add(explo1)
        golpe_sonido.play()

    #Coliciones jugador - enemigo
    colicion3=pygame.sprite.spritecollide(player,grupo_enemigos,False)
    for k in colicion3:
        player.vida-=100
        enemigos=Enemigos(10,10)
        grupo_jugador.add(enemigos)
        grupo_enemigos.add(enemigos) 
        if player.vida <=0:
            mostrar_mensaje_final(score)  # Mostrar mensaje final antes de cerrar la ventana
            pygame.quit()
            quit()
            run=False

    #indicador y score
    texto_puntuación(window,(' PUNTUACION: '+str(score)+'  '),30, width-85,20)
    barra_vida(window, width-285,0,player.vida)

    pygame.display.flip()
#pygame.quit()




import pygame
from random import *

pygame.init()

screen_width = 1200
screen_heigth = 610
screen = pygame.display.set_mode((screen_width,screen_heigth))

pygame.display.set_caption("도망쳐 페파피그!")

background1 = pygame.image.load("C:\\Users\\김기호\\Desktop\\조단\\Git Hub\\Dan\\FirstGame\\pyGame_basic\\background.png")
background2 = pygame.image.load("C:\\Users\\김기호\\Desktop\\조단\\Git Hub\\Dan\\FirstGame\\pyGame_basic\\backgrounp.png")

mainpeppa = pygame.image.load("C:\\Users\\김기호\\Desktop\\조단\\Git Hub\\Dan\\FirstGame\\pyGame_basic\\chr1.png")
maindaddy = pygame.image.load("C:\\Users\\김기호\\Desktop\\조단\\Git Hub\\Dan\\FirstGame\\pyGame_basic\\daddy.png")

mainpeppa_size = mainpeppa.get_rect().size
mainpeppa_width = mainpeppa_size[0]
mainpeppa_height = mainpeppa_size[1]
mainpeppa_x_pos = (screen_width/2) - (mainpeppa_width/2)
mainpeppa_y_pos = screen_heigth - mainpeppa_height

maindaddy_size = maindaddy.get_rect().size
maindaddy_width = maindaddy_size[0]
maindaddy_height = maindaddy_size[1]
maindaddy_x_pos = randint(0,screen_width - maindaddy_width)
maindaddy_y_pos = 0
maindaddy_speed = 5

total_time = 100
game_font = pygame.font.SysFont("d2codingd2codingd2codingligatured2codingligaturebold", 25)
start_ticks = pygame.time.get_ticks()

clock = pygame.time.Clock()

to_x = 0
peppa_speed = 0.6

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        press_k = game_font.render("PRESS \'K\' KEY To Start Game",True,(255,255,255))
        screen.blit(background1, (0, 0))
        screen.blit(press_k,(430,520))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                running = False

    pygame.display.update()


running = True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:  # 키가 눌린지 확인(down = 누르다로 해석)
            if event.key == pygame.K_LEFT:  # 왼쪽으로 이동
                to_x -= peppa_speed
            elif event.key == pygame.K_RIGHT:  # 케릭터를 오른쪽으로
                to_x += peppa_speed
        if event.type == pygame.KEYUP:  # 방향키를 때면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0


    mainpeppa_x_pos += to_x * dt

    if mainpeppa_x_pos < 0:
        mainpeppa_x_pos = 0
    elif mainpeppa_x_pos > screen_width - mainpeppa_width:
        mainpeppa_x_pos = screen_width - mainpeppa_width


    mainpeppa_rect = mainpeppa.get_rect()
    mainpeppa_rect.left = mainpeppa_x_pos
    mainpeppa_rect.top = mainpeppa_y_pos

    maindaddy_rect = maindaddy.get_rect()
    maindaddy_rect.left = maindaddy_x_pos
    maindaddy_rect.top = maindaddy_y_pos

    if mainpeppa_rect.colliderect(maindaddy_rect):
        print("충돌했어요")
        running = False

    maindaddy_y_pos += maindaddy_speed
    if maindaddy_y_pos > screen_heigth:
        maindaddy_y_pos = 0
        maindaddy_x_pos = randint(0, screen_width - maindaddy_width)


    screen.blit(background2,(0,0))
    screen.blit(mainpeppa,(mainpeppa_x_pos,mainpeppa_y_pos))
    screen.blit(maindaddy, (maindaddy_x_pos,maindaddy_y_pos))


    laptime = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render("종료까지 : "+str(int(total_time - laptime)),True,(255,255,255))
    screen.blit(timer,(15,15))
    if total_time - laptime < 0:
        print("타임 아웃")
        running = False


    pygame.display.update()
pygame.time.delay(1000)
pygame.quit()
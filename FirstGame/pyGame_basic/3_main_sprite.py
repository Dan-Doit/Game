import pygame

pygame.init() # 초기화 반드시 필요!

# 화면크기 설정
screen_width = 1200  # 가로크기
screen_height = 610 # 세로크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("조단 게임") # 게임 이름
# 백그라운드 이미지 불러오기
background = pygame.image.load("C:\\Users\\김기호\\Desktop\\조단\\Git Hub\\Dan\\FirstGame\\pyGame_basic\\background.png")
character = pygame.image.load("C:\\Users\\김기호\\Desktop\\조단\\Git Hub\\Dan\\FirstGame\\pyGame_basic\\chr1.png")
character_size = character.get_rect().size # 이미지의 크기를 불러옴
character_width = character_size[0]  # 케릭터의 가로크기
character_height = character_size[1] # 케릭터의 세로크기
character_x_pos = (screen_width/2) - (character_width/2)    # 화면 가로의 절반크기 위치(position)
character_y_pos = screen_height - character_height  # 화면 세로의 가장아래 위치(케릭터의 값을 빼야 함! 이유는 알아서 생각)

# 이벤트 루프
running = True  #게임이 진행중인가
while running:
    for event in pygame.event.get():    # 파이게임을 시작하기위해 무조건 적어야함(키보드와 마우스 동작 확인)
        if event.type == pygame.QUIT:   # 창을닫을때 나가기를 함 True -> False
            running = False
    # screen.fill((0,0,255))            # RGB 값으로 배경을 채울수도있다.
    screen.blit(background,(0,0))       # 0,0 배경 입히기
    screen.blit(character,(character_x_pos,character_y_pos)) # 캐릭터 그리기


    pygame.display.update()             # 게임화면을 계속 보이게 업데이트함
# 게임이 종료시점
pygame.quit()
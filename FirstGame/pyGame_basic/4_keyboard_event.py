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
# 이동할 좌표
to_x = 0
to_y = 0


# 이벤트 루프
running = True  #게임이 진행중인가
while running:
    for event in pygame.event.get():    # 파이게임을 시작하기위해 무조건 적어야함(키보드와 마우스 동작 확인)
        if event.type == pygame.QUIT:   # 창을닫을때 나가기를 함 True -> False
            running = False

        if event.type == pygame.KEYDOWN:# 키가 눌린지 확인(down = 누르다로 해석)
            if event.key == pygame.K_LEFT: # 왼쪽으로 이동
                to_x -= 5
            elif event.key == pygame.K_RIGHT: # 케릭터를 오른쪽으로
                to_x += 5
            elif event.key == pygame.K_DOWN:
                to_y += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
        if event.type == pygame.KEYUP:  # 방향키를 때면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y
    if character_x_pos < 0:            # 가로 경계값 처리
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # screen.fill((0,0,255))            # RGB 값으로 배경을 채울수도있다.
    screen.blit(background,(0,0))       # 0,0 배경 입히기
    screen.blit(character,(character_x_pos,character_y_pos)) # 캐릭터 그리기


    pygame.display.update()             # 게임화면을 계속 보이게 업데이트함
# 게임이 종료시점
pygame.quit()
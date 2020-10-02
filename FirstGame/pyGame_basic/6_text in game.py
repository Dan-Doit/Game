import pygame

pygame.init() # 초기화 반드시 필요!

# 화면크기 설정
screen_width = 1200  # 가로크기
screen_height = 610 # 세로크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("조단 게임") # 게임 이름

# FPS
clock = pygame.time.Clock()
# 백그라운드 이미지 불러오기
background = pygame.image.load("C:\\Users\\김기호\\Desktop\\조단\\Git Hub\\Dan\\FirstGame\\pyGame_basic\\background.png")
# 주인공 케릭터
character = pygame.image.load("C:\\Users\\김기호\\Desktop\\조단\\Git Hub\\Dan\\FirstGame\\pyGame_basic\\chr1.png")
character_size = character.get_rect().size # 이미지의 크기를 불러옴
character_width = character_size[0]  # 케릭터의 가로크기
character_height = character_size[1] # 케릭터의 세로크기
character_x_pos = (screen_width/2) - (character_width/2)    # 화면 가로의 절반크기 위치(position)
character_y_pos = screen_height - character_height  # 화면 세로의 가장아래 위치(케릭터의 값을 빼야 함! 이유는 알아서 생각)

# 적 케릭터
enemy = pygame.image.load("C:\\Users\\김기호\\Desktop\\조단\\Git Hub\\Dan\\FirstGame\\pyGame_basic\\en1.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 불러옴
enemy_width = enemy_size[0]  # 케릭터의 가로크기
enemy_height = enemy_size[1] # 케릭터의 세로크기
enemy_x_pos = (screen_width/2) - (enemy_width/2)    # 화면 가로의 절반크기 위치(position)
enemy_y_pos = (screen_height/2) - (enemy_height/2)  # 화면 세로의 가장아래 위치(케릭터의 값을 빼야 함! 이유는 알아서 생각)

# 폰트 정의 :                  폰트,사이즈
game_font = pygame.font.Font(None, 40)
# 시간정보
total_time = 10
# 시간 계산
start_ticks = pygame.time.get_ticks() # 현재 tick 을 받아옴


# 이동할 좌표
to_x = 0
to_y = 0

character_speed = 0.6

# 이벤트 루프
running = True  #게임이 진행중인가
while running:
    # 케릭터가 100 만큼 이동 하려면
    # FPS 10 : 1초에 100 가려면 10*(10) 이동력이 10이 되야함
    # FPS 20 : 1초에 100 가려면 20*(5) 이동력이 5가 되어야함
    dt = clock.tick(60)                 # 게임의 초당 프레임수를 설정 (지금은 30)
    for event in pygame.event.get():    # 파이게임을 시작하기위해 무조건 적어야함(키보드와 마우스 동작 확인)
        if event.type == pygame.QUIT:   # 창을닫을때 나가기를 함 True -> False
            running = False

        if event.type == pygame.KEYDOWN:# 키가 눌린지 확인(down = 누르다로 해석)
            if event.key == pygame.K_LEFT: # 왼쪽으로 이동
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 케릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
        if event.type == pygame.KEYUP:  # 방향키를 때면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                to_y = 0

    # 케릭터 포지션은 누르는 키값 * 프레임값(프레임에 따라 움직이는 속도가 변하면 안댐)
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    if character_x_pos < 0:            # 가로 경계값 처리
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False
    # screen.fill((0,0,255))            # RGB 값으로 배경을 채울수도있다.
    screen.blit(background,(0,0))       # 0,0 배경 입히기
    screen.blit(character,(character_x_pos,character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos)) # 적군 그리기

    # 타이머 집어넣기 (밀리 세컨드라 평범한 초로 바꾸려면 1000으로 나누어야한다.)
    laptime = (pygame.time.get_ticks() - start_ticks) / 1000
            #      렌더 정보표시   정보 (정해준 시간 - 랩타임),(필)True,RGB 글자색상
    timer = game_font.render(str(int(total_time - laptime)),True,(255,255,255))
    # 출력할 위치
    screen.blit(timer,(10,10))
    if total_time - laptime < 0 :
        print("타임 아웃")
        running = False

    pygame.display.update()             # 게임화면을 계속 보이게 업데이트함

# 잠시 대기 (2초) 밀리타임이라 2000곱함
pygame.time.delay(1000)
# 게임이 종료시점
pygame.quit()
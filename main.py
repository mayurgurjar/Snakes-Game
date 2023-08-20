import pygame
import random
import os
pygame.mixer.init()
pygame.init()
screen_width = 600
screen_height = 600

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
green = (0,255,0)
blue = (0,255,255)

gamewindow = pygame.display.set_mode((screen_width,screen_height))
backgroungimage = pygame.image.load("bg.jpg")
backgroungimage = pygame.transform.scale(backgroungimage, (screen_width , screen_height)).convert_alpha()
gamecaption=  pygame.display.set_caption("game hi game")

exit_game= False
game_end =False

snake_x = 10
snake_y = 10
snake_size = 15
food_size = 10
score =  0
food_x = random.randint(0,screen_width)
food_y = random.randint(0,screen_height)
fps = 40
clock = pygame.time.Clock()
velocity_x = 0
velocity_y = 0

font = pygame.font.SysFont(None , 60 )
def screen_score(text , color , x,y):
    screen_text = font.render(text , True , color)
    gamewindow.blit(screen_text , [x,y])

def snake_plot(gamewindow , color ,snake_list , snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gamewindow , color , [x ,y , snake_size , snake_size])

font1 = pygame.font.SysFont(None , 55)
def screen_gameover(text , color , x,y):
    game_text = font1.render(text , True ,color )
    gamewindow.blit(game_text  , [x,y])

snake_list = []
snake_length = 1

def welcome():

    pygame.mixer.music.load('carry.voice.mp3')
    pygame.mixer.music.play()

    exit_game = False
    while not exit_game:
        gamewindow.fill(blue)
        backgroungimage = pygame.image.load("carry.jfif")
        backgroungimage = pygame.transform.scale(backgroungimage , (screen_width,screen_height)).convert_alpha()
        gamewindow.blit(backgroungimage , (0,0))

        screen_score("space daba chalu kar bhidu", red, 10,50)
        for event in pygame.event.get():
            if event==pygame.QUIT:
                exit_game=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                 gameloop()

        pygame.display.update()
        clock.tick(fps)



def gameloop():
    snake_list = []
    snake_length = 1

    exit_game = False
    game_end = False

    snake_x = 10
    snake_y = 10
    snake_size = 15
    food_size = 10
    score = 0
    food_x = random.randint(0, screen_width)
    food_y = random.randint(0, screen_height)
    fps = 40
    clock = pygame.time.Clock()
    velocity_x = 0
    velocity_y = 0

    while not exit_game:
        if game_end:
            gamewindow.fill(white)
            image = pygame.image.load("bhau.jpg")
            image = pygame.transform.scale(image , (screen_width,screen_height)).convert_alpha()
            gamewindow.blit(image, (0,0))
            screen_gameover("Game Over! khatam"   ,red  ,101,50  )

            for event in pygame.event.get():
                print(event)

                if event.type == pygame.QUIT:
                    exit_game = True


                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:

                        welcome()
        else :
            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                      exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x= 2
                        velocity_y =0

                    if event.key==pygame.K_LEFT:
                        velocity_x = -2
                        velocity_y = 0
                    if event.key==pygame.K_UP:
                        velocity_y = -2
                        velocity_x = 0
                    if event.key==pygame.K_DOWN:
                        velocity_y = 2
                        velocity_x = 0

            snake_x = snake_x+velocity_x
            snake_y = snake_y+velocity_y

            if abs(snake_x-food_x)<15 and abs(snake_y-food_y)<15:
                score+=1
                print("score:" , score)
                food_x = random.randint(0, screen_width)
                food_y = random.randint(0, screen_height)
                snake_length+=5




            gamewindow.fill(green)
            gamewindow.blit(backgroungimage ,( 0,0 ))

            pygame.draw.rect(gamewindow , black , [snake_x , snake_y , snake_size , snake_size])
            snake_plot(gamewindow , black , snake_list , snake_size)
            screen_score("score:" + str(score * 1) , red, 6, 6)



            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)


            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                 game_end=True
            pygame.mixer.music.load('khatam.mp3')
            pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_end = True
                print("game over by ")
                pygame.mixer.music.load('khatam.mp3')
                pygame.mixer.music.play()

            pygame.draw.rect(gamewindow , red, [food_x , food_y , food_size , food_size])
        pygame.display.update()

        clock.tick(fps)

    pygame.quit()
    quit()
welcome()

a = input()

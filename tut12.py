import pygame
import random
pygame.init()

#colors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)


#creating game window
gameWindow = pygame.display.set_mode((1200,500))

#Game title
pygame.display.set_caption("Snake Game")
# pygame.display.update()


#game specific variables
exit_game = False
game_over = False
snake_x = 45   # location in x
snake_y = 55  # location in y
snake_size = 10  # size of snake initially
velocity_x =0
velocity_y =0
init_velocity = 3
food_x = random.randint(20,1000)
food_y = random.randint(20,400)
food_size = 10
score = 0


fps = 60
clock = pygame.time.Clock()    #Acc to particular time we have to update the frame of game
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN: #matlab mene koi key dabai
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x = -init_velocity
                velocity_y = 0

            if event.key == pygame.K_UP:
                velocity_y = -init_velocity
                velocity_x = 0

            if event.key == pygame.K_DOWN:
                velocity_y = init_velocity
                velocity_x = 0

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    if abs(snake_x - food_x)<6 and abs(snake_y-food_y)<6:
        score+=10
        print("score: ",score)
        food_x = random.randint(20, 1000)
        food_y = random.randint(20, 400)


    gameWindow.fill(white)   # background colour ko white se fill kardega aur yeh tabhi chalega jab hum pygame.display.update function challayenge
    #rectangle banane ke liye humne nichla function use kiya hai jo snake ke head ka kaam karega aur uske parameter's hai:-
    #gameWindow : - Kis jagah pe rectangle banana hai
    #black :- kis colour ka banana hai
    #[snake_x, snake_y, snake_size, snake_size] :- coordinate position of snake in pygame window , snake ki length and width
    pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.draw.rect(gameWindow, red, [food_x, food_y, food_size, food_size])
    pygame.display.update()
    clock.tick(fps)
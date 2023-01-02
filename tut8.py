import pygame
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
fps = 30
clock = pygame.time.Clock()    #Acc to particular time we have to update the frame of game
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN: #matlab mene koi key dabai
            if event.key == pygame.K_RIGHT:
                snake_x = snake_x + 10

            if event.key == pygame.K_LEFT:
                snake_x = snake_x - 10

            if event.key == pygame.K_UP:
                snake_y = snake_y - 10

            if event.key == pygame.K_DOWN:
                snake_y = snake_y + 10


    gameWindow.fill(white)   # background colour ko white se fill kardega aur yeh tabhi chalega jab hum pygame.display.update function challayenge
    #rectangle banane ke liye humne nichla function use kiya hai jo snake ke head ka kaam karega aur uske parameter's hai:-
    #gameWindow : - Kis jagah pe rectangle banana hai
    #black :- kis colour ka banana hai
    #[snake_x, snake_y, snake_size, snake_size] :- coordinate position of snake in pygame window , snake ki length and width
    pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()
    clock.tick(fps)
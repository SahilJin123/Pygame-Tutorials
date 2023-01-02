import pygame
x = pygame.init()

pygamewindow = pygame.display.set_mode((1200,500))
pygame.display.set_caption("HungSnake")

exit_game = False
game_over = False

while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game = True
        if event.type == pygame.KEYDOWN:  # yeh line bata raha hai ki kya key dabi hai
            if event.key == pygame.K_RIGHT:  #yeh condition check kar raha hai ki right key dabi hai kya
                print("Right Key")

        # print(event)

pygame.quit()
quit()

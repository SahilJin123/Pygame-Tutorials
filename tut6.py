#tut is basically to Handle this present events in the game that is how game response when some particular button is pressed

import pygame
x = pygame.init()

gamewindow = pygame.display.set_mode((1200,500))
pygame.display.set_caption("My First Game")

#game specific variable
exit_game = False
game_over = False

#almost(jaise bade bade event) kisi bhi type ke event ko handle karne ke liye hum game specific variable banayenge
while not exit_game:
    for event in pygame.event.get():
        print(event)
    pass


pygame.quit()
quit()


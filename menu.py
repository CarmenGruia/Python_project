import pygame

pygame.init()

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

WIDTH = 600
HEIGHT = 600
BACKGROUND = (153, 51, 255)
LINE_COLOR = (204, 153, 255)
LINE_WIDTH = 15
FIGURE_WIDTH = 10
CIRCLE_RADIUS = 60


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('X _ 0')
screen.fill(BACKGROUND)


def buttons_draw():
    pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(200, 270, 200, 70), 3)
    pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(200, 370, 200, 70), 3)
    pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(200, 470, 200, 70), 3)


def main_menu():
    myimage = pygame.image.load("ox.png")
    text1 = myfont.render('Easy', False, LINE_COLOR)
    text2 = myfont.render('Medium', False, LINE_COLOR)
    text3 = myfont.render('Hard', False, LINE_COLOR)
    game_difficulty = 0
    while True:
        screen.fill(BACKGROUND)
        screen.blit(pygame.transform.scale(myimage, (400, 200)), (100, 10))
        buttons_draw()
        screen.blit(text1, (265, 280))
        screen.blit(text2, (250, 380))
        screen.blit(text3, (265, 480))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed(3)[0]:
                    pos = pygame.mouse.get_pos()
                    if 200 < pos[0] < 400 and 270 < pos[1] < 340:
                        game_difficulty = 1
                        return game_difficulty
                    if 200 < pos[0] < 400 and 370 < pos[1] < 440:
                        game_difficulty = 2
                        return game_difficulty
                    if 200 < pos[0] < 400 and 470 < pos[1] < 540:
                        game_difficulty = 3
                        return game_difficulty
        if game_difficulty is not 0:
            break
        else:
            pygame.display.flip()

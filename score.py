import pygame
import game

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
    pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(133, 390, 80, 70), 3)
    pygame.draw.rect(screen, LINE_COLOR, pygame.Rect(379, 390, 80, 70), 3)


def main_menu(scoreX, score0, winner):
    screen.fill(BACKGROUND)
    winner_txt1 = myfont.render('You won!', False, LINE_COLOR)
    winner_txt2 = myfont.render('Computer won!', False, LINE_COLOR)
    winner_txt3 = myfont.render('Nobody won!', False, LINE_COLOR)
    text1 = myfont.render('You: ', False, LINE_COLOR)
    text2 = myfont.render(str(scoreX), False, LINE_COLOR)
    text3 = myfont.render('Computer:', False, LINE_COLOR)
    text4 = myfont.render(str(score0), False, LINE_COLOR)
    text5 = myfont.render('Play again?', False, LINE_COLOR)
    text6 = myfont.render('Yes', False, LINE_COLOR)
    text7 = myfont.render('No', False, LINE_COLOR)
    while True:
        screen.fill(BACKGROUND)
        buttons_draw()
        if winner == 'X':
            screen.blit(winner_txt1, (220, 40))
        elif winner == '0':
            screen.blit(winner_txt2, (220, 40))
        else:
            screen.blit(winner_txt3, (220, 40))
        screen.blit(text1, (175, 100))
        screen.blit(text2, (250, 100))
        screen.blit(text3, (175, 150))
        screen.blit(text4, (325, 150))
        screen.blit(text5, (225, 280))
        screen.blit(text6, (150, 400))
        screen.blit(text7, (400, 400))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    if 133 < pos[0] < 213 and 390 < pos[1] < 460:
                        return 1
                    if 379 < pos[0] < 459 and 390 < pos[1] < 460:
                        return 2

        pygame.display.flip()

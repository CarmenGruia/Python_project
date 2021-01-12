import pygame

pygame.init()

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


def lines_draw():
    # first horizontal line
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    # second horizontal line
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    # first vertical line
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    # second vertical line
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)


def figures_draw(cy, cx, figure):
    centerx = cx * 200 + 100
    centery = cy * 200 + 100
    if figure == '0':
        pygame.draw.ellipse(screen, LINE_COLOR, (centerx-40, centery-50, 80, 100), FIGURE_WIDTH)
    else:
        pygame.draw.line(screen, LINE_COLOR, (centerx, centery), (centerx + 30, centery + 50), FIGURE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (centerx, centery), (centerx - 30, centery - 50), FIGURE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (centerx, centery), (centerx + 30, centery - 50), FIGURE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (centerx, centery), (centerx - 30, centery + 50), FIGURE_WIDTH)


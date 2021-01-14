import random
import sys
import pygame
import game_graphic
import menu
import score


class Game:
    def __init__(self):
        self.initialize_game()
        self.scoreX = 0
        self.score0 = 0
        self.winner = '*'

    def initialize_game(self):
        self.current_board = [['*', '*', '*'],
                              ['*', '*', '*'],
                              ['*', '*', '*']]

        # Player X always plays first
        self.player_turn = 'X'
        game_graphic.screen.fill(game_graphic.BACKGROUND)
        game_graphic.lines_draw()

    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}'.format(self.current_board[i][j]), end=" ")
            print()
        print()

    def is_valid(self, cx, cy):
        # The coordinates need to be between 0 and 2
        if cx < 0 or cx > 2 or cy < 0 or cy > 2:
            return False
        # There has to be an empty place
        elif self.current_board[cx][cy] != '*':
            return False
        else:
            return True

    def is_end(self):
        # Vertical win
        for i in range(0, 3):
            if (self.current_board[0][i] != '*' and
                    self.current_board[0][i] == self.current_board[1][i] and
                    self.current_board[1][i] == self.current_board[2][i]):
                return self.current_board[0][i]

        # Horizontal win
        for i in range(0, 3):
            if self.current_board[i] == ['X', 'X', 'X']:
                return 'X'
            elif self.current_board[i] == ['O', 'O', 'O']:
                return 'O'

        # Main diagonal win
        if (self.current_board[0][0] != '*' and
                self.current_board[0][0] == self.current_board[1][1] and
                self.current_board[0][0] == self.current_board[2][2]):
            return self.current_board[0][0]

        # Second diagonal win
        if (self.current_board[0][2] != '*' and
                self.current_board[0][2] == self.current_board[1][1] and
                self.current_board[0][2] == self.current_board[2][0]):
            return self.current_board[0][2]

        # Full board?
        for i in range(0, 3):
            for j in range(0, 3):
                # If there's an empty field, then no
                if self.current_board[i][j] == '*':
                    return None

        # It's a tie!
        return '*'

    def random_move(self):
        cx = 3
        cy = 3
        # Choose random, but valid move
        while not self.is_valid(cx, cy):
            cx = random.randrange(0, 3)
            cy = random.randrange(0, 3)
        self.current_board[cx][cy] = 'O'
        self.player_turn = 'X'
        return cx, cy

    def max(self):
        maxv = -2
        cx = None
        cy = None
        result = self.is_end()

        if result == 'X':
            return -1, 0, 0
        elif result == 'O':
            return 1, 0, 0
        elif result == '*':
            return 0, 0, 0

        for i in range(0, 3):
            for j in range(0, 3):
                # On the empty field player 'O' makes a move and calls Min
                if self.current_board[i][j] == '*':
                    self.current_board[i][j] = 'O'
                    (m, min_i, min_j) = self.min()
                    # Fixing the maxv value if needed
                    if m > maxv:
                        maxv = m
                        cx = i
                        cy = j
                    # Setting back the field to empty
                    self.current_board[i][j] = '*'
        return maxv, cx, cy

    def min(self):
        minv = 2
        cx = None
        cy = None

        result = self.is_end()

        if result == 'X':
            return -1, 0, 0
        elif result == 'O':
            return 1, 0, 0
        elif result == '*':
            return 0, 0, 0

        for i in range(0, 3):
            for j in range(0, 3):
                # On the empty field player 'O' makes a move and calls Max
                if self.current_board[i][j] == '*':
                    self.current_board[i][j] = 'X'
                    (m, max_i, max_j) = self.max()
                    # Fixing the minv value if needed
                    if m < minv:
                        minv = m
                        cx = i
                        cy = j
                    # Setting back the field to empty
                    self.current_board[i][j] = '*'

        return minv, cx, cy

    def smart_move(self):
        (m, cx, cy) = self.max()
        self.current_board[cx][cy] = 'O'
        self.player_turn = 'X'
        return cx, cy

    def play(self, game_difficulty):
        # Count the steps to know which strategy to use in case of medium difficulty
        step = 1
        while True:
            # If ok is 1, then the game continues
            ok = 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        # If pause is 0 then after X moves, 0 moves
                        pause = 0
                        # X's move
                        pos = pygame.mouse.get_pos()
                        # X's coordinates
                        cy = pos[0] // 200
                        cx = pos[1] // 200
                        if self.is_valid(cx, cy):
                            self.current_board[cx][cy] = 'X'
                            self.player_turn = 'O'
                            game_graphic.figures_draw(cx, cy, 'X')
                            if self.is_end() == '*' or self.is_end() == 'X':
                                # The X move was the last, now the board is full, so 0 doesn't move
                                pause = 1
                        else:
                            print('The move is not valid! Try again.')
                            # The X move wasn't valid, so 0 doesn't move yet
                            pause = 1
                        # 0's move
                        if pause == 0:
                            # If the game difficulty is easy, 0 moves randomly
                            if game_difficulty == 1:
                                (cx, cy) = self.random_move()
                                game_graphic.figures_draw(cx, cy, '0')
                            # If the game difficulty is medium, 0 moves moves once randomly, once smartly
                            elif game_difficulty == 2:
                                print(step)
                                if step % 2 == 1:
                                    (cx, cy) = self.random_move()
                                else:
                                    (cx, cy) = self.smart_move()
                                game_graphic.figures_draw(cx, cy, '0')
                            # If the game difficulty is hard, 0 moves smartly
                            elif game_difficulty == 3:
                                (cx, cy) = self.smart_move()
                                game_graphic.figures_draw(cx, cy, '0')
                        self.draw_board()
                        step = step + 1
                self.result = self.is_end()
                pygame.display.flip()
                # If the game is over
                if self.result is not None:
                    if self.result == 'X':
                        print('The winner is X!')
                        self.scoreX = self.scoreX + 1
                        self.winner = 'X'
                    elif self.result == 'O':
                        print('The winner is O!')
                        self.score0 = self.score0 + 1
                        self.winner = '0'
                    elif self.result == '*':
                        print("It's a tie!")
                        self.winner = '*'
                    ok = 0
            # To see the last move before showing the result
            if ok == 0:
                pygame.time.delay(600)
                break


def main():
    g = Game()
    game_difficulty = menu.main_menu()
    game_graphic.screen.fill(game_graphic.BACKGROUND)
    game_graphic.lines_draw()
    #!!modification
    g.play(3)

    while True:
        scoreX = g.scoreX
        score0 = g.score0
        winner = g.winner
        if score.main_menu(scoreX, score0, winner) == 2:
            main()
        else:
            g.initialize_game()
            game_graphic.screen.fill(game_graphic.BACKGROUND)
            game_graphic.lines_draw()
            # !!modification
            g.play(3)


if __name__ == "__main__":
    main()

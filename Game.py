import pygame, sys, random, time
from playsound import playsound

pygame.init()

# start set sizes
windowsSize = (900, 600)
board_x, board_y = 1, 1
ball_x, ball_y = random.randrange(0, 900), random.randrange(0, 80)
directionBall_X, directionBall_Y = 1, 1
damageNum = 3
score = 0
# end set sizes

# start board icon
board = pygame.image.load('board.jpg')
boardSize = board.get_size()
# end board icon

# start ball icon
ball = pygame.image.load('ball.jpg')
ballSize = ball.get_size()
# end ball icon

calibri = pygame.font.SysFont('Calibri', 21)
Damage = calibri.render("health : ", 1, (225, 0, 0), (0, 0, 0))

gameOverCalibri = pygame.font.SysFont('Calibri', 90)
writeGO = gameOverCalibri.render("Game Over :(", 1, (255, 0, 0), (0, 0, 0))

screen = pygame.display.set_mode(windowsSize)

# for hidden mouse
pygame.mouse.set_visible(0)

# start get time
clock = pygame.time.Clock()
# start get time

# start say Game Over and restart game
def GameOver():
    playsound('GameOver.mp3')
    time.sleep(2)
    Game_Loop(board_x, board_y, ball_x, ball_y, directionBall_X, directionBall_Y, damageNum, score)
# end say Game Over and restart game

# start start Game Loop
def Game_Loop(board_x, board_y, ball_x, ball_y, directionBall_X, directionBall_Y, damageNum, score):
    while True:

        # start set speed
        randTimeSecond = random.randrange(50, 350)
        clock.tick(randTimeSecond)
        # end set speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # start style
        screen.fill((0, 0, 0))
        # end style

        # start get mouse position
        mousePosition = pygame.mouse.get_pos()

        # start set mouse position
        board_x, board_y = mousePosition
        board_y = 560
        # end set mouse position

        # start board if
        if board_x + boardSize[0] > 900:
            board_x = 900 - boardSize[0]
        # end board if

        # start ball mover
        #X_mover = random.randint(4, 8)
        #Y_mover = random.randint(4, 7)
        ball_x += 6 * directionBall_X
        ball_y += 6 * directionBall_Y
        # end ball mover

        # start ball if
        if ball_x + ballSize[0] > 900 or ball_x <= 0:
            directionBall_X *= -1
        if ball_y + ballSize[1] > 600 or ball_y <= 0:
            directionBall_Y *= -1
        # end ball if

        # start gameOver if
        if ball_y + ballSize[1] > 600:
            if damageNum == 1:
                GameOver()
            else:
                damageNum -= 1
        # end gameOver if

        # start Computing damage
        if damageNum == 3:
            health = calibri.render("3", 1, (225, 0, 0), (0, 0, 0))
        if damageNum == 2:
            health = calibri.render("2", 1, (225, 0, 0), (0, 0, 0))
        if damageNum == 1:
            health = calibri.render("1", 1, (225, 0, 0), (0, 0, 0))
        # end Computing damage

        # start Reaction and calculate ball and board
        if ball_y + ball_x > board_y + board_x:
            directionBall_Y *= -1
            score += 0.2
            print(score)

            # if score >= 100:
            #     screen.fill((70, 70, 70))
        # end Reaction and calculate ball and board

        # start set ball, board and damage on windows
        if damageNum == 0:
            screen.blit(writeGO, (220, 250))
        screen.blit(Damage, (1, 1))
        screen.blit(health, (70, 1))
        screen.blit(board, (board_x, board_y))
        screen.blit(ball, (ball_x, ball_y))
        # end set ball and board on windows

        # start window updater
        pygame.display.update()
# start start Game Loop

Game_Loop(board_x, board_y, ball_x, ball_y, directionBall_X, directionBall_Y, damageNum, score)
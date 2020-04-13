import pygame

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

FPS = (input("\n\n______________________________________\n40 or below for  Beginners\n____________________________________________\n50 to 65 for  Intermediate\n__________________________________________\n70+ for Adavanced\n______________________________________________\nEnter your Speed value: -   "))
if ('35'<FPS<'80'):
    FPS = int(FPS)
else:
    FPS = int(60)
pygame.init()


size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dinoy Ka Pong Game")


rect_x = 400
rect_y = 580


rect_change_x = 0
rect_change_y = 0


ball_x = 50
ball_y = 50


ball_change_x = 5
ball_change_y = 5

score = 0
def level():
    if(50>FPS>35):
        level = "Beginner Level"
    elif(FPS<66):
        level = "Intermediate Level"
    else:
        level = "Advanced Level"
    return level

def drawrect( screen , x , y):
    if x <= 0:
        x = 0
    if x >= 699:
        x = 699
    pygame.draw.rect(screen, red, [x, y, 100, 20])

done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type== pygame.KEYDOWN:
            if event.key== pygame.K_LEFT:
                rect_change_x= -6
            elif event.key== pygame.K_RIGHT:
                rect_change_x= 6
        elif event.type== pygame.KEYUP:
            if event.key== pygame.K_LEFT or event.key== pygame.K_RIGHT:
                rect_change_x= 0

    screen.fill(black)
    rect_x += rect_change_x
    rect_y += rect_change_y

    ball_x += ball_change_x
    ball_y += ball_change_y

    if ball_x < 0:
        ball_x = 0
        ball_change_x = ball_change_x * -1
    elif ball_x > 785:
        ball_x = 785
        ball_change_x = ball_change_x * -1
    elif ball_y < 0:
        ball_y = 0
        ball_change_y = ball_change_y * -1
    elif ball_x> rect_x and ball_x< rect_x+100 and ball_y== 565:
        ball_change_y = ball_change_y * -1
        score = score + 1
    elif ball_y > 600:
        ball_change_y = ball_change_y * -1
        score = 0
    pygame.draw.rect(screen, white, [ball_x, ball_y, 15, 15])

    drawrect(screen, rect_x, rect_y)

    font = pygame.font.SysFont(('calibri'), 15, False, False)
    text = font.render(level()+": Score= " + str(score), True, white)
    screen.blit(text, [600, 100])

    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()

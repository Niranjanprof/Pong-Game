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

#the movement of ball
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

#redraw the rectangle
    drawrect(screen, rect_x, rect_y)

#score board
    font = pygame.font.SysFont(('calibri'), 15, False, False)
    text = font.render("Score= " + str(score), True, white)
    screen.blit(text, [600, 100])


    pygame.display.flip()
    clock.tick(60)
pygame.quit()

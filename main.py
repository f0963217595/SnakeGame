import pygame
import apple #引入apple.py
import snake #引入snake.py
#宣告想使用的顏色
white = (255,255,255)

#初始化apple.py裡面的Apple類別
#宣告一個變數app_obj，是Apple類別的初始化
app_obj = apple.Apple()

#初始化snake.py裡面的Snake類別
#宣告一個變數snake_obj，是Snake類別的初始化
snake_obj = snake.Snake()

pygame.init()
screen = pygame.display.set_mode((800,600))
screen.fill(white)
pygame.display.set_caption("貪食蛇遊戲")
pygame.display.update()

gameRun = True
gameOver = False
clock = pygame.time.Clock()

while gameRun:
    clock.tick(10)
    for event in pygame.event.get():
        #事件捕捉
        if event.type == pygame.QUIT:
            gameRun = False
        if event.type == pygame.KEYDOWN:#按下按鈕
            if event.key == pygame.K_UP:#上
                if snake_obj.dir != "下":
                    snake_obj.dir = "上"
            elif event.key == pygame.K_DOWN:#下
                if snake_obj.dir != "上":
                    snake_obj.dir = "下"
            elif event.key == pygame.K_RIGHT:#右
                if snake_obj.dir != "左":
                    snake_obj.dir = "右"
            elif event.key == pygame.K_LEFT:#左
                if snake_obj.dir != "右":
                    snake_obj.dir = "左"
    screen.fill(white)
    app_obj.createApple()
    snake_obj.move(app_obj) #蛇移動的程式碼
    
    result = snake_obj.checkGameOver()
    if result == True:#GameOver後的行為
        gameOver = True
        #snake_obj = snake.Snake()

    #Game Over的畫面    
    while gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = False
                gameRun = False
            if event.type == pygame.KEYDOWN:
                #按下ESC鍵
                if event.key == pygame.K_ESCAPE:
                    gameOver = False
                    snake_obj = snake.Snake()
        screen.fill((255,0,0))
        pygame.display.update()
                    
    pygame.draw.rect(screen,
                     (255,0,0),
                     [app_obj.x, app_obj.y,10,10],
                     0)
    for body in snake_obj.body:
        pygame.draw.rect(screen,
                         (0,0,255),
                         [body[0], body[1],10,10],
                         0)
    
    pygame.display.update()
pygame.quit()

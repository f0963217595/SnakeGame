import pygame
import apple #引入apple.py
#宣告想使用的顏色
white = (255,255,255)

#初始化apple.py裡面的Apple類別
#宣告一個變數app_obj，是Apple類別的初始化
app_obj = apple.Apple()

pygame.init()
screen = pygame.display.set_mode((800,600))
screen.fill(white)
pygame.display.set_caption("貪食蛇遊戲")
pygame.display.update()

gameRun = True
clock = pygame.time.Clock()

while gameRun:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRun = False
    screen.fill(white)
    app_obj.createApple()
    
    app_obj.changeStatus(False)
    
    pygame.draw.rect(screen,
                     (255,0,0),
                     [app_obj.x, app_obj.y,10,10],
                     0)
    pygame.display.update()
pygame.quit()

from data import *
from maze_funcion import *
from random import randint

window = pygame.display.set_mode((setting_win["WIDTH"], setting_win["HEIGHT"]))
pygame.display.set_caption("MAZE")

def run():
    game = True

    hero = Hero(10,10, 70, 106, image= hero_list)
    bot1 = Bot(190, 10, 50, 50, image= bot1_list, vertical=True)
    bot2 = Bot(900, 570, 80, 100, image= bot2_list)
    clock = pygame.time.Clock()


    while game:
        window.fill((228, 172, 255))
        #x,y = 20, 20
        #for i in range(50):
        #    pygame.draw.line(window, (255,255,255), (0, y), (setting_win["WIDTH"], y))
        #    pygame.draw.line(window, (255,255,255), (x, 0), (x, setting_win["HEIGHT"]))
        #    x += 20
        #    y += 20
        
        for wall in wall_list:
            pygame.draw.rect(window, (255,255,255), wall)

        hero.move(window)

        bot1.move(window)

        bot2.shoot(window, hero)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    hero.MOVE["UP"] = True
                if event.key == pygame.K_s:
                    hero.MOVE["DOWN"] = True
                if event.key == pygame.K_a:
                    hero.MOVE["LEFT"] = True
                if event.key == pygame.K_d:
                    hero.MOVE["RIGHT"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    hero.MOVE["UP"] = False
                if event.key == pygame.K_s:
                    hero.MOVE["DOWN"] = False
                if event.key == pygame.K_a:
                    hero.MOVE["LEFT"] = False
                if event.key == pygame.K_d:
                    hero.MOVE["RIGHT"] = False

        clock.tick(60)
        pygame.display.flip()

run()
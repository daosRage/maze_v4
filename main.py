from data import *
from maze_funcion import *
from random import randint

window = pygame.display.set_mode((setting_win["WIDTH"], setting_win["HEIGHT"]))
pygame.display.set_caption("MAZE")

def run():
    game = True
    door = False
    lvl = 1
    menu = False

    hero = Hero(10,10, 70, 106, image= hero_list)
    bot1 = Bot(190, 10, 50, 50, image= bot1_list, vertical=True)
    bot2 = Bot(900, 570, 80, 100, image= bot2_list)
    clock = pygame.time.Clock()
    start_rect = pygame.Rect(setting_win["WIDTH"] // 2 - 270, setting_win["HEIGHT"] // 2, 250, 65)
    end_rect = pygame.Rect(setting_win["WIDTH"] // 2 + 20, setting_win["HEIGHT"] // 2, 250, 65)
    font_start_end = pygame.font.Font(None, 50)


    while game:
        events = pygame.event.get()
        window.fill((228, 172, 255))

        x = 920
        for i in range(hero.HP):
            window.blit(hp_image, (x, 10))
            x += 25
        if hero.HP == 0:
            menu = True
            hero.SPEED = 0
        #x,y = 20, 20
        #for i in range(50):
        #    pygame.draw.line(window, (255,255,255), (0, y), (setting_win["WIDTH"], y))
        #    pygame.draw.line(window, (255,255,255), (x, 0), (x, setting_win["HEIGHT"]))
        #    x += 20
        #    y += 20
        
        for wall in wall_list:
            pygame.draw.rect(window, (255,255,255), wall)

        hero.move(window)

        bot1.move(window, hero)

        bot2.shoot(window, hero)


        if not door:
            window.blit(key_image, (520, 40))
            if key_image.get_rect(topleft=(520, 40)).colliderect(hero):
                door = True
        else:
            window.blit(door_image, (850, 300))
            if door_image.get_rect(topleft=(850, 300)).colliderect(hero):
                lvl += 1
        


        for event in events:
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

        if menu:
            pygame.draw.rect(window, (191, 248, 151), start_rect)
            pygame.draw.rect(window, (191, 248, 151), end_rect)
            window.blit(font_start_end.render("START", True, (0,0,0)), (start_rect.x + 60, start_rect.y + 15))
            window.blit(font_start_end.render("END", True, (0,0,0)), (end_rect.x + 85, end_rect.y + 15))
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x,y = event.pos
                    if start_rect.collidepoint(x, y):
                        pass
                    if end_rect.collidepoint(x, y):
                        game = False



        clock.tick(60)
        pygame.display.flip()

run()
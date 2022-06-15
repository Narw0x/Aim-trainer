import pygame
import random
from math import *

pygame.init()

width = 1000
height = 1000

pygame.display.set_caption('Aim Trainer')
okno = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()
fps = 60

cervena_50 = pygame.image.load("./cervena-50.png")

modra_50 = pygame.image.load("./modra-50.png")

biela = "#FFFFFF"
cierna_farba = "#000000"

font_32 = pygame.font.Font('freesansbold.ttf', 32)
font_64 = pygame.font.Font('freesansbold.ttf', 64)
font_128 = pygame.font.Font('freesansbold.ttf', 128)

score = 0
kliky = 0

cas = 30
sekunda = 0

random_x = random.randint(100, width-100)
random_y = random.randint(100, height-100)

staticky = False
dynamicky = False

class Terc():
    def __init__(self, img, x, y):
        self.img = img
        self.rect = img.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self,okno):
        okno.blit(self.img, self.rect)

class Terc_dynamicky(Terc):
    def __init__(self, img, x, y):
        super().__init__(img, x, y)
        self.speed = random.randint(1, 150)

    def move(self):
        self.speed = random.randint(1, 150)
        self.rect.x -= self.speed
        self.speed = random.randint(1, 150)
        self.rect.y -= self.speed

    def moveTo(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def check_if_clicked(self, pos):
        pos = pygame.mouse.get_pos()
        if pos[0] in range(self.rect.x, self.rect.x + self.img.get_width()) and pos[1] in range(self.rect.y, self.rect.y + self.img.get_height()):
            return True
        else:
            return False

class Terc_staticky(Terc):
    def __init__(self, img, x, y):
        super().__init__(img, x, y)
        
    def moveTo(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def check_if_clicked(self, pos):
        pos = pygame.mouse.get_pos()
        if pos[0] in range(self.rect.x, self.rect.x + self.img.get_width()) and pos[1] in range(self.rect.y, self.rect.y + self.img.get_height()):
            return True
        else:
            return False

def main(staticky, dynamicky, kliky):
    global random_x, random_y,sekunda, cas, score
    while True:
        pos = pygame.mouse.get_pos()
        okno.fill(biela)
        clock.tick(fps)
        sekunda += 1

        if staticky:
            terc_1 = Terc_staticky(cervena_50, random_x, random_y)
            terc_1.draw(okno)

            if sekunda % 60 == 0:
                cas -= 1
                    
            if cas <= 0:
                end(kliky)

            score_text =  font_32.render("score: " + str(score), True, cierna_farba)
            score_rect = score_text.get_rect()
            score_rect.center = (90, 950)

            okno.blit(score_text, score_rect)

            cas_text =  font_32.render("cas: " + str(cas), True, cierna_farba)
            cas_rect = cas_text.get_rect()
            cas_rect.center = (250, 950)

            okno.blit(cas_text, cas_rect)

            pygame.display.update()

        
        if dynamicky:
            terc_2 = Terc_dynamicky(modra_50, random_x, random_y)
        
            if sekunda % 10 == 0:
                
                terc_2.move()
                terc_2.draw(okno)

                score_text =  font_32.render("score: " + str(score), True, cierna_farba)
                score_rect = score_text.get_rect()
                score_rect.center = (90, 950)

                okno.blit(score_text, score_rect)

                cas_text =  font_32.render("čas: " + str(cas), True, cierna_farba)
                cas_rect = cas_text.get_rect()
                cas_rect.center = (250, 950)

                okno.blit(cas_text, cas_rect)

                pygame.display.update()

                if sekunda % 60 == 0:
                    cas -= 1
                    
                if cas <= 0:
                    end(kliky)

                if terc_2.check_if_clicked(pos):
                    score += 1
                    random_x = random.randint(200, width-200)
                    random_y = random.randint(200, height-200)
                    terc_2.moveTo(random_x, random_y)
                    terc_2.draw(okno)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                kliky += 1


                if staticky:
                    if terc_1.check_if_clicked(pos):
                        score += 1
                        random_x = random.randint(100, width-100)
                        random_y = random.randint(100, height-100)
                        terc_1.moveTo(random_x, random_y)
                        terc_1.draw(okno)
                        pygame.display.update()
                
def main_menu():
    while True:
        okno.fill(biela)
        clock.tick(fps)

        menu =  font_128.render("Aim Trainer", True, cierna_farba)
        menu_rect = menu.get_rect()
        menu_rect.center = (width/2, height/2 - 200)

        text =  font_32.render("Stlac 'ENTER' pre start", True, cierna_farba)
        text_rect = menu.get_rect()
        text_rect.center = (width/2 + 185, height/2 + 100 )

        konec =  font_32.render("Stlac 'ESC' pre vypnutie", True, cierna_farba)
        konec_rect = konec.get_rect()
        konec_rect.center = (width/2  , height/2 + 100)

        okno.blit(menu, menu_rect)
        okno.blit(text, text_rect)
        okno.blit(konec, konec_rect)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_RETURN:
                    vyber_hry()
                
def vyber_hry():
    global cas, score
    while True:
        okno.fill(biela)
        clock.tick(fps)

        menu =  font_128.render("Vyber hru", True, cierna_farba)
        menu_rect = menu.get_rect()
        menu_rect.center = (width/2, height/2 - 200)

        text =  font_32.render("Stlac 'E' pre easy hru", True, cierna_farba)
        text_rect = menu.get_rect()
        text_rect.center = (width/2 - 100 , height/2 + 40)

        text2 =  font_32.render("Stlac 'H' pre hard hru", True, cierna_farba)
        text2_rect = menu.get_rect()
        text2_rect.center = (width/2 + 350 , height/2 + 40)

        okno.blit(menu, menu_rect)
        okno.blit(text, text_rect)
        okno.blit(text2, text2_rect)
       
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_e:
                    staticky = True
                    dynamicky = False
                    score = 0
                    cas = 30
                    kliky = 0
                    main(staticky , dynamicky, kliky)
                if event.key == pygame.K_h:
                    dynamicky = True
                    staticky = False
                    score = 0
                    cas = 30
                    kliky = 0
                    main(staticky, dynamicky, kliky)

def end(kliky):
    
    while True:
        okno.fill(biela)
        clock.tick(fps)

        menu =  font_64.render("Tvoje score je :  " + str(score), True, cierna_farba)
        menu_rect = menu.get_rect()
        menu_rect.center = (width/2, 300)

        klik = font_32.render("Klikol si : " + str(kliky) + (" krat"), True, cierna_farba)
        klik_rect = klik.get_rect()
        klik_rect.center = (width/2, 400)

        precenta = font_32.render("Uspešnosť : " + str(round(score/kliky*100, 2)) + (" %"), True, cierna_farba)
        precenta_rect = precenta.get_rect()
        precenta_rect.center = (width/2, 440)

        text =  font_32.render("Stlac 'ENTER' pre pokracovanie", True, cierna_farba)
        text_rect = text.get_rect()
        text_rect.center = (width/2  , height/2 + 40)

        konec =  font_32.render("Stlac 'ESC' pre vypnutie", True, cierna_farba)
        konec_rect = konec.get_rect()
        konec_rect.center = (width/2  , height/2 + 80)


        okno.blit(menu, menu_rect)
        okno.blit(text, text_rect)
        okno.blit(konec, konec_rect)
        okno.blit(klik, klik_rect)
        okno.blit(precenta, precenta_rect)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_RETURN:
                    vyber_hry()
                 
if __name__ == '__main__':
    main_menu()
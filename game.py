import pygame
import os
import sys


def magaz():
    Magaz()
    global knopki_list
    knopki_list += [Knopka(1560, 65, 'mass')]
    knopki_list += [Knopka(1560, 260, 'luchnik')]
    knopki_list += [Knopka(1560, 455, 'zam')]
    knopki_list += [Knopka(1560, 650, 'dal')]
    knopki_list += [Knopka(1560, 845, 'sila')]
    MassImage(1780, 90)
    LuchnikImage(1780, 285)
    ZamImage(1780, 480)
    DalImage(1780, 675)
    SilaImage(1780, 870)




def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


def generate_level(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                level[y][x] = None
            elif level[y][x] == '#':
                level[y][x] = Stena(x, y)
            elif level[y][x] == '-':
                level[y][x] = Doroga(x, y)
    return level


def load_level(filename, number):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    lines = level_map.index('lv' + str(number))
    level_map = level_map[lines + 1: lines + 12]
    for i in range(len(level_map)):
        level_map[i] = list(level_map[i])
    return level_map


class Magaz(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(magaz_sprites, all_sprites)
        self.image = image_list['magaz']
        self.rect = self.image.get_rect().move(1540, 0)
        self.x = 1540
        self.y = 0


class Knopka(pygame.sprite.Sprite):
    def __init__(self, x, y, name):
        super().__init__(magaz_sprites, all_sprites, knopki_sprites)
        self.image = image_list['knopka'][0]
        self.rect = self.image.get_rect().move(x, y)
        self.x = x
        self.y = y
        self.name = name
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.image = image_list['knopka'][0]
        self.rect = self.image.get_rect().move(self.x, self.y)

    def new(self):
        self.image = image_list['knopka'][1]
        self.rect = self.image.get_rect().move(self.x, self.y)
        return self.name


class LuchnikImage(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(magaz_sprites, all_sprites)
        self.image = image_list['luchnik'][0]
        self.rect = self.image.get_rect().move(x, y)
        self.x = x
        self.y = y


class MassImage(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(magaz_sprites, all_sprites)
        self.image = image_list['mass'][0]
        self.rect = self.image.get_rect().move(x, y)
        self.x = x
        self.y = y


class SilaImage(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(magaz_sprites, all_sprites)
        self.image = image_list['sila'][0]
        self.rect = self.image.get_rect().move(x, y)
        self.x = x
        self.y = y


class DalImage(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(magaz_sprites, all_sprites)
        self.image = image_list['dal'][0]
        self.rect = self.image.get_rect().move(x, y)
        self.x = x
        self.y = y


class ZamImage(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(magaz_sprites, all_sprites)
        self.image = image_list['zam'][0]
        self.rect = self.image.get_rect().move(x, y)
        self.x = x
        self.y = y


class Luchnik(pygame.sprite.Sprite):
    def __init__(self, x, y):
        global coin
        super().__init__(tower_sprites, all_sprites)
        self.coin = [60, 80, 120]
        self.sales = [30, 70, 130]
        coin -= 60
        self.lv = 1
        self.image = image_list['luchnik'][0]
        self.rect = self.image.get_rect().move(tile * x + sd_x, tile * y + sd_y)
        self.x = x
        self.y = y
        self.rad = Rad(x, y, int(1.5 * tile))

    def info(self):
        global inform
        self.rad.new()
        Info('sale', self.x, self.y, self.lv)
        Info('buy', self.x, self.y, self.lv)
        Info('info', self.x, self.y, self.lv)
        inform = True

    def lvup(self):
        global coin
        if coin >= self.coin[self.lv]:
            self.lv += 1
            coin -= self.coin[self.lv - 1]
            self.image = image_list['luchnik'][self.lv - 1]
            self.rect = self.image.get_rect().move(tile * self.x + sd_x, tile * self.y + sd_y)

    def sale(self):
        global coin
        coin += self.sales[self.lv - 1]
        level[self.y][self.x] = None
        self.kill()

class Mass(pygame.sprite.Sprite):
    def __init__(self, x, y):
        global coin
        super().__init__(tower_sprites, all_sprites)
        self.coin = [60, 80, 120]
        self.sales = [30, 70, 130]
        self.lv = 1
        coin -= 60
        self.image = image_list['mass'][0]
        self.rect = self.image.get_rect().move(tile * x + sd_x, tile * y + sd_y)
        self.x = x
        self.y = y
        self.rad = Rad(x, y, int(1.5 * tile))

    def info(self):
        global inform
        self.rad.new()
        Info('sale', self.x, self.y, self.lv)
        Info('buy', self.x, self.y, self.lv)
        Info('info', self.x, self.y, self.lv)
        inform = True

    def lvup(self):
        global coin
        if coin >= self.coin[self.lv]:
            self.lv += 1
            coin -= self.coin[self.lv - 1]
            self.image = image_list['mass'][self.lv - 1]
            self.rect = self.image.get_rect().move(tile * self.x + sd_x, tile * self.y + sd_y)

    def sale(self):
        global coin
        coin += self.sales[self.lv - 1]
        level[self.y][self.x] = None
        self.kill()



class Sila(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.lv = 1
        global coin
        super().__init__(tower_sprites, all_sprites)
        self.coin = [250, 320, 400]
        self.sales = [120, 280, 480]
        coin -= 250
        self.image = image_list['sila'][0]
        self.rect = self.image.get_rect().move(tile * x + sd_x, tile * y + sd_y)
        self.x = x
        self.y = y
        self.rad = Rad(x, y, int(1.5 * tile))

    def info(self):
        global inform
        self.rad.new()
        Info('sale', self.x, self.y, self.lv)
        Info('buy', self.x, self.y, self.lv)
        Info('info', self.x, self.y, self.lv)
        inform = True

    def lvup(self):
        global coin
        if coin >= self.coin[self.lv]:
            self.lv += 1
            coin -= self.coin[self.lv - 1]
            self.image = image_list['sila'][self.lv - 1]
            self.rect = self.image.get_rect().move(tile * self.x + sd_x, tile * self.y + sd_y)

    def sale(self):
        global coin
        coin += self.sales[self.lv - 1]
        level[self.y][self.x] = None
        self.kill()


class Dal(pygame.sprite.Sprite):
    def __init__(self, x, y):
        global coin
        super().__init__(tower_sprites, all_sprites)
        self.coin = [180, 200, 250]
        self.sales = [90, 190, 310]
        self.lv = 1
        coin -= 180
        self.image = image_list['dal'][0]
        self.rect = self.image.get_rect().move(tile * x + sd_x, tile * y + sd_y)
        self.x = x
        self.y = y
        self.rad = Rad(x, y, int(1.5 * tile))

    def info(self):
        global inform
        self.rad.new()
        Info('sale', self.x, self.y, self.lv)
        Info('buy', self.x, self.y, self.lv)
        Info('info', self.x, self.y, self.lv)
        inform = True

    def lvup(self):
        global coin
        if coin >= self.coin[self.lv]:
            self.lv += 1
            coin -= self.coin[self.lv - 1]
            self.image = image_list['dal'][self.lv - 1]
            self.rect = self.image.get_rect().move(tile * self.x + sd_x, tile * self.y + sd_y)

    def sale(self):
        global coin
        coin += self.sales[self.lv - 1]
        level[self.y][self.x] = None
        self.kill()


class Zam(pygame.sprite.Sprite):
    def __init__(self, x, y):
        global coin
        super().__init__(tower_sprites, all_sprites)
        self.coin = [90, 120, 150]
        self.sales = [40, 100, 180]
        coin -= 90
        self.lv = 1
        self.image = image_list['zam'][0]
        self.rect = self.image.get_rect().move(tile * x + sd_x, tile * y + sd_y)
        self.x = x
        self.y = y
        self.rad = Rad(x, y, int(1.5 * tile))

    def info(self):
        global inform
        self.rad.new()
        Info('sale', self.x, self.y, self.lv)
        Info('buy', self.x, self.y, self.lv)
        Info('info', self.x, self.y, self.lv)
        inform = True

    def lvup(self):
        global coin
        if coin >= self.coin[self.lv]:
            self.lv += 1
            coin -= self.coin[self.lv - 1]
            self.image = image_list['zam'][self.lv - 1]
            self.rect = self.image.get_rect().move(tile * self.x + sd_x, tile * self.y + sd_y)

    def sale(self):
        global coin
        coin += self.sales[self.lv - 1]
        level[self.y][self.x] = None
        self.kill()


class Stena(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(okr_sprites, all_sprites)
        self.image = image_list['stena']
        self.rect = self.image.get_rect().move(tile * x + sd_x, tile * y + sd_y)
        self.x = x
        self.y = y

    def info(self):
        pass


class Doroga(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(okr_sprites, all_sprites)
        self.image = image_list['doroga']
        self.rect = self.image.get_rect().move(tile * x + sd_x, tile * y + sd_y)
        self.x = x
        self.y = y

    def info(self):
        pass


class Rad(pygame.sprite.Sprite):
    def __init__(self, x, y, rad):
        super().__init__(rad_sprites, all_sprites)
        self.x = x
        self.y = y
        self.rad = rad
        self.image = pygame.Surface((2 * rad, 2 * rad), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color(128, 128, 128, 0), (rad, rad), rad)
        self.rect = self.image.get_rect().move(int(tile * (x + 0.5)) - rad + sd_x, int(tile * (y + 0.5)) - rad + sd_y)

    def new(self):
        self.image = pygame.Surface((2 * self.rad, 2 * self.rad), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color(128, 128, 128, 20), (self.rad, self.rad), self.rad)
        self.rect = self.image.get_rect().move(int(tile * (self.x + 0.5)) - self.rad + sd_x,
                                               int(tile * (self.y + 0.5)) - self.rad + sd_y)

    def update(self):
        self.image = pygame.Surface((2 * self.rad, 2 * self.rad), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color(128, 128, 128, 0), (self.rad, self.rad), self.rad)
        self.rect = self.image.get_rect().move(int(tile * (self.x + 0.5)) - self.rad + sd_x,
                                               int(tile * (self.y + 0.5)) - self.rad + sd_y)



class Fon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(fon_sprites, all_sprites)
        self.image = load_image('fon.png')
        self.rect = self.image.get_rect().move(0, 0)


class Info(pygame.sprite.Sprite):
    def __init__(self, name, x, y, lv):
        super().__init__(info_sprites, all_sprites)
        self.lv = lv
        self.name = name
        self.x = x
        self.y = y
        if self.name == 'buy':
            self.image = image_list['buy']
            if y < 5:
                self.rect = self.image.get_rect().move(x * tile + sd_x - 30, y * tile + sd_y + 150)
            else:
                self.rect = self.image.get_rect().move(x * tile + sd_x - 30, y * tile + sd_y - 125)
        elif self.name == 'sale':
            self.image = image_list['sale']
            if y < 5:
                self.rect = self.image.get_rect().move(x * tile + sd_x + 55, y * tile + sd_y + 150)
            else:
                self.rect = self.image.get_rect().move(x * tile + sd_x + 55, y * tile + sd_y - 125)
        else:
            self.image = image_list['info']
            if y < 5:
                self.rect = self.image.get_rect().move(x * tile + sd_x - 100, y * tile + sd_y + 110)
            else:
                self.rect = self.image.get_rect().move(x * tile + sd_x - 100, y * tile + sd_y - 40)

    def update(self):
        if pygame.sprite.spritecollideany(self, mouse_sprites):
            if self.name == 'buy' and self.lv != 3:
                level[self.y][self.x].lvup()
            elif self.name == 'sale':
                level[self.y][self.x].sale()


class Mouse(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(mouse_sprites)
        self.x = x
        self.y = y
        self.image = pygame.Surface((1, 1), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color(128, 128, 128, 0), (1, 1), 1)
        self.rect = self.image.get_rect().move(x, y)


image_list = {'luchnik': [load_image('luchnik1.png'), load_image('luchnik2.png'), load_image('luchnik3.png')],
              'mass': [load_image('mass1.png'), load_image('mass2.png'), load_image('mass3.png')],
              'sila': [load_image('sila1.png'), load_image('sila2.png'), load_image('sila3.png')],
              'dal': [load_image('dal1.png'), load_image('dal2.png'), load_image('dal3.png')],
              'zam': [load_image('zam1.png'), load_image('zam2.png'), load_image('zam3.png')],
              'stena': load_image('stena.png'), 'doroga': load_image('doroga.png'), 'magaz': load_image('magaz.png'),
              'knopka': [load_image('knopka1.png'), load_image('knopka2.png')], 'buy': load_image('buy.png'),
              'sale': load_image('sale.png'), 'info': load_image('info.png')}


number = 1
inform = False
all_sprites = pygame.sprite.Group()
tower_sprites = pygame.sprite.Group()
okr_sprites = pygame.sprite.Group()
magaz_sprites = pygame.sprite.Group()
knopki_sprites = pygame.sprite.Group()
rad_sprites = pygame.sprite.Group()
fon_sprites = pygame.sprite.Group()
info_sprites = pygame.sprite.Group()
mouse_sprites = pygame.sprite.Group()
coin = 1000
knopki_list = []
tile = 100
sd_x = 20
sd_y = 20



if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Да')
    size = width, height = 500, 500
    screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
    fon = Fon()
    running = True
    clock = pygame.time.Clock()
    level = generate_level(load_level('levels.txt', number))
    magaz()
    t = 0
    font = pygame.font.Font(None, 30)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                rad_sprites.update()
                x, y = event.pos
                Mouse(x, y)
                if inform:
                    inform = False
                    info_sprites.update()
                    info_sprites = pygame.sprite.Group()
                elif x > 20 and x < 1520 and y > 20 and y < 1020:
                    x, y = (x - 20) // 100, (y - 20) // 100
                    if level[y][x] == None and t != 0:
                        if t == 'luchnik' and coin >= 60:
                            level[y][x] = Luchnik(x, y)
                        elif t == 'mass' and coin >= 60:
                            level[y][x] = Mass(x, y)
                        elif t == 'dal' and coin >= 180:
                            level[y][x] = Dal(x, y)
                        elif t == 'sila' and coin >= 250:
                            level[y][x] = Sila(x, y)
                        elif t == 'zam' and coin >= 90:
                            level[y][x] = Zam(x, y)
                    elif level[y][x] != None and t == 0:
                        level[y][x].info()
                elif x > 1560 and x < 1900 and y > 65 and y < 215:
                    knopki_sprites.update()
                    if t != 'mass':
                        t = knopki_list[0].new()
                    else:
                        t = 0
                elif x > 1560 and x < 1900 and y > 260 and y < 410:
                    knopki_sprites.update()
                    if t != 'luchnik':
                        t = knopki_list[1].new()
                    else:
                        t = 0
                elif x > 1560 and x < 1900 and y > 455 and y < 605:
                    knopki_sprites.update()
                    if t != 'zam':
                        t = knopki_list[2].new()
                    else:
                        t = 0
                elif x > 1560 and x < 1900 and y > 650 and y < 800:
                    knopki_sprites.update()
                    if t != 'dal':
                        t = knopki_list[3].new()
                    else:
                        t = 0
                elif x > 1560 and x < 1900 and y > 845 and y < 995:
                    knopki_sprites.update()
                    if t != 'sila':
                        t = knopki_list[4].new()
                    else:
                        t = 0
                mouse_sprites = pygame.sprite.Group()
        fon_sprites.draw(screen)
        tower_sprites.draw(screen)
        okr_sprites.draw(screen)
        rad_sprites.draw(screen)
        info_sprites.draw(screen)
        magaz_sprites.draw(screen)
        string_rendered = font.render(str(coin), 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        intro_rect.top = 20
        intro_rect.x = 1570
        screen.blit(string_rendered, intro_rect)
        pygame.display.flip()
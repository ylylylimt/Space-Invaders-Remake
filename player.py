import pygame

pygame.init()
pygame.font.init()

myfont = pygame.font.Font("Grand9K Pixel.ttf", 30)

winner_text = ""
x_red = 1000
x_green_bul = 0
y_red = 1000
y_green_bul = 0
x_green = 1000
x_red_bul = 0
y_green = 1000
y_red_bul = 0
check_red_bul = True

x_blue = 1000
y_blue = 1000
x_blue_bul = 0
y_blue_bul = 0
x_yellow = 1000
y_yellow = 1000
x_yellow_bul = 0
y_yellow_bul = 0


class Player():
    def __init__(self, x, y, width, height, color, health, x_health, y_health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.health = health
        self.x_health = x_health
        self.y_health = y_health
        self.health_red = 10
        self.health_green = 10
        self.health_blue = 10
        self.health_yellow = 10
        self.moving = False
        self.bullet = pygame.Rect(self.x + self.width + 10, self.y + self.height // 2 - 2, 10, 5)
        self.x_green = -1
        self.y_green = self.y
        self.x_red = -1
        self.y_red = self.y
        self.x_blue = -1
        self.y_blue = self.y
        self.x_yellow = -1
        self.y_yellow = self.y
        self.rect = (x, y, width, height)
        self.vel = 5
        self.x_redy = 0

    def draw1(self, win):
        self.draw_spaceship(win)
        self.update_h(win)

    def draw_spaceship(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.circle(win, self.color, (self.x + self.width // 2, self.y), self.width // 2)
        pygame.draw.rect(win, self.color,
                         (self.x - self.width // 4, self.y + self.height // 2, self.width // 2, self.height // 4))
        pygame.draw.rect(win, self.color, (
            self.x + self.width - self.width // 4, self.y + self.height // 2, self.width // 2, self.height // 4))
        pygame.draw.rect(win, self.color,
                         (self.x + self.width // 4, self.y + self.height, self.width // 2, self.height // 4))

    def move(self, win):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel
        if keys[pygame.K_RCTRL]:
            self.moving = True

        if self.x <= 50:
            self.x = 50
        if self.x >= 800:
            self.x = 800
        if self.y <= 50:
            self.y = 50
        if self.y >= 500:
            self.y = 500

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

    def update_h(self, win):
        if self.color == (221, 30, 38):
            health_text = myfont.render(
                "Lives: " + str(self.health_red), 1, (255, 255, 255))
            win.blit(health_text, (self.x_health, self.y_health))
        if self.color == (54, 168, 73):
            health_text = myfont.render(
                "Lives: " + str(self.health_green), 1, (255, 255, 255))
            win.blit(health_text, (self.x_health, self.y_health))
        if self.color == (0, 0, 255):
            health_text = myfont.render(
                "Lives: " + str(self.health_blue), 1, (255, 255, 255))
            win.blit(health_text, (self.x_health, self.y_health))
        if self.color == (255, 255, 0):
            health_text = myfont.render(
                "Lives: " + str(self.health_yellow), 1, (255, 255, 255))
            win.blit(health_text, (self.x_health, self.y_health))

    def bul(self, win):
        if self.color == (54, 168, 73):
            pygame.draw.rect(win, (54, 168, 73), self.bullet)
        elif self.color == (221, 30, 38):
            pygame.draw.rect(win, (221, 30, 38), self.bullet)
        elif self.color == (0, 0, 255):
            pygame.draw.rect(win, (0, 0, 255), self.bullet)
        elif self.color == (255, 255, 0):
            pygame.draw.rect(win, (255, 255, 0), self.bullet)

    def mov(self):
        global check_red_bul
        if self.moving == False:
            if self.color == (54, 168, 73):
                self.bullet.x = self.x + self.width
                self.bullet.y = self.y + self.height // 2 - 2
                check_red_bul = True
            elif self.color == (221, 30, 38):
                self.bullet.x = self.x - 10
                self.bullet.y = self.y + self.height // 2 - 2
                check_red_bul = True
            elif self.color == (0, 0, 255):
                self.bullet.x = self.x + self.width
                self.bullet.y = self.y + self.height // 2 - 2
                check_red_bul = True
            elif self.color == (255, 255, 0):
                self.bullet.x = self.x - 10
                self.bullet.y = self.y + self.height // 2 - 2
                check_red_bul = True
        if self.moving == True:
            if self.color == (54, 168, 73):
                self.bullet.x += 5
            elif self.color == (221, 30, 38):
                self.bullet.x -= 5
            elif self.color == (0, 0, 255):
                self.bullet.x += 5
            elif self.color == (255, 255, 0):
                self.bullet.x -= 5
        if self.color == (54, 168, 73):
            if self.bullet.x >= 900:
                self.moving = False
                self.bullet.x = self.x + self.width
                self.bullet.y = self.y + self.height // 2 - 2
        elif self.color == (221, 30, 38):
            if self.bullet.x <= 0:
                self.moving = False
                self.bullet.x = self.x + self.width
                self.bullet.y = self.y + self.height // 2 - 2
        elif self.color == (0, 0, 255):
            if self.bullet.x >= 900:
                self.moving = False
                self.bullet.x = self.x + self.width
                self.bullet.y = self.y + self.height // 2 - 2
        elif self.color == (255, 255, 0):
            if self.bullet.x <= 0:
                self.moving = False
                self.bullet.x = self.x + self.width
                self.bullet.y = self.y + self.height // 2 - 2

    def colour(self):
        global x_red
        global x_green_bul
        global y_red
        global y_green_bul
        global x_green
        global x_red_bul
        global y_green
        global y_red_bul
        global check_red_bul
        global x_blue
        global y_blue
        global x_blue_bul
        global y_blue_bul
        global x_yellow
        global y_yellow
        global x_yellow_bul
        global y_yellow_bul

        if self.color == (221, 30, 38):
            x_red = self.x
            y_red = self.y
        if self.color == (54, 168, 73):
            x_green = self.x
            y_green = self.y
        if self.color == (0, 0, 255):
            x_blue = self.x
            y_blue = self.y
        if self.color == (255, 255, 0):
            x_yellow = self.x
            y_yellow = self.y

        if self.color == (221, 30, 38):
            x_red_bul = self.bullet.x
            y_red_bul = self.bullet.y
        if self.color == (54, 168, 73):
            x_green_bul = self.bullet.x
            y_green_bul = self.bullet.y
        if self.color == (0, 0, 255):
            x_blue_bul = self.bullet.x
            y_blue_bul = self.bullet.y
        if self.color == (255, 255, 0):
            x_yellow_bul = self.bullet.x
            y_yellow_bul = self.bullet.y

        if x_red_bul <= x_green + 50 and x_red_bul >= x_green + 48 and y_red_bul >= y_green - 5 and y_red_bul <= y_green + 50:
            self.health_red -= 1
            self.bullet.x = self.x + self.width
            self.bullet.y = self.y + self.height // 2 - 2
            self.moving = False

        if x_green_bul >= x_red - 10 and x_green_bul <= x_red - 8 and y_green_bul >= y_red - 5 and y_green_bul <= y_red + 50:
            self.health_green -= 1
            self.bullet.x = self.x + self.width
            self.bullet.y = self.y + self.height // 2 - 2
            self.moving = False

        if x_blue_bul <= x_yellow + 50 and x_blue_bul >= x_yellow + 48 and y_blue_bul >= y_yellow - 5 and y_blue_bul <= y_yellow + 50:
            self.health_blue -= 1
            self.bullet.x = self.x + self.width
            self.bullet.y = self.y + self.height // 2 - 2
            self.moving = False

        if x_yellow_bul >= x_blue - 10 and x_yellow_bul <= x_blue - 8 and y_yellow_bul >= y_blue - 5 and y_yellow_bul <= y_blue + 50:
            self.health_yellow -= 1
            self.bullet.x = self.x + self.width
            self.bullet.y = self.y + self.height // 2 - 2
            self.moving = False

    def is_winner(self):
        if self.health_red <= 0:
            return False
        if self.health_green <= 0:
            return True

    def is_winner2(self):
        if self.health_blue <= 0:
            return False
        if self.health_yellow <= 0:
            return True

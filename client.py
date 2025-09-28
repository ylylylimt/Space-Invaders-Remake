import pygame
from network import Network
import button
import time

pygame.init()
pygame.font.init()
pygame.mixer.init()

myfont = pygame.font.Font("Grand9K Pixel.ttf", 50)

width = 900
height = 700

def create_window(game_id):
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption(f"Client {game_id}")
    return win

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

background_img = pygame.image.load("images/menu_background.png").convert_alpha()
menu_img = pygame.image.load("images/menu.png").convert_alpha()
start_img = pygame.image.load("images/button_start.png").convert_alpha()
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()

background_img = pygame.transform.scale(background_img, (width, height))

start_button = button.Button(470, 150, start_img, 1)
resume_button = button.Button(510, 250, resume_img, 1)
quit_button = button.Button(550, 350, quit_img, 1)

menu_img_x = 140
menu_img_y = 65


def redrawWindow(win, player, player2):
    win.fill((0, 0, 0))

    win.blit(background_img, (0, 0))
    player.mov()
    player2.mov()
    player.bul(win)
    player2.bul(win)
    player.colour()
    player2.colour()
    player.draw1(win)
    player2.draw1(win)
    pygame.display.update()


def draw_winner(win, a):
    draw_text = myfont.render(a, 1, (255, 255, 255))
    win.blit(draw_text, (900 / 2 - draw_text.get_width() / 2, 500 / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(5000)


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    win.blit(img, (x, y))


def main_menu():
    run = True
    game_paused = True
    menu_state = "main"

    while run:
        win.fill((52, 78, 91))

        win.blit(background_img, (0, 0))

        if game_paused:
            if menu_state == "main":
                if start_button.draw(win):
                    game_paused = False
                if resume_button.draw(win):
                    game_paused = False
                if quit_button.draw(win):
                    run = False
                    pygame.quit()
                win.blit(menu_img, (menu_img_x, menu_img_y))
        else:
            return True

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and not game_paused:
                if event.key == pygame.K_SPACE:
                    game_paused = True
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                return False

        pygame.display.update()


def main(game_id):
    n = Network(game_id)
    p = n.getP()
    clock = pygame.time.Clock()

    if not main_menu():
        return

    run = True
    game_paused = False

    while run:

        clock.tick(60)
        p2 = n.getP()

        n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_paused = not game_paused
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        if game_paused:
            main_menu()
            game_paused = False
        else:
            p.move(win)
            redrawWindow(win, p, p2)

            text = ""
            f = p.is_winner()
            if f == True:
                text = "Green Wins!"
            if f == False:
                text = "Red Wins!"

            f2 = p.is_winner2()
            if f2 == True:
                text = "Yellow Wins!"
            if f2 == False:
                text = "Blue Wins!"

            if text != "":
                draw_winner(win, text)
                break

    n.close()


if __name__ == "__main__":
    import sys
    game_id = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    main(game_id)
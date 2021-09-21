# Part E
# Digunakan untuk mengambil library yang digunakan
import pygame
import sys
from pygame import display

# digunakan untuk mendeklarasikan lebar tinggi window dan nama window serta tulisan pada window
WIDTH, HEIGHT = 620, 460
TITLE = "Smooth Movement"
font_color = (0, 0, 0)

# Digunakan untuk mendeklarasikan beberapa nilai yang digunakan seperti gambar, text, background dan lebar window
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.image.load("assets/background.jpg")
character = pygame.image.load("assets/fish.png")
pygame.display.set_caption(TITLE)
font = pygame.font.SysFont("Times New Roman", 25)
text = font.render("Ivan Fausta Dinata", True, font_color)
text1 = font.render("Game Fish & Sharp Coral Reef", True, font_color)
clock = pygame.time.Clock()

# Part D
# Digunakan untuk mengatur letak dari bangun yang dibuat untuk pertama kali dan memuat beberapa deklarasi atau persamaan nilai. dan digunakan untuk membuat warna pada bangun rect


class Player:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = (250, 120, 60)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4

    # Part F
    # Digunakan untuk membuat atau memunculkan rect pada window pygame
    def draw(self, win):
        win.blit(character, self.rect)

    # Part A
    # Digunakan untuk mengatur gerakan pada rect yang berasal dari inputan keyboard, dan memperbarui terus menerus sesuai dengan inputan yang ada

    def update(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed

        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)


# Part B
# Player Initialization
# Digunakan untuk membuat sebuah deklarasi baru yang menyataakan nilai player berasal dari pembagian lebar dan tinggi
player = Player(WIDTH/2, HEIGHT/2)

# Main Loop
# Digunakan sebagai perulangan
while True:
    # Digunakan untuk melooping event
    for event in pygame.event.get():
        # Jika mengklik keluar atau mengkeluarkan pygame akan mengkeluarkan pygame
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Digunakan jika tombol keyboard ditekan maka akan menjalankan nilai yang sesuai
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed = True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
        # Digunakan jika tidak ada tombol yang ditekan pada keyboard
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False

        # Digunakan untuk memberikan batasan gerakan pada object yang ada
        if player.x > 580:
            player.x = 580
        if player.x < 30:
            player.x = 10
        if player.y > 420:
            player.y = 420
        if player.y < 30:
            player.y = 10

    # Part C
    # Digunakan untuk mencetak semua deklarasi yang sudah ada sebelumnya seperti warna, background, dan text serta window
    win.fill((0, 0, 0))
    win.blit(background, (0, 0))
    win.blit(text, (220, 0))
    win.blit(text1, (160, 25))
    player.draw(win)

    # update
    player.update()
    pygame.display.flip()

    clock.tick(120)

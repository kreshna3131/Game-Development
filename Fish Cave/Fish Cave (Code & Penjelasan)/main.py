# Digunakan untuk mengimport fungsi random yang digunakan untuk merandom angka
import random
# Digunakan untuk mengimport fungsi sys yang digunakan untuk keluar dari game jika sys.exit dijalankan
import sys
# Digunakan untuk mengimport fungsi pygame yang digunakan untuk menjalankan game yang dibuat
import pygame
# Digunakan untuk mengimport basic pygame yang digunakan untuk menjalankan game yang dibuat
from pygame.locals import *


# Digunakan untuk mengatur fps dari game yang dibuat
FPS = 32
# Digunakan untuk mengatur tinggi dan lebar window tampilan game yang dibuat
SCREENWIDTH = 800
SCREENHEIGHT = 600
# Mendeklarasikan ukuran window yang digunakan sebagai screen tampilan
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
# Digunakan untuk mendeklarasikan nilai ground yang ada didalam game
GROUNDY = SCREENHEIGHT * 0.8
# Digunakan untuk mendeklarasikan game sound dan game sprites bernilai kosong
GAME_SPRITES = {}
GAME_SOUNDS = {}
# Digunakan untuk mendeklarasikan image yang digunakan didalam game
PLAYER = 'gallery/sprites/ikan.png'
BACKGROUND = 'gallery/sprites/bg.png'
PIPE = 'gallery/sprites/batu2.png'


# Digunakan untuk membuat sebuah class fungsi yang digunakan untuk membuat tampilan walcome screen yang didalamnya terdapat pesan penyambutan, dan perulangan sebagai menu yang jika diclose akan keluar dan jika tidak maka akan menjalankan game dengan memanggil asset yang digunakan pada tampilan game saat dimainkan atau sedang dimainkan


def welcomeScreen():
    # Mendeklarasikan tempat untuk setiap asset yang muncul atau digunakan
    playerx = int(SCREENWIDTH/5)
    playery = int((SCREENHEIGHT - GAME_SPRITES['player'].get_height())/2)
    messagex = int((SCREENWIDTH - GAME_SPRITES['message'].get_width())/2)
    messagey = int(SCREENHEIGHT*0.13)
    basex = -10
    # Perulangan untuk mengecek pemilihan menu yang digunakan
    while True:
        for event in pygame.event.get():
            # Percabangan jika tombol close ditekan maka akan keluar dari game yang sedang dibuka
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # Percabangan jika user atau pemain mengklik tombol key up atau spasi maka game akan otomatis dijalankan atau berjalan atau dimulai
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_SPRITES['background'], (0, 0))
                SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
                SCREEN.blit(GAME_SPRITES['message'], (messagex, messagey))
                SCREEN.blit(GAME_SPRITES['base'], (basex, 330))
                pygame.display.update()
                FPSCLOCK.tick(FPS)


# Digunakan untuk membuat sebuah class fungsi yang digunakan untuk membuat rintangan berupa karang tajam secara random, membuat fungsi terbang jika tombol space atau key up diklik, membuat score, serta mengatur rintangan yang dibuat jika terjadi beberapa masalah seperti ketidak sesuaiian


def mainGame():
    # Mendeklarasikan beberapa jumlah seperti score dan peletakan lokasi kordinat
    score = 0
    playerx = int(SCREENWIDTH/5)
    playery = int(SCREENWIDTH/2)
    basex = -10

    # mendeklarasikan pembuatan rintangan terumbu karang tajam secara random
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # Membuat list jarak atara rintangan terumbu karang satu bagian atas dengan terumbu karang tajam selanjutnya
    upperPipes = [
        {'x': SCREENWIDTH+200, 'y': newPipe1[0]['y']},
        {'x': SCREENWIDTH+300+(SCREENWIDTH/3), 'y': newPipe2[0]['y']},
    ]
    # Membuat list jarak atara rintangan terumbu karang satu bagian atas dengan terumbu karang tajam selanjutnya
    lowerPipes = [
        {'x': SCREENWIDTH+200, 'y': newPipe1[1]['y']},
        {'x': SCREENWIDTH+300+(SCREENWIDTH/3), 'y': newPipe2[1]['y']},
    ]

    # Mendeklarasikan beberapa nilai dari propertis yang digunakan dalam game
    pipeVelX = -4
    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    # Mendeklarasikan nilai kecepatan dari kepakan atau pergerakan dari objek
    playerFlapAccv = -8
    playerFlapped = False

    # melakukan perulangan while yang dimana jika while true
    while True:
        # maka event dalam pygame akan mengambil dengan get
        for event in pygame.event.get():
            # jika event.type ini sama dengan quit atau event.type sama dengan keydown dan escape
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                # maka lakukan perintah quit
                pygame.quit()
                sys.exit()
            # jika event.type ini sama dengan keydown dan space serta up
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                # jika player lebih dari 0 maka lakukan playerFlap dan tambahkan suara wing
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUNDS['wing'].play()

        # function akan mengembalikan nilai true jika player ini terjadi nabrak
        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes)
        if crashTest:
            return

        # check for score
        # mengecek score yang dimana playerx ditambah game dengan player dengan tinggi dibagi 2
        playerMidPos = playerx + GAME_SPRITES['player'].get_width()/2
        # perulangan for jika pipa di upperpipes
        for pipe in upperPipes:
            # maka deklrasi dan masukkan pipe x ditambah game dengan array 0 dan juga tinggi dibagi 2
            pipeMidPos = pipe['x'] + GAME_SPRITES['pipe'][0].get_width()/2
            # jika pipeMidPos kurang dari sama dengan player dan juga kurang dari PipeMidPos ditambah 4
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                # maka score ditambah sama dengan 1
                score += 1
                # dan mencetak score ditambah sound
                print(f"Your score is {score}")
                GAME_SOUNDS['point'].play()

        # jika playerVelY kurang dari maxVelY dan tidak playerFlapped
        if playerVelY < playerMaxVelY and not playerFlapped:
            # maka playerVelY ditambah sama dengan playerAccY
            playerVelY += playerAccY

        # jika playeFlapped ini sama dengan false
        if playerFlapped:
            playerFlapped = False
        # maka tinggi player sama dengan game player dan dapatkan tingginya
        playerHeight = GAME_SPRITES['player'].get_height()
        # deklarasi playery yang dimana jika playery ditambah minimal nya
        playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

        # menggerakkan pipa ke arah kiri
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        # menambahkan pipa baru saat pertama di screen
        # jika 0 kurang dari upperpipe dengan array 0 dan x kurang dari 5
        if 0 < upperPipes[0]['x'] < 5:
            # membuat pipa baru dengan random
            newpipe = getRandomPipe()
            # membuat pipa atas
            upperPipes.append(newpipe[0])
            # membuat pipa bawah
            lowerPipes.append(newpipe[1])

        # jika upperpipa ini index 0 dan string x kurang dari game dengan index 0 maka ambilkan lebarnya
        if upperPipes[0]['x'] < -GAME_SPRITES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        # digunakan untuk menampilkan pada screen dengan background
        SCREEN.blit(GAME_SPRITES['background'], (0, 0))
        # perulangan for jika lowerpipa ini didalam zip dengan upperpipe dan lowerpipe
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            # menampilkan jika game ini array pipe dan index 0
            SCREEN.blit(GAME_SPRITES['pipe'][0],
                        # mengambil upperpipa x dan juga upperpipe y
                        (upperPipe['x'], upperPipe['y']))
            # menampilkan jika game ini array pipe dan index 1
            SCREEN.blit(GAME_SPRITES['pipe'][1],
                        # maka lowerpipa x dan y
                        (lowerPipe['x'], lowerPipe['y']))

        # menampilkan gambar base pada screen dengan basex dan 330
        SCREEN.blit(GAME_SPRITES['base'], (basex, 330))
        # menampilkan gambar player dengan x dan y
        SCREEN.blit(GAME_SPRITES['player'], (playerx, playery))
        # untuk digit jika int x dan for x didalam list maka string score
        myDigits = [int(x) for x in list(str(score))]
        # deklarasi lebar sama dengan 0
        width = 0
        # perulangan for jika digit didalam mydigit
        for digit in myDigits:
            # lebar ditambah sama dengan game dengan array number dan digit maka tangkap lebarnya
            width += GAME_SPRITES['numbers'][digit].get_width()
        # jika xoffset ini diisi dengan lebar screen dikurang lebar dibagi 2
        Xoffset = (SCREENWIDTH - width)/2

        # jika digit didalam mydigit
        for digit in myDigits:
            # maka tampilkan number dan digit
            SCREEN.blit(GAME_SPRITES['numbers'][digit],
                        # yang dimana xoffset dan height dikali 0,12
                        (Xoffset, SCREENHEIGHT*0.12))
            # jika xoffset ditambah sama dengan game dengan array number dan digit maka tangkap lebarnya
            Xoffset += GAME_SPRITES['numbers'][digit].get_width()
        # pygame menampilkan display update untuk mengupdate
        pygame.display.update()
        # berfungsi untuk mengatur waktu dengan FPS
        FPSCLOCK.tick(FPS)

# mendefinisikan ketika player bertabarakan dengan rintangan/menyentuh ground


def isCollide(playerx, playery, upperPipes, lowerPipes):

    if playery > GROUNDY - 50 or playery < 0:
        #  memunculkan suara ketika bertabrakan
        GAME_SOUNDS['hit'].play()
        return True
    #  menambahkan fungsi ketika player menyentuh bebatuan lancip yang terletak di atas
    for pipe in upperPipes:
        pipeHeight = GAME_SPRITES['pipe'][0].get_height()
        # apabila pemain terkena bebatuan yang letaknya di atas maka akan mati
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width()):
            # menambahkan efek suara ketika player terkena bebatuan
            GAME_SOUNDS['hit'].play()
            # mengembalikan ke nilai benar
            return True

    # menambahkan fungsi ketika player menyentuh bebatuan lancip yang terletak di bawah
    for pipe in lowerPipes:
        # apabila pemain terkena bebatuan yang letaknya di atas maka akan mati
        if (playery + GAME_SPRITES['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_SPRITES['pipe'][0].get_width():
            # menambahkan efek suara ketika player terkena bebatuan
            GAME_SOUNDS['hit'].play()
            return True
    # mengembalikan ke nilai false
    return False

# mendefinisikan bebatuan lancip secara random


def getRandomPipe():
    # menambahkan panjang bebatuan lancip
    pipeHeight = GAME_SPRITES['pipe'][0].get_height()
    # memberikan batasan
    offset = SCREENHEIGHT/4
    # memberikan jarak acak pada bebatuan lancip
    y2 = offset + random.randrange(0, int(SCREENHEIGHT -
                                   GAME_SPRITES['base'].get_height() - 1.2 * offset))
    # untuk mendefinisikan letak bebatuan lancip
    pipeX = SCREENWIDTH + 10
    # untuk mendefinisikan letak bebatuan lancip
    y1 = pipeHeight - y2 + offset
    pipe = [
        # bebatuan lancip atas
        {'x': pipeX, 'y': -y1},
        # bebatuan lancip bawah
        {'x': pipeX, 'y': y2}
    ]
    # mengembalikan ke nilai pipe
    return pipe


# Ini akan menjadi poin utama dari mana permainan akan dimulai
if __name__ == "__main__":
    # Inisialisasi semua modul pygame
    pygame.init()
    # memberikan durasi pada game
    FPSCLOCK = pygame.time.Clock()
    # memberikan nama game pada program
    pygame.display.set_caption('Fish Cave Adventure')
    # menambahkan gambar berbentuk angka ketika mendapatkan skor
    GAME_SPRITES['numbers'] = (
        pygame.image.load('gallery/sprites/0.png').convert_alpha(),
        pygame.image.load('gallery/sprites/1.png').convert_alpha(),
        pygame.image.load('gallery/sprites/2.png').convert_alpha(),
        pygame.image.load('gallery/sprites/3.png').convert_alpha(),
        pygame.image.load('gallery/sprites/4.png').convert_alpha(),
        pygame.image.load('gallery/sprites/5.png').convert_alpha(),
        pygame.image.load('gallery/sprites/6.png').convert_alpha(),
        pygame.image.load('gallery/sprites/7.png').convert_alpha(),
        pygame.image.load('gallery/sprites/8.png').convert_alpha(),
        pygame.image.load('gallery/sprites/9.png').convert_alpha(),
    )
    # menambahkan gambar menu game
    GAME_SPRITES['message'] = pygame.image.load(
        'gallery/sprites/judul.png').convert_alpha()
    # menambahkan gambar untuk base pada game berubapa gambar bebatuan
    GAME_SPRITES['base'] = pygame.image.load(
        'gallery/sprites/base.png').convert_alpha()

    # menambahkan gambar untuk pipa pada game berubap gambar bebatuan yang lancip.
    GAME_SPRITES['pipe'] = (pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180),
                            pygame.image.load(PIPE).convert_alpha()
                            )

    # berfungsi untuk menambahkan suara pada game
    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

    # menambahkan gambar background pada game
    GAME_SPRITES['background'] = pygame.image.load(BACKGROUND).convert()
    # menambahkan gambar player(ikan) pada game
    GAME_SPRITES['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        # Menampilkan layar selamat datang kepada pengguna sampai dia menekan tombol
        welcomeScreen()
        # Ini adalah fungsi permainan utama
        mainGame()

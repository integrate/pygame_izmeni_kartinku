import pygame, time, izmeni_kartinku

screen = pygame.display.set_mode([900, 600])

pic1 = pygame.image.load("pictures/pic1.png")
pic1ch = pic1
pic1ch = izmeni_kartinku.izmeni_kartinku(pic1ch, 200, 200, [62, 68, 148], 80, [123,255,123])
pic1ch = izmeni_kartinku.izmeni_kartinku(pic1ch, 200, 200, [237, 28, 36], 150, [0,0,255,70])
pic1ch = izmeni_kartinku.izmeni_kartinku(pic1ch, 100, 100, [255,255,255], 1, [255,247,19])
pic1ch = izmeni_kartinku.izmeni_kartinku(pic1ch, 100, 100, [0,0,0], 1, [0,255,0,120])

while True:
    time.sleep(1/60)

    events = pygame.event.get()

    screen.fill([250,255,255])
    screen.blit(pic1, [0,0])

    screen.blit(pic1ch, [500,200])

    pygame.display.flip()
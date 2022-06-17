import pygame, time, izmeni_kartinku

screen = pygame.display.set_mode([900, 600])

pic1 = pygame.image.load("pictures/pic3.png")
pic1ch = pic1
# pic1ch = izmeni_kartinku.izmeni_kartinku(pic1ch, 200, 200, [62, 68, 148], 80)
# pic1ch = izmeni_kartinku.izmeni_kartinku(pic1ch, 200, 200, [237, 28, 36], 150)
# pic1ch = izmeni_kartinku.izmeni_kartinku(pic1ch, 200, 200, [255,255,255], 1)

while True:
    time.sleep(1/60)

    events = pygame.event.get()

    screen.fill([100,20,255])
    screen.blit(pic1, [0,0])

    screen.blit(pic1ch, [500,200])

    pygame.display.flip()
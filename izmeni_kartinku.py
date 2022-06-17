import pygame

# def get_not_used_color(kartinka:pygame.Surface):
#     """
#     Looks for not used color in picture
#     :param kartinka:
#     :return: [r,g,b]
#     """
#     for r in range(0,256):
#         for g in range(0,256):
#             for b in range(0,256):
#                 mask = pygame.mask.from_threshold(kartinka, [r,g,b])
#                 if mask.count()==0:
#                     return [r,g,b]
#     raise Exception("Can not find unused color on picture to make it transparent")


def izmeni_kartinku(kartinka:pygame.Surface, shirina, visota, uberi_cvet, porog):

    #change pic size
    kartinka = pygame.transform.scale(kartinka, [shirina, visota])

    #convert to picture with transparency data
    kartinka = kartinka.convert_alpha()

    # get mask of pixels with ignored colors
    m1 = pygame.mask.from_threshold(kartinka, uberi_cvet, [porog, porog, porog])

    # make square filled with one of ignored colors
    q2 = kartinka.copy()
    q2.fill(uberi_cvet)

    #set pixels should be transparent, unset pixels should be taken from original picture
    m1.to_surface(q2, setcolor=[0,0,0,0], unsetsurface=kartinka)
    return q2



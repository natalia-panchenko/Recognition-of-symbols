from PIL import Image, ImageDraw
from os import path
import copy


file_name = input("Введите название файла: ")


def image_init():
    print('image_init success')
    image = Image.open(path.join(file_name, file_name + ".png"))
    image.save('image.png', "PNG")
    image = Image.open('image.png')

    return image


def image_bin(image):
    pix = image.load()
    draw = ImageDraw.Draw(image)
    width, height = image.size

    for i in range(width):
        for j in range(height):
            red = pix[i, j][0]
            green = pix[i, j][1]
            blue = pix[i, j][2]
            S = red + green + blue
            if S <= 383:
                red, green, blue = 0, 0, 0
            else:
                red, green, blue = 255, 255, 255
            draw.point((i, j), (red, green, blue))

    # image.save("image.png", "PNG")
    image.save("bin_image.png", "PNG")
    del draw
    print('image_bin success')
    return image


def resize(image):
    width = 64
    height = 64
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save("resized_image.png", "PNG")
    print('resize success')
    return resized_image


def thinning(image):
    width = 64
    height = 64
    # start_image = Image.open("image.png")
    start_image = copy.deepcopy(image)
    # image = Image.open("image.png")
    draw = ImageDraw.Draw(image)

    pix = start_image.load()
    flag = False

    print('thinning init')

    while flag is False:
        flag = False

        for i in range(height):
            for j in range(width):
                if pix[i, j][0] == 0:
                    if pix[i - 1, j - 1][0] == 0 and pix[i, j - 1][0] == 0 and pix[i + 1, j - 1][0] == 0 and \
                                    pix[i + 1, j][0] == 0 and pix[i, j + 1][0] == 255 and \
                            (pix[i - 1, j + 1][0] == 255 or pix[i + 1, j + 1][0] == 255):
                        draw.point((i, j), (255, 255, 255))  # template a
                        flag = True
                        print('template a')

                    if pix[i - 1, j - 1][0] == 0 and pix[i, j - 1][0] == 0 and \
                            (pix[i + 1, j - 1][0] == 255 or pix[i + 1, j + 1][0] == 255) and pix[i + 1, j][0] == 255 \
                            and pix[i, j + 1][0] == 0 and pix[i - 1, j + 1][0] == 0:
                        draw.point((i, j), (255, 255, 255))  # template b
                        flag = True
                        print('template b')

                    if (pix[i - 1, j - 1][0] == 255 or pix[i + 1, j - 1][0] == 255) and \
                                    pix[i, j - 1][0] == 255 and pix[i - 1, j][0] == 0 and \
                                    pix[i - 1, j + 1][0] == 0 and pix[i, j + 1][0] == 0 \
                            and pix[i + 1, j + 1][0] == 0 and pix[i, j + 2][0] == 0:
                        draw.point((i, j), (255, 255, 255))  # template c
                        flag = True
                        print('template c')

                    if (pix[i - 1, j - 1][0] == 255 or pix[i - 1, j + 1][0] == 255) and \
                                    pix[i - 1, j][0] == 255 and pix[i, j - 1][0] == 0 \
                            and pix[i, j + 1][0] == 0 and pix[i + 1, j - 1][0] == 0 and pix[i + 1, j][0] == 0 \
                            and pix[i + 1, j + 1][0] == 0 and pix[i + 2, j] == 0:
                        draw.point((i, j), (255, 255, 255))  # template d
                        flag = True
                        print('template d')

                    if pix[i - 1, j][0] == 255 and pix[i - 1, j + 1][0] == 255 and pix[i, j - 1][0] == 0 \
                            and pix[i, j + 1][0] == 255 and pix[i + 1, j][0] == 0:
                        draw.point((i, j), (255, 255, 255))  # template e
                        flag = True
                        print('template e')

                    if pix[i - 1, j][0] == 0 and pix[i - 1, j + 1][0] == 0 and pix[i, j - 1][0] == 255 \
                            and pix[i, j + 1][0] == 0 and pix[i + 1, j - 1][0] == 255 and pix[i + 1, j][0] == 255:
                        draw.point((i, j), (255, 255, 255))  # template f
                        flag = True
                        print('template f')

                    if pix[i - 1, j - 1][0] == 255 and pix[i - 1, j][0] == 0 and pix[i - 1, j + 1][0] == 255 \
                            and pix[i, j - 1][0] == 255 and pix[i, j + 1][0] == 0 and pix[i + 1, j - 1][0] == 255 and \
                                    pix[i + 1, j][0] == 255 and pix[i + 1, j + 1][0] == 255:
                        draw.point((i, j), (255, 255, 255))  # template g
                        flag = True
                        print('template g')

                    if pix[i - 1, j][0] == 0 and pix[i, j - 1][0] == 0 \
                            and pix[i, j + 1][0] == 255 and pix[i + 1, j][0] == 255 and pix[i + 1, j + 1][0] == 255:
                        draw.point((i, j), (255, 255, 255))  # template h
                        flag = True
                        print('template h')

                    if pix[i - 1, j - 1][0] == 255 and pix[i - 1, j][0] == 255 and pix[i, j - 1][0] == 255 \
                            and pix[i, j + 1][0] == 0 and pix[i + 1, j][0] == 0 and pix[i + 1, j + 1][0] == 0:
                        draw.point((i, j), (255, 255, 255))  # template i
                        flag = True
                        print('template i')

                    if pix[i - 1, j - 1][0] == 255 and pix[i - 1, j][0] == 255 and pix[i - 1, j + 1][0] == 255 and \
                                    pix[i, j - 1][0] == 255 \
                            and pix[i, j + 1][0] == 0 and pix[i + 1, j - 1][0] == 255 and pix[i + 1, j][0] == 0 and \
                                    pix[i + 1, j + 1][0] == 255:
                        draw.point((i, j), (255, 255, 255))  # template j
                        flag = True
                        print('template j')

                    if pix[i - 1, j - 1][0] == 255 and pix[i - 1, j][0] == 255 and pix[i - 1, j + 1][0] == 255 and \
                                    pix[i, j - 1][0] == 255 \
                            and pix[i, j + 1][0] == 255 and pix[i + 1, j - 1][0] == 0 and pix[i + 1, j][0] == 0 and \
                                    pix[i + 1, j + 1][0] == 0:
                        draw.point((i, j), (255, 255, 255))  # template k
                        flag = True
                        print('template k')

                    if pix[i - 1, j - 1][0] == 0 and pix[i - 1, j][0] == 255 and pix[i - 1, j + 1][0] == 255 and \
                                    pix[i, j - 1][0] == 0 \
                            and pix[i, j + 1][0] == 255 and pix[i + 1, j - 1][0] == 0 and pix[i + 1, j][0] == 255 and \
                                    pix[i + 1, j + 1][0] == 255:
                        draw.point((i, j), (255, 255, 255))  # template l
                        flag = True
                        print('template l')

                    if pix[i - 1, j - 1][0] == 0 and pix[i - 1, j][0] == 0 and pix[i - 1, j + 1][0] == 0 and \
                                    pix[i, j - 1][0] == 255 \
                            and pix[i, j + 1][0] == 255 and pix[i + 1, j - 1][0] == 255 and pix[i + 1, j][
                        0] == 255 and pix[i + 1, j + 1][0] == 255:
                        draw.point((i, j), (255, 255, 255))  # template m
                        flag = True
                        print('template m')

                    if pix[i - 1, j - 1][0] == 255 and pix[i - 1, j][0] == 255 and pix[i - 1, j + 1][0] == 0 and \
                                    pix[i, j - 1][0] == 255 \
                            and pix[i, j + 1][0] == 0 and pix[i + 1, j - 1][0] == 255 and pix[i + 1, j][0] == 255 and \
                                    pix[i + 1, j + 1][0] == 0:
                        draw.point((i, j), (255, 255, 255))  # template n
                        flag = True
                        print('template n')

                        # if (pix[i - 1, j - 1][0] == 255 or pix[i, j + 1][0] == 255) and pix[i - 1, j][0] == 0 and pix[i - 1, j + 1][0] == 0 and \
                        # 				pix[i, j - 1][0] == 255 and pix[i + 1, j - 1][0] == 0 and pix[i + 1, j][0] == 0 and\
                        # 				pix[i + 1, j + 1][0] == 0: # template a2
                        # 	draw.point((i, j), (255, 255, 255))
                        # 	flag = True

                        # if (pix[i-1, j-1][0] == 255 or pix[i - 1, j +1][0] == 255) and pix[i - 1, j][0] == 255 and pix[i, j - 1][0] == 0\
                        # 		and pix[i, j + 1][0] == 0 and pix[i + 1, j - 1][0] == 0 and pix[i + 1, j][0] == 0 and pix[i + 1, j + 1][0] == 0:
                        # 	draw.point((i, j), (255,255,255)) #  template b2
                        # 	flag = True

    print('thinning end of templates')
    # image.save("image.png", "PNG")
    image.save("thin_image.png", "PNG")
    del draw
    print('thinning success')
    return image


image = image_init()
image = resize(image)
image = image_bin(image)
image = thinning(image)
image.save('image.png', 'PNG')
image.close()

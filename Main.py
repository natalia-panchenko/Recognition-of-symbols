from PIL import Image, ImageDraw
from os import path


file_name = input("Введите название файла: ")


def image_init():
    return Image.open(path.join(file_name, file_name + ".png"))


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
            if (S <= 383):
                red, green, blue = 0, 0, 0
            else:
                red, green, blue = 255, 255, 255
            draw.point((i, j), (red, green, blue))

    image.save("bin_" + file_name + ".png", "PNG")
    del draw


def thinning(image):
    width, height = image.size

    bin_image = Image.open("bin_" + file_name + ".png")
    bin_image1 = Image.open("bin_" + file_name + ".png")
    draw = ImageDraw.Draw(bin_image1)

    pix3 = bin_image.load()
    flag = False

    while flag is False:
        flag = False

        for i in range(height):
            for j in range(width):
                if pix3[i, j][0] == 0:
                    if pix3[i - 1, j - 1][0] == 0 and pix3[i, j - 1][0] == 0 and pix3[i + 1, j - 1][0] == 0 and \
                                    pix3[i + 1, j][0] == 0 and pix3[i, j + 1][0] == 255 and \
                            (pix3[i - 1, j + 1][0] == 255 or pix3[i + 1, j + 1][0] == 255):
                        draw.point((i, j), (255, 255, 255))  # template a
                        flag = True

                    if pix3[i - 1, j - 1][0] == 0 and pix3[i, j - 1][0] == 0 and \
                            (pix3[i + 1, j - 1][0] == 255 or pix3[i + 1, j + 1][0] == 255) and pix3[i + 1, j][0] == 255 \
                            and pix3[i, j + 1][0] == 0 and pix3[i - 1, j + 1][0] == 0:
                        draw.point((i, j), (255, 255, 255))  # template b
                        flag = True

                    if (pix3[i - 1, j - 1][0] == 255 or pix3[i + 1, j - 1][0] == 255) and \
                                    pix3[i, j - 1][0] == 255 and pix3[i - 1, j][0] == 0 and \
                                    pix3[i - 1, j + 1][0] == 0 and pix3[i, j + 1][0] == 0 \
                            and pix3[i + 1, j + 1][0] == 0 and pix3[i, j + 2][0] == 0:
                        draw.point((i, j), (255, 255, 255))  # template c
                        flag = True

                    if (pix3[i - 1, j - 1][0] == 255 or pix3[i - 1, j + 1][0] == 255) and \
                                    pix3[i - 1, j][0] == 255 and pix3[i, j - 1][0] == 0 \
                            and pix3[i, j + 1][0] == 0 and pix3[i + 1, j - 1][0] == 0 and pix3[i + 1, j][0] == 0 \
                            and pix3[i + 1, j + 1][0] == 0 and pix3[i + 2, j] == 0:
                        draw.point((i, j), (255, 255, 255))  # template d
                        flag = True

                    if pix3[i - 1, j][0] == 255 and pix3[i - 1, j + 1][0] == 255 and pix3[i, j - 1][0] == 0 \
                            and pix3[i, j + 1][0] == 255 and pix3[i + 1, j][0] == 0:
                        draw.point((i, j), (255, 255, 255))  # template e
                        flag = True

                    if pix3[i - 1, j][0] == 0 and pix3[i - 1, j + 1][0] == 0 and pix3[i, j - 1][0] == 255 \
                            and pix3[i, j + 1][0] == 0 and pix3[i + 1, j - 1][0] == 255 and pix3[i + 1, j][0] == 255:
                        draw.point((i, j), (255, 255, 255))  # template f
                        flag = True

                    if pix3[i - 1, j - 1][0] == 255 and pix3[i - 1, j][0] == 0 and pix3[i - 1, j + 1][0] == 255 \
                            and pix3[i, j - 1][0] == 255 and pix3[i, j + 1][0] == 0 and pix3[i + 1, j - 1][0] == 255 and \
                                    pix3[i + 1, j][0] == 255 and pix3[i + 1, j + 1][0] == 255:
                        draw.point((i, j), (255, 255, 255))  # template g
                        flag = True

                    if pix3[i - 1, j][0] == 0 and pix3[i, j - 1][0] == 0 \
                            and pix3[i, j + 1][0] == 255 and pix3[i + 1, j][0] == 255 and pix3[i + 1, j + 1][0] == 255:
                        draw.point((i, j), (255, 255, 255))  # template h
                        flag = True

                    if pix3[i - 1, j - 1][0] == 255 and pix3[i - 1, j][0] == 255 and pix3[i, j - 1][0] == 255 \
                            and pix3[i, j + 1][0] == 0 and pix3[i + 1, j][0] == 0 and pix3[i + 1, j + 1][0] == 0:
                        draw.point((i, j), (255, 255, 255))  # template i
                        flag = True

                    if pix3[i - 1, j - 1][0] == 255 and pix3[i - 1, j][0] == 255 and pix3[i - 1, j + 1][0] == 255 and \
                                    pix3[i, j - 1][0] == 255 \
                            and pix3[i, j + 1][0] == 0 and pix3[i + 1, j - 1][0] == 255 and pix3[i + 1, j][0] == 0 and \
                                    pix3[i + 1, j + 1][0] == 255:
                        draw.point((i, j), (255, 255, 255))  # template j
                        flag = True

                    if pix3[i - 1, j - 1][0] == 255 and pix3[i - 1, j][0] == 255 and pix3[i - 1, j + 1][0] == 255 and \
                                    pix3[i, j - 1][0] == 255 \
                            and pix3[i, j + 1][0] == 255 and pix3[i + 1, j - 1][0] == 0 and pix3[i + 1, j][0] == 0 and \
                                    pix3[i + 1, j + 1][0] == 0:
                        draw.point((i, j), (255, 255, 255))  # template k
                        flag = True

                    if pix3[i - 1, j - 1][0] == 0 and pix3[i - 1, j][0] == 255 and pix3[i - 1, j + 1][0] == 255 and \
                                    pix3[i, j - 1][0] == 0 \
                            and pix3[i, j + 1][0] == 255 and pix3[i + 1, j - 1][0] == 0 and pix3[i + 1, j][0] == 255 and \
                                    pix3[i + 1, j + 1][0] == 255:
                        draw.point((i, j), (255, 255, 255))  # template l
                        flag = True

                    if pix3[i - 1, j - 1][0] == 0 and pix3[i - 1, j][0] == 0 and pix3[i - 1, j + 1][0] == 0 and \
                                    pix3[i, j - 1][0] == 255 \
                            and pix3[i, j + 1][0] == 255 and pix3[i + 1, j - 1][0] == 255 and pix3[i + 1, j][
                        0] == 255 and pix3[i + 1, j + 1][0] == 255:
                        draw.point((i, j), (255, 255, 255))  # template m
                        flag = True

                    if pix3[i - 1, j - 1][0] == 255 and pix3[i - 1, j][0] == 255 and pix3[i - 1, j + 1][0] == 0 and \
                                    pix3[i, j - 1][0] == 255 \
                            and pix3[i, j + 1][0] == 0 and pix3[i + 1, j - 1][0] == 255 and pix3[i + 1, j][0] == 255 and \
                                    pix3[i + 1, j + 1][0] == 0:
                        draw.point((i, j), (255, 255, 255))  # template n
                        flag = True

                        # if (pix3[i - 1, j - 1][0] == 255 or pix3[i, j + 1][0] == 255) and pix3[i - 1, j][0] == 0 and pix3[i - 1, j + 1][0] == 0 and \
                        # 				pix3[i, j - 1][0] == 255 and pix3[i + 1, j - 1][0] == 0 and pix3[i + 1, j][0] == 0 and\
                        # 				pix3[i + 1, j + 1][0] == 0: # template a2
                        # 	draw.point((i, j), (255, 255, 255))
                        # 	flag = True

                        # if (pix3[i-1, j-1][0] == 255 or pix3[i - 1, j +1][0] == 255) and pix3[i - 1, j][0] == 255 and pix3[i, j - 1][0] == 0\
                        # 		and pix3[i, j + 1][0] == 0 and pix3[i + 1, j - 1][0] == 0 and pix3[i + 1, j][0] == 0 and pix3[i + 1, j + 1][0] == 0:
                        # 	draw.point((i, j), (255,255,255)) #  template b2
                        # 	flag = True

    bin_image1.save("bin_" + file_name + "_1.png", "PNG")
    del draw


image = image_init()
image_bin(image)
thinning(image)
image.close()

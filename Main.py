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


def scaling(image):
    width = 64
    height = 64
    pix = image.load()
    first_row = 0
    last_row = 0
    print("ok")
    flag = False

    for j in range(width):
        if flag == True:
            break
        for i in range(height):
            if pix[i, j][0] == 0:
                first_row = j
                print(first_row)
                flag = True
                break

    j = width - 1
    flag = False

    while j >= 0:
        if flag == True:
            break
        i = height - 1
        while i >= 0:
            if pix[i, j][0] == 0:
                last_row = j
                flag = True
                break
            i -= 1
        j -= 1

        # for i in range(height):
        #     if flag == True:
        #         break
        #     for j in range(width):
        #         print(i, j)
        #         if pix[i, j][0] == 0:
        #             first_row = i
        #             print(first_row)
        #             flag = True
        #             break
        #
        # i = height - 1
        # flag = False
        #
        # while i >= 0:
        #     if flag == True:
        #         break
        #     j = width - 1
        #     while j >= 0:
        #         if pix[i, j][0] == 0:
        #             last_row = i
        #             flag = True
        #             break
        #         j -= 1
        #     i -= 1

    symbol_height = last_row - first_row + 1
    print(symbol_height, last_row, first_row)

    if symbol_height > 20:
        height = 64 - (symbol_height - 20) - 4
        print(height)
        scal_image = image.resize((height, height), Image.ANTIALIAS)
        scal_image.save("scal_image.png", "PNG")
        print('scaling success')
        print(type(scal_image))
        return scal_image


def thinning(image):
    width, height = image.size
    draw = ImageDraw.Draw(image)

    flag = True

    print('thinning init')

    while flag:
        start_image = copy.deepcopy(image)
        pix = start_image.load()
        flag = False
        for i in range(width):
            for j in range(height):
                if pix[j, i][0] == 0:
                    if pix[j - 1, i - 1][0] == 0 and pix[j, i - 1][0] == 0 and pix[j + 1, i - 1][0] == 0 and \
                                    pix[j + 1, i][0] == 0 and pix[j, i + 1][0] == 255 and \
                            (pix[j - 1, i + 1][0] == 255 or pix[j + 1, i + 1][0] == 255):
                        flag = True
                        print('template a')

                    if pix[j - 1, i - 1][0] == 0 and pix[j, i - 1][0] == 0 and \
                            (pix[j + 1, i - 1][0] == 255 or pix[j + 1, i + 1][0] == 255) and pix[j + 1, i][0] == 255 \
                            and pix[j, i + 1][0] == 0 and pix[j - 1, i + 1][0] == 0:
                        draw.point((j, i), (255, 255, 255))  # template b
                        flag = True
                        print('template b')

                    if (pix[j - 1, i - 1][0] == 255 or pix[j + 1, i - 1][0] == 255) and \
                                    pix[j, i - 1][0] == 255 and pix[j - 1, i][0] == 0 and \
                                    pix[j - 1, i + 1][0] == 0 and pix[j, i + 1][0] == 0 \
                            and pix[j + 1, i + 1][0] == 0 and pix[j, i + 2][0] == 0:
                        draw.point((j, i), (255, 255, 255))  # template c
                        flag = True
                        print('template c')

                    if (pix[j - 1, i - 1][0] == 255 or pix[j - 1, i + 1][0] == 255) and \
                                    pix[j - 1, i][0] == 255 and pix[j, i - 1][0] == 0 \
                            and pix[j, i + 1][0] == 0 and pix[j + 1, i - 1][0] == 0 and pix[j + 1, i][0] == 0 \
                            and pix[j + 1, i + 1][0] == 0 and pix[j + 2, i] == 0:
                        draw.point((j, i), (255, 255, 255))  # template d
                        flag = True
                        print('template d')

                    if pix[j - 1, i][0] == 255 and pix[j - 1, i + 1][0] == 255 and pix[j, i - 1][0] == 0 \
                            and pix[j, i + 1][0] == 255 and pix[j + 1, i][0] == 0:
                        draw.point((j, i), (255, 255, 255))  # template e
                        flag = True
                        print('template e')

                    if pix[j - 1, i][0] == 0 and pix[j - 1, i + 1][0] == 0 and pix[j, i - 1][0] == 255 \
                            and pix[j, i + 1][0] == 0 and pix[j + 1, i - 1][0] == 255 and pix[j + 1, i][0] == 255:
                        draw.point((j, i), (255, 255, 255))  # template f
                        flag = True
                        print('template f')

                    if pix[j - 1, i - 1][0] == 255 and pix[j - 1, i][0] == 0 and pix[j - 1, i + 1][0] == 255 \
                            and pix[j, i - 1][0] == 255 and pix[j, i + 1][0] == 0 and pix[j + 1, i - 1][0] == 255 and \
                                    pix[j + 1, i][0] == 255 and pix[j + 1, i + 1][0] == 255:
                        draw.point((j, i), (255, 255, 255))  # template g
                        flag = True
                        print('template g')

                    if pix[j - 1, i][0] == 0 and pix[j, i - 1][0] == 0 \
                            and pix[j, i + 1][0] == 255 and pix[j + 1, i][0] == 255 and pix[j + 1, i + 1][0] == 255:
                        draw.point((j, i), (255, 255, 255))  # template h
                        flag = True
                        print('template h')

                    if pix[j - 1, i - 1][0] == 255 and pix[j - 1, i][0] == 255 and pix[j, i - 1][0] == 255 \
                            and pix[j, i + 1][0] == 0 and pix[j + 1, i][0] == 0 and pix[j + 1, i + 1][0] == 0:
                        draw.point((j, i), (255, 255, 255))  # template i
                        flag = True
                        print('template i')

                    if pix[j - 1, i - 1][0] == 255 and pix[j - 1, i][0] == 255 and pix[j - 1, i + 1][0] == 255 and \
                                    pix[j, i - 1][0] == 255 \
                            and pix[j, i + 1][0] == 0 and pix[j + 1, i - 1][0] == 255 and pix[j + 1, i][0] == 0 and \
                                    pix[j + 1, i + 1][0] == 255:
                        draw.point((j, i), (255, 255, 255))  # template j
                        flag = True
                        print('template j')

                    if pix[j - 1, i - 1][0] == 255 and pix[j - 1, i][0] == 255 and pix[j - 1, i + 1][0] == 255 and \
                                    pix[j, i - 1][0] == 255 \
                            and pix[j, i + 1][0] == 255 and pix[j + 1, i - 1][0] == 0 and pix[j + 1, i][0] == 0 and \
                                    pix[j + 1, i + 1][0] == 0:
                        draw.point((j, i), (255, 255, 255))  # template k
                        flag = True
                        print('template k')

                    if pix[j - 1, i - 1][0] == 0 and pix[j - 1, i][0] == 255 and pix[j - 1, i + 1][0] == 255 and \
                                    pix[j, i - 1][0] == 0 \
                            and pix[j, i + 1][0] == 255 and pix[j + 1, i - 1][0] == 0 and pix[j + 1, i][0] == 255 and \
                                    pix[j + 1, i + 1][0] == 255:
                        draw.point((j, i), (255, 255, 255))  # template l
                        flag = True
                        print('template l')

                    if pix[j - 1, i - 1][0] == 0 and pix[j - 1, i][0] == 0 and pix[j - 1, i + 1][0] == 0 and \
                                    pix[j, i - 1][0] == 255 \
                            and pix[j, i + 1][0] == 255 and pix[j + 1, i - 1][0] == 255 and pix[j + 1, i][
                        0] == 255 and pix[j + 1, i + 1][0] == 255:
                        draw.point((j, i), (255, 255, 255))  # template m
                        flag = True
                        print('template m')

                    if pix[j - 1, i - 1][0] == 255 and pix[j - 1, i][0] == 255 and pix[j - 1, i + 1][0] == 0 and \
                                    pix[j, i - 1][0] == 255 \
                            and pix[j, i + 1][0] == 0 and pix[j + 1, i - 1][0] == 255 and pix[j + 1, i][0] == 255 and \
                                    pix[j + 1, i + 1][0] == 0:
                        draw.point((j, i), (255, 255, 255))  # template n
                        flag = True
                        print('template n')

    print('thinning end of templates')
    image.save("thin_image.png", "PNG")
    del draw
    print('thinning success')
    return image


def key_pixels_find(image):
    width, height = image.size
    draw = ImageDraw.Draw(image)
    start_image = copy.deepcopy(image)
    pix = start_image.load()

    for i in range(width):
        for j in range(height):
            neigh_counter = 0
            if pix[i, j][0] == 0:
                if pix[i - 1, j - 1][0] == 0:
                    neigh_counter += 1
                if pix[i, j - 1][0] == 0:
                    neigh_counter += 1
                if pix[i + 1, j - 1][0] == 0:
                    neigh_counter += 1
                if pix[i - 1, j][0] == 0:
                    neigh_counter += 1
                if pix[i + 1, j][0] == 0:
                    neigh_counter += 1
                if pix[i - 1, j + 1][0] == 0:
                    neigh_counter += 1
                if pix[i, j + 1][0] == 0:
                    neigh_counter += 1
                if pix[i + 1, j + 1][0] == 0:
                    neigh_counter += 1

                if neigh_counter != 2:
                    draw.point((i, j), (1, 210, 255))

    image = key_pixels_delete(image)

    return image


def key_pixels_delete(image):
    width, height = image.size
    draw = ImageDraw.Draw(image)
    start_image = copy.deepcopy(image)
    pix = start_image.load()

    for i in range(width):
        for j in range(height):
            if pix[i, j][0] == 1:

                if pix[i - 1, j][0] == 1 and pix[i, j - 1][0] == 1:
                    draw.point((i - 1, j), (0, 0, 0))
                    draw.point((i, j - 1), (0, 0, 0))

                if pix[i + 1, j][0] == 1 and pix[i, j + 1][0] == 1:
                    draw.point((i + 1, j), (0, 0, 0))
                    draw.point((i, j + 1), (0, 0, 0))

                if pix[i, j - 1][0] == 1 and pix[i + 1, j][0] == 1:
                    draw.point((i, j - 1), (0, 0, 0))
                    draw.point((i + 1, j), (0, 0, 0))

                if pix[i - 1, j][0] == 1 and pix[i, j + 1][0] == 1:
                    draw.point((i - 1, j), (0, 0, 0))
                    draw.point((i, j + 1), (0, 0, 0))

    return image


def thinning_ZS(image):
    width, height = image.size
    draw = ImageDraw.Draw(image)

    flag = True

    while flag:
        flag = False
        start_image = copy.deepcopy(image)
        pix = start_image.load()
        for i in range(width):
            for j in range(height):
                black_neighbours = 0
                if pix[i, j][0] == 0:
                    # condition a
                    if pix[i - 1, j - 1][0] == 0:
                        black_neighbours += 1
                    if pix[i, j - 1][0] == 0:
                        black_neighbours += 1
                    if pix[i + 1, j - 1][0] == 0:
                        black_neighbours += 1
                    if pix[i + 1, j][0] == 0:
                        black_neighbours += 1
                    if pix[i + 1, j + 1][0] == 0:
                        black_neighbours += 1
                    if pix[i, j + 1][0] == 0:
                        black_neighbours += 1
                    if pix[i - 1, j + 1][0] == 0:
                        black_neighbours += 1
                    if pix[i - 1, j][0] == 0:
                        black_neighbours += 1

                    if black_neighbours < 2 or black_neighbours > 6:
                        continue

                    # condition b
                    transitions_number = 0
                    if pix[i, j - 1][0] == 255 and pix[i + 1, j - 1][0] == 0:
                        transitions_number += 1
                    if pix[i + 1, j - 1][0] == 255 and pix[i + 1, j][0] == 0:
                        transitions_number += 1
                    if pix[i + 1, j][0] == 255 and pix[i + 1, j + 1][0] == 0:
                        transitions_number += 1
                    if pix[i + 1, j + 1][0] == 255 and pix[i, j + 1][0] == 0:
                        transitions_number += 1
                    if pix[i, j + 1][0] == 255 and pix[i - 1, j + 1][0] == 0:
                        transitions_number += 1
                    if pix[i - 1, j + 1][0] == 255 and pix[i - 1, j][0] == 0:
                        transitions_number += 1
                    if pix[i - 1, j][0] == 255 and pix[i - 1, j - 1][0] == 0:
                        transitions_number += 1
                    if pix[i - 1, j - 1][0] == 255 and pix[i, j - 1][0] == 0:
                        transitions_number += 1

                    if transitions_number != 1:
                        continue

                    # condition c, d
                    condition_cd_first = False

                    if pix[i, j - 1][0] + pix[i + 1, j][0] + pix[i, j + 1][0] >= 255 and \
                                                    pix[i + 1, j][0] + pix[i, j + 1][0] + pix[i - 1, j][0] >= 255:
                        condition_cd_first = True

                    if not condition_cd_first:
                        continue

                    draw.point((i, j), (255, 255, 255))
                    # print(i, j)
                    flag = True

        start_image = copy.deepcopy(image)
        pix = start_image.load()
        for i in range(width):
            for j in range(height):
                black_neighbours = 0
                if pix[i, j][0] == 0:
                    # condition a
                    if pix[i - 1, j - 1][0] == 0:
                        black_neighbours += 1
                    if pix[i, j - 1][0] == 0:
                        black_neighbours += 1
                    if pix[i + 1, j - 1][0] == 0:
                        black_neighbours += 1
                    if pix[i + 1, j][0] == 0:
                        black_neighbours += 1
                    if pix[i + 1, j + 1][0] == 0:
                        black_neighbours += 1
                    if pix[i, j + 1][0] == 0:
                        black_neighbours += 1
                    if pix[i - 1, j + 1][0] == 0:
                        black_neighbours += 1
                    if pix[i - 1, j][0] == 0:
                        black_neighbours += 1

                    if black_neighbours < 2 or black_neighbours > 6:
                        continue

                    # condition b
                    transitions_number = 0
                    if pix[i, j - 1][0] == 255 and pix[i + 1, j - 1][0] == 0:
                        transitions_number += 1
                    if pix[i + 1, j - 1][0] == 255 and pix[i + 1, j][0] == 0:
                        transitions_number += 1
                    if pix[i + 1, j][0] == 255 and pix[i + 1, j + 1][0] == 0:
                        transitions_number += 1
                    if pix[i + 1, j + 1][0] == 255 and pix[i, j + 1][0] == 0:
                        transitions_number += 1
                    if pix[i, j + 1][0] == 255 and pix[i - 1, j + 1][0] == 0:
                        transitions_number += 1
                    if pix[i - 1, j + 1][0] == 255 and pix[i - 1, j][0] == 0:
                        transitions_number += 1
                    if pix[i - 1, j][0] == 255 and pix[i - 1, j - 1][0] == 0:
                        transitions_number += 1
                    if pix[i - 1, j - 1][0] == 255 and pix[i, j - 1][0] == 0:
                        transitions_number += 1

                    if transitions_number != 1:
                        continue

                    # condition c, d
                    condition_cd_second = False

                    if pix[i, j - 1][0] + pix[i + 1, j][0] + pix[i - 1, j][0] >= 255 and \
                                                    pix[i, j - 1][0] + pix[i, j + 1][0] + pix[i - 1, j][0] >= 255:
                        condition_cd_second = True

                    if not condition_cd_second:
                        continue

                    draw.point((i, j), (255, 255, 255))
                    # print(i, j)
                    flag = True

    return image


def smth(image):
    width, height = image.size
    pix = image.load()
    key_pixels = []

    for i in range(width):
        for j in range(height):
            neigh_counter = 0
            if pix[i, j][0] == 1:
                # key_pixels.append({"coordinates": (i, j)})
                if pix[i - 1, j - 1][0] == 0:
                    neigh_counter += 1
                if pix[i, j - 1][0] == 0:
                    neigh_counter += 1
                if pix[i + 1, j - 1][0] == 0:
                    neigh_counter += 1
                if pix[i - 1, j][0] == 0:
                    neigh_counter += 1
                if pix[i + 1, j][0] == 0:
                    neigh_counter += 1
                if pix[i - 1, j + 1][0] == 0:
                    neigh_counter += 1
                if pix[i, j + 1][0] == 0:
                    neigh_counter += 1
                if pix[i + 1, j + 1][0] == 0:
                    neigh_counter += 1
                if neigh_counter == 0:
                    key_pixels.append({"coordinates": (i, j), "type": "type-0"})
                elif neigh_counter == 1:
                    key_pixels.append({"coordinates": (i, j), "type": "type-1"})
                elif neigh_counter == 3:
                    key_pixels.append({"coordinates": (i, j), "type": "type-3"})
                elif neigh_counter == 4:
                    key_pixels.append({"coordinates": (i, j), "type": "type-4"})

    print(key_pixels)

    # length = 0
    # bends = 0
    # for k in key_pixels:
    #     x = key_pixels.keys(k)
    #     y = key_pixels.keys(k + 1)
    #
    #     while True:
    #         i = x
    #         j = y
    #         if pix[i, j - 1][0] == 0:
    #             length += 1
    #             x = i
    #             y = j - 1
    #
    #         if pix[i, j + 1][0] == 0:
    #             length += 1
    #             x = i
    #             y = j + 1
    #
    #         if pix[i - 1, j][0] == 0:
    #             length += 1
    #             x = i - 1
    #             y = j
    #
    #         if pix[i + 1, j][0] == 0:
    #             length += 1
    #             x = i + 1
    #             y = j
    #
    #         if pix[i - 1, j - 1][0] == 0 or pix[i - 1, j + 1][0] == 0 or pix[i + 1, j - 1][0] == 0 \
    #             or pix[i + 1, j + 1][0] == 0:
    #             length += 1
    #             bends += 1
    return image


image = image_init()
image = resize(image)
image = image_bin(image)
image = thinning_ZS(image)
image = thinning(image)
image = key_pixels_find(image)
image = smth(image)
image.save('image.png', 'PNG')
image.close()

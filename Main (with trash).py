from PIL import Image, ImageDraw
import numpy as np
from os import path


file_name = input("Введите название файла: ")

with Image.open(path.join(file_name, file_name + ".png")) as image:
	draw = ImageDraw.Draw(image)
	width, height = image.size

	pix = image.load()

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

bin_image = Image.open("bin_" + file_name + ".png")

# pix = np.array([pix[i, j] for j in range(width) for i in range(height)])
# np.set_printoptions(threshold=np.nan)

# array_for_1 = open(path.join(file_name,'array_for_'+ file_name + '.txt'),'w')
# array_for_1.write(str(pix))
# array_for_1.close()

# pix2 = []
#
# for i in range(pix.size//3):
# 	if pix[i][1] == 0:
# 		pix2.insert(i, 1)
# 	else:
# 		pix2.insert(i, 0)
#
# pix2 = np.array(pix2)
# pix2.shape = (width, height)
#
# # with open('array2.txt, 'w') as file:
# 	# .....
#
#
# bay_array_for_1 = open(path.join(file_name, 'array2.txt'),'w')
# bay_array_for_1.write(str(pix2))
# bay_array_for_1.close()

bin_image1 = Image.open("bin_" + file_name + ".png")
draw = ImageDraw.Draw(bin_image1)

pix3 = bin_image.load()
flag = False

while flag is False:
	flag = False

	for i in range(height):
		for j in range(width):
			if pix3[i, j][0] == 0:
				if pix3[i-1, j-1][0] == 0 and pix3[i, j-1][0] == 0 and pix3[i+1, j-1][0] == 0 and \
				pix3[i+1, j][0] == 0 and pix3[i, j+1][0] == 255 and \
						(pix3[i-1, j+1][0] == 255 or pix3[i+1, j+1][0] == 255):
					draw.point((i, j), (255,255,255)) #  template a
					flag = True
					#break

				if pix3[i-1, j-1][0] == 0 and pix3[i, j-1][0] == 0 and \
				(pix3[i+1, j-1][0] == 255 or pix3[i+1, j+1][0] == 255) and pix3[i+1, j][0] == 255\
				and pix3[i, j+1][0] == 0 and pix3[i-1, j+1][0] == 0:
					draw.point((i, j), (255,255,255)) #  template b
					flag = True
					#break

				if (pix3[i-1, j-1][0] == 255 or pix3[i+1, j-1][0] == 255) and\
				pix3[i, j-1][0] == 255 and pix3[i-1, j][0] == 0 and\
				pix3[i-1, j+1][0] == 0 and pix3[i, j+1][0] == 0 \
				and pix3[i+1, j+1][0] == 0 and pix3[i, j+2][0] == 0:
					draw.point((i, j), (255,255,255)) #  template c
					flag = True
					#break

				if (pix3[i - 1, j - 1][0] == 255 or pix3[i - 1, j + 1][0] == 255) and\
				pix3[i - 1, j][0] == 255 and pix3[i, j - 1][0] == 0\
				and pix3[i, j + 1][0] == 0 and pix3[i + 1, j - 1][0] == 0 and pix3[i + 1, j][0] == 0 \
				and pix3[i + 1, j + 1][0] == 0 and pix3[i + 2, j] == 0:
					draw.point((i, j), (255, 255, 255)) # template d
					flag = True
					#break

				if pix3[i - 1, j][0] == 255 and pix3[i - 1, j + 1][0] == 255 and pix3[i, j - 1][0] == 0 \
					and pix3[i, j + 1][0] == 255 and pix3[i + 1, j][0] == 0:
					draw.point((i, j), (255, 255, 255)) #  template e
					flag = True
					#break

				if pix3[i - 1, j][0] == 0 and pix3[i - 1, j + 1][0] == 0 and pix3[i, j - 1][0] == 255 \
					and pix3[i, j + 1][0] == 0 and pix3[i + 1, j - 1][0] == 255 and pix3[i + 1, j][0] == 255:
					draw.point((i, j), (255, 255, 255)) #  template f
					flag = True
					#break

				if pix3[i - 1, j - 1][0] == 255 and pix3[i - 1, j][0] == 0 and pix3[i - 1, j + 1][0] == 255\
				and pix3[i, j - 1][0] == 255 and pix3[i, j + 1][0] == 0 and pix3[i + 1, j - 1][0] == 255 and\
				pix3[i + 1, j][0] == 255 and pix3[i + 1, j + 1][0] == 255:
					draw.point((i, j), (255, 255, 255)) #  template g
					flag = True
					#break

				if pix3[i - 1, j][0] == 0 and pix3[i, j - 1][0] == 0 \
					and pix3[i, j + 1][0] == 255 and pix3[i + 1, j][0] == 255 and pix3[i + 1, j + 1][0] == 255:
					draw.point((i, j), (255, 255, 255)) #  template h
					flag = True
					#break

				if pix3[i - 1, j - 1][0] == 255 and pix3[i - 1, j][0] == 255 and pix3[i, j - 1][0] == 255 \
					and pix3[i, j + 1][0] == 0 and pix3[i + 1, j][0] == 0 and pix3[i + 1, j + 1][0] == 0:
					draw.point((i, j), (255, 255, 255)) #  template i
					flag = True
					#break

				if pix3[i - 1, j - 1][0] == 255 and pix3[i - 1, j][0] == 255 and pix3[i - 1, j + 1][0] == 255 and pix3[i, j - 1][0] == 255 \
					and pix3[i, j + 1][0] == 0 and pix3[i + 1, j - 1][0] == 255 and pix3[i + 1, j][0] == 0 and pix3[i + 1, j + 1][0] == 255:
					draw.point((i, j), (255, 255, 255)) #  template j
					flag = True
					#break

				if pix3[i - 1, j - 1][0] == 255 and pix3[i - 1, j][0] == 255 and pix3[i - 1, j + 1][0] == 255 and pix3[i, j - 1][0] == 255 \
					and pix3[i, j + 1][0] == 255 and pix3[i + 1, j - 1][0] == 0 and pix3[i + 1, j][0] == 0 and pix3[i + 1, j + 1][0] == 0:
					draw.point((i, j), (255, 255, 255)) # template k
					flag = True
					#break

				if pix3[i - 1, j - 1][0] == 0 and pix3[i - 1, j][0] == 255 and pix3[i - 1, j + 1][0] == 255 and pix3[i, j - 1][0] == 0 \
					and pix3[i, j + 1][0] == 255 and pix3[i + 1, j - 1][0] == 0 and pix3[i + 1, j][0] == 255 and pix3[i + 1, j + 1][0] == 255:
					draw.point((i, j), (255, 255, 255)) #  template l
					flag = True
					#break

				if pix3[i - 1, j - 1][0] == 0 and pix3[i - 1, j][0] == 0 and pix3[i - 1, j + 1][0] == 0 and pix3[i, j - 1][0] == 255 \
					and pix3[i, j + 1][0] == 255 and pix3[i + 1, j - 1][0] == 255 and pix3[i + 1, j][0] == 255 and pix3[i + 1, j + 1][0] == 255:
					draw.point((i, j), (255, 255, 255)) #  template m
					flag = True
					#break

				if pix3[i - 1, j - 1][0] == 255 and pix3[i - 1, j][0] == 255 and pix3[i - 1, j + 1][0] == 0 and pix3[i, j - 1][0] == 255 \
					and pix3[i, j + 1][0] == 0 and pix3[i + 1, j - 1][0] == 255 and pix3[i + 1, j][0] == 255 and pix3[i + 1, j + 1][0] == 0:
					draw.point((i, j), (255, 255, 255)) #  template n
					flag = True
					#break
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

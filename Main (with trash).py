from PIL import Image, ImageDraw
import numpy as np
from os import path


file_name = input("Введите название файла: ")

with Image.open(path.join(file_name, file_name + ".png")) as image:
	#width, height = image.size
	width = 62
	height = 62
	resized_image = image.resize((width, height), Image.ANTIALIAS)
	resized_image.save("resized_" + file_name + ".png")

	draw = ImageDraw.Draw(resized_image)
	pix = resized_image.load()

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

	resized_image.save("bin_" + file_name + ".png", "PNG")
	del draw

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

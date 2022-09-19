from colorizer import colorize

path = 'image.png'
target = [150, 10, 10]
tolerance = [30, 10, 10]
new_color = (100, 200, 245)

image = colorize(path, target, tolerance, new_color)
image.save('colorized.png', optimize=True)
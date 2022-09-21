from colorizer import colorize_by_tolerance, colorize_by_range

mode = 'tolerance'
path = 'image.png'
target = [150, 10, 10]
tolerance = [30, 10, 10]
new_color = (100, 200, 245)

# mode = 'range'
# path = 'image.png'
# high_target = [175, 20, 20]
# low_target = [140, 0, 0]
# new_color = (100, 200, 245)

if (mode == 'tolerance'):
    image = colorize_by_tolerance(path, target, tolerance, new_color)
    image.save('colorized.png', optimize=True)

if (mode == 'range'):
    image = colorize_by_range(path, high_target, low_target, new_color)
    image.save('colorized.png', optimize=True)
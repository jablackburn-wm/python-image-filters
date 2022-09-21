from PIL import Image

def colorize_by_tolerance(path, target, tolerance, new_color):
    image = Image.open(path).convert('RGB')

    pixels = image.getdata()

    new_pixels = []

    for p in pixels:
        new_pixels.append(p)

    pointer = 0

    while pointer < len(new_pixels):

        p = new_pixels[pointer]

        r = p[0]
        g = p[1]
        b = p[2]

        if (
            r < (target[0] + tolerance[0]) and 
            r > (target[0] - tolerance[0]) and 
            g < (target[0] + tolerance[0]) and 
            g > (target[1] - tolerance[1]) and 
            b < (target[2] + tolerance[2]) and 
            b > (target[2] - tolerance[2])
        ):
            new_pixels[pointer] = new_color

        pointer += 1

    newImage = Image.new("RGB", image.size)
    newImage.putdata(new_pixels)

    return newImage



def colorize_by_range(path, high_target, low_target, new_color):
    image = Image.open(path).convert('RGB')

    pixels = image.getdata()

    new_pixels = []

    for p in pixels:
        new_pixels.append(p)

    pointer = 0

    while pointer < len(new_pixels):

        p = new_pixels[pointer]

        r = p[0]
        g = p[1]
        b = p[2]

        if (
            r < (high_target[0]) and 
            r > (low_target[0]) and 
            g < (high_target[1]) and 
            g > (low_target[1]) and 
            b < (high_target[2]) and 
            b > (low_target[2])
        ):
            new_pixels[pointer] = new_color

        pointer += 1

    newImage = Image.new("RGB", image.size)
    newImage.putdata(new_pixels)

    return newImage
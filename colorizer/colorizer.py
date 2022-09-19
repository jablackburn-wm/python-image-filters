from PIL import Image

def colorize(path, target, tolerance, new_color):
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
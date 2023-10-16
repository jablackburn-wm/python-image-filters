from PIL import Image 
import math

def ambiguousFilter(path, rkey, gkey, bkey, mult, add):
    image = Image.open(path)

    pixels = image.getdata()

    new_pixels = []
    for p in pixels:
        new_pixels.append(p)

    pointer = 0
    while pointer < len(new_pixels):
        p = new_pixels[pointer]

        keydict = {
            "r": p[0],
            "b": p[1],
            "g": p[2],
            "rinvert": 255 - p[0],
            "ginvert": 255 - p[1],
            "binvert": 255 - p[2]
        }

        newr = (math.floor(keydict[rkey] * mult[0])) + add[0]
        newg = (math.floor(keydict[gkey] * mult[1])) + add[1]
        newb = (math.floor(keydict[bkey] * mult[2])) + add[2]

        new_pixels[pointer] = (newr, newg, newb)

        pointer += 1

    newImage = Image.new("RGB", image.size)
    newImage.putdata(new_pixels)

    return newImage


from PIL import Image

def discriminate(path, highColor, lowColor, highSplit, lowSplit):
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


        if ((g + r + b) // 3) <= lowSplit:
            newr = highColor[0]
            newg = highColor[1]
            newb = highColor[2]
        elif ((g + r + b) // 3) > highSplit:
            newr = lowColor[0]
            newg = lowColor[1]
            newb = lowColor[2]
        else:
            newr = r
            newg = g
            newb = b

        new_pixels[pointer] = (newr, newg, newb)

        pointer += 1
    
    newImage = Image.new("RGB", image.size)
    newImage.putdata(new_pixels)

    return newImage

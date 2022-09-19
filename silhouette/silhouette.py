from PIL import Image

def silhouette(path, split):
    image = Image.open(path).convert('RGB')

    pixels = image.getdata()
    width = image.width
    rows = image.height

    new_pixels = []

    for p in pixels:
        new_pixels.append(p)

    for row in range(rows - 1):
        l_pointer = 0

        while l_pointer <= width:
            p = width * row + l_pointer

            r = new_pixels[p][0]
            g = new_pixels[p][1]
            b = new_pixels[p][2]

            if ((r + g + b) // 3) < split:
                break
            
            new_pixels[p] = (0, 0, 0)

            l_pointer += 1
            
    for row in range(rows - 1):
        r_pointer = width - 1

        while r_pointer >= 0:
            p = width * row + r_pointer

            r = new_pixels[p][0]
            g = new_pixels[p][1]
            b = new_pixels[p][2]

            if ((r + g + b) // 3) < split:
                break

            new_pixels[p] = (0, 0, 0)

            r_pointer -= 1

    
    
    newImage = Image.new("RGB", image.size)
    newImage.putdata(new_pixels)

    return newImage

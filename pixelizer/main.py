from pixelizer import pixelize

path = 'image.png'
width = 50
height = 50
size = [width, height]

# path = input('path:')
# width = int(input('width:'))
# height = int(imput('height:'))
# size = [width, height]

image = pixelize(path, size)
image.save('pixelized.png', optimize=True)
from discriminate import discriminate

path = 'image.jpeg'
lowColor = [0, 0, 0]
highColor = [255, 255, 255]
highSplit = 100
lowSplit = 150

image = discriminate(path, highColor, lowColor, highSplit, lowSplit)
image.save('black-white.jpg', optimize=True)
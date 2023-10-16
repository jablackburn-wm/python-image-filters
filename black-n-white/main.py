from discriminate import discriminate

path = 'shaded-wfigure102.png'
lowColor = [255, 255, 255]
highColor = [0, 0, 0]
highSplit = 255
lowSplit = 100

image = discriminate(path, highColor, lowColor, highSplit, lowSplit)
image.save('black-white.jpg', optimize=True)

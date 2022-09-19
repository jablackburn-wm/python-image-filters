from discriminate import discriminate

path = 'image.jpeg'
highColor = [0, 0, 0]
lowColor = [255, 255, 255]
highSplit = 100
lowSplit = 150

# path = input()
# highColor = input()
# lowColor = input()
# midColor = input()
# highSplit = input()
# lowSplit = input()

image = discriminate(path, highColor, lowColor, highSplit, lowSplit)
image.save('black-white.jpg', optimize=True)
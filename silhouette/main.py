from silhouette import silhouette

path = 'image.jpg'
split = 150

# path = input('path:')
# split = input('split:')

image = silhouette(path, split)
image.save('silhouette.jpg', optimize=True)
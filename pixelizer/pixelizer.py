from PIL import Image

def pixelize(path, size): 

    image = Image.open(path).convert('RGB')

    image = image.resize((size[0], size[1]))

    return image

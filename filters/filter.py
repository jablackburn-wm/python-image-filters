from ambiguous_filter import ambiguousFilter
import os

def filter(origin, folder, name, mult, add, args): 
    for i in reversed(range(len(origin))):
        if origin[i] == '.':
            extension = origin[i:]

    abspath = os.path.abspath(folder)
    for keys in args:
        Image = ambiguousFilter(origin, keys[0], keys[1], keys[2], mult, add)
        Image.save(f'{abspath}/{name}_{keys[3]}_{mult}_{add}{extension}', optimize=True)




from ambiguous_filter import ambiguousFilter
import os

def filter(origin, folder, name, rmult, gmult, bmult, args): 
    abspath = os.path.abspath(folder)
    for keys in args:
        Image = ambiguousFilter(origin, keys[0], keys[1], keys[2], rmult, bmult, gmult)
        Image.save(f'{abspath}/{name}_{keys[3]}_{rmult}_{bmult}_{gmult}.jpeg', optimize=True)




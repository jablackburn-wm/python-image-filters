# Image Filters


# Summary
This is an ongoing project to create useful and unique image filters with python. Currently it a suite of color-swapping filters whick rearrange, invert, and multiply pixel values

you can choose numbers to multiply each r, g, and b pixel value by. By default these should be 1.

with constant multipliers, there are 216 filter variations. first there are 27 permutations of r, g, and b, then 27 more inverted versions of those images. Then there are 54 more filters for single/double pixel inversions, meaning only one or two of the pixel values is inverted. 

# ambiguous_filter.py
this is the base functionality behind all these filters. this file simply includes a filter function that returns the filtered image data, taking a number of arguments: 
(path, rkey, gkey, bkey, rmult, gmult, bmult)

path is the path of the image being filtered. 

rkey, gkey, and bkey correspond to the operation performed on the corresponding pixel value.
Notice there is a dictionary within the function that links strings to expressions:
    keydict = {
                "r": p[0],
                "b": p[1],
                "g": p[2],
                "rinvert": 255 - p[0],
                "ginvert": 255 - p[1],
                "binvert": 255 - p[2]
            }
the function retrieves the proper expression for each pixel value from the table based on the rkey/gkey/bkey that is passed in. 

rmult, gmult, and bmult are the multipliers applied to each pixel value. For normal behavior these should be 1.
set these between 0 and 1 to reduce the values, set them above 1 to increase them. 
Don't worry about going over 255, any number above that will resolve itself to 255. 

# Keys Guide 
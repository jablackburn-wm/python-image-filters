# Image Filters

# Summary

This is an ongoing project to create useful and unique image filters with python. 

'filters' includes functions to filter images by swapping around and manipulating the pixel values. 

'black-n-white' can be used to discriminate an image into only two colors, for instance, turning an image into only black and white. 

'pixelixer' is used to pixelate an image and/or change its aspect ratio. 

'colorizer' is used to replace a range of color values with a new color

'silhouette' is used to color the outside of a dark outline black, effectively turning it into a reverse silhouette. 


These programs are pretty old and un-polished. Most of the inputs have to be hard coded direclty into 
the "main.py" files for each program. In the revamped iteration of this project in rust, I plan to handle inputs and organizing output elegantly with the command line.


# filters

### ambiguous_filter.py

this is the base functionality behind all these filters. this file simply includes a filter function that returns the filtered image data, taking a number of arguments: 
(path, rkey, gkey, bkey, mult, add)

path is the path of the image being filtered. 

rkey, gkey, and bkey correspond to the operation performed on the corresponding pixel value.
Notice there is a dictionary within the function that links strings to expressions.
the function retrieves the proper expression for each pixel value from the table based on the rkey/gkey/bkey that is passed in. This allows for 

mult is an array of numbers by which the pixel values will be multiplied. 
mult[0] is applied to R, mult[1] is applied to G, and mult[2] is applied to B. 
set these between 0 and 1 to reduce the values, set them above 1 to increase them. 
Don't worry about going over 255, any number above that will resolve itself to 255. 

add is an array of integers which are added to the corresponding pixel value. 
The order is the same as for mult: R, G, B.

### filter.py

filter.py defines a function to iterate over an array of keys, get images from the ambiguous filter function with each set of keys, and save those images to some output folder.
the function takes 6 arguments: (origin, folder, name, mult, add, args)

origin is the path to the original image. 
folder is the path to the output folder where the filtered images will be saved.
name becomes part of the filename of the output images.
mult is the array of multipliers.
add is the array of adders. 
args is the array of keys.
### keys.py

keys.py is a file containing all the keys for filtering images. 
These keys determine how to swap and invert the pixel values according to the keydict dictionary in ambiguous_filter.py.

there are 27 permutations of RGB, each of which can be inverted a total of 8 ways:

1: R,G,B
2: R-invert, G-invert, B-invert
3: R-invert, G, B
4: R, G-invert, B
5: R, G, B-invert
6: R-invert, G-invert, B
7: R-invert, G, B-invert
8: R, G-invert, B-invert

the 27 permutations times the 8 ways to invert the values makes for a total of 216 possible variations.
The all_keys keys include all of these variations, but you can use subsets of the keys if you want.

### main.py

the main.py file is the file to execute when it comes time to filter some images. 
first you will need to specify the origin, folder, name, mult array, add array, and args array by either defining their values or typing inputs at runtime. for simplicity, store inputs in an "inputs" directory, then create a folder to hold the outputs within an "outputs" directory

# colorizer

### colorizer.py

this file houses the main functionality for colorizing images, that is, replacing a range of colors with a new color. This file exports two functions with similar purposes but different implementation:

colorize_by_tolerance(path, target, tolerance, new_color)

this function takes a target color and a tolerance array to determine which pixels will be replaced with the new color.
path is the path of the image to be colorized.
target is an array of 3 values, corresponding to the R, G, and B values of the target color.
tolerance is an array of 3 values, corresponding to the tolerances around the R, G, and B values of the target color. if a pixel value falls within these tolerances, it is replaced with new_color.
new_color is simply the new color to replace the targeted pixels.

colorize_by_range(path, high_target, low_target, new_color)

this function replaces pixels with a new color if they fall between the high and low target values. 
path is the path of the image to be colorized.
high_target is an array of 3 values corresponding to the high target color, below which all pixel values must be if they are to be replaced.
low_target is an array of 3 values corresponding to the low target color, above which all pixel values must be if they are to be replaced.
new_color is simply the new color to replace the targeted pixels.

### main.py

this is the main file used to call the colorizer functions.
specify the mode as either 'tolerance' or 'range' to specify which mode to run the colorizer in. 
If you use it in tolerance mode you must define a target value and a tolerance array, if you use it in range mode you must supply a high and low target value. 

# black-n-white

### discriminate.py

this file houses the discriminate function, which replaces pixels in an image with two colors. This can be used to turn an image to black and white. 

the function takes 5 arguments: (path, highcolor, lowcolor, highsplit, lowsplit)

path is the path of the image to be filtered. 
high and low color are arrays of 3 values representing the colors to fill in the image. 
the high and low splits are values which determine which color to replace a given pixel with.
For each pixel, the pixel values are averaged. if that average happens to be above the high split, it is converted to the high color. if the average is below the low split, it is turned to the low color. if neither are true, the pixel is left alone. setting the high and low split equal to each other ensures that all pixels are replaced. 

### main.py

this is the main file used to call the discriminate function. specify the arguments you want to use beforehand. Use an "Inputs" folder for simplicity and organization.

# pixelizer

### pixelizer.py 

this file exports a simple function which uses PIL's resize method to change the dimentions of an image and/or make it more pixelated. the path argument is the path of the image to be resized, and the size argument is an array containing the new dimentions of the image. 

### main.py

this is the main file to run the pixelizer function. specify the path, width and height before runnin it. 

# silhouette

### silhouette.py

this file houses the silhouette function, which takes two arguments: the path and the split

path is the path of the image to be filtered.
split is the target value used to stop the silhouetter.

the sihouette function goes down the image row by row, moving in from both sides turning every pixel black until it reaches a pixel whose average value is less than the split. this way, you can turn the left and right side of a black outline black. 
Honestly this program is very immature and broken; in the future I'd like to re-create this program utilizing the flood fill algorithm.

### main.py 

this is the main file to run the silhouette function from. specify the path and the split before running it.

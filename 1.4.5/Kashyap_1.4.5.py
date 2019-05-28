from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path  
import PIL
import PIL.ImageDraw            

def round_corners_one_image(original_image, percent_of_side=.3):
    """ Rounds the corner of a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with rounded corners, where
    0 < percent_of_side < 1
    is the corner radius as a portion of the shorter dimension of original_image
    """
    #set the radius of the rounded corners
    width, height = original_image.size
    radius = int(percent_of_side * min(width, height)) # radius in pixels
    
    ###
    #create a mask
    ###
    
    #start with transparent mask
    rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    
    # Draw two rectangles to fill interior with opaqueness
    drawing_layer.polygon([(radius,0),(width-radius,0),
                            (width-radius,height),(radius,height)],
                            fill=(127,0,127,255))
    drawing_layer.polygon([(0,radius),(width,radius),
                            (width,height-radius),(0,height-radius)],
                            fill=(127,0,127,255))

    #Draw four filled circles of opaqueness
    drawing_layer.ellipse((0,0, 2*radius, 2*radius), 
                            fill=(0,127,127,255)) #top left
    drawing_layer.ellipse((width-2*radius, 0, width,2*radius), 
                            fill=(0,127,127,255)) #top right
    drawing_layer.ellipse((0,height-2*radius,  2*radius,height), 
                            fill=(0,127,127,255)) #bottom left
    drawing_layer.ellipse((width-2*radius, height-2*radius, width, height), 
                            fill=(0,127,127,255)) #bottom right
                         
    # Uncomment the following line to show the mask
    # plt.imshow(rounded_mask)
    
    # Make the new image, starting with all transparent
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    result.paste(original_image, (0,0), mask=rounded_mask)
    return result
    
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

def round_corners_of_all_images(directory=None):
    """ Saves a modfied version of each image in directory.
    
    Uses current directory if no directory is specified. 
    Places images in subdirectory 'modified', creating it if it does not exist.
    New image files are of type PNG and have transparent rounded corners.
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    # Load all the images
    image_list, file_list = get_images(directory)  

    # Go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        print(n)
        filename, filetype = os.path.splitext(file_list[n])
        
        # Round the corners with default percent of radius
        curr_image = image_list[n]
        new_image = round_corners_one_image(curr_image) 
        
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)

#1-4 N/A
#5. round_corners_of_all_images(), get_images(), round_corners_one_image() are 
    #the three methods that have been declared but have never been called.
#6. It created a new folder. The folder contains all the modified images 
#7a. 2 arguments
    #Argument 1: original image object of the class PIL.Image
    #Argument 2: percent of side is an integer that determines the border-radius of a specific image
    #Result: Returns PIL.Image object
#7b. It creates a transparent purple color.
#7c. rouded_mask and drawing_layer
#7d. We want the mask in the corners to be zero because we don't want it to appear.
#7e. 33-38 = the image with the rectangles. 41-48 = the image with ellipses.
#7f. The color is a transparent black.
#7g. The color in the corners are (0, 0, 0, 0) (Black transparent)
#8a. 1 or 0 arguments
#8b. Returns two lists. The first one is made up of PIL.Image objects and the 
    #second list returns a list of strings containing the names of the image files
#8c. os.getcwd(), os.listdir(directory), os.path.join(directory, entry)
#8d. Return a list containing the names of the entries in the directory given by
    #path. The list is in arbitrary order, and does not include the special 
    #entries '.' and '..' even if they are present in the directory.
#8e. They do this because they don't any Filename exceptions popping up which 
    #can completely halt the program. Instead they could execute another block of code.
#8f. If it raises an error, lines 80 and 81 allow the code in the catch block 
    #to execute. In this case it is pass so the program is not halted.
#9a. If the user does not provide a valid directory and/or it already exists in 
    #the specific parent directory
#9b. It represents the length of the list and how many elements are inside of it.
#9c. It is the specific index that the for loop is at at a specific moment in time. 
    #It allows you to perform methods on specific elements on the list.
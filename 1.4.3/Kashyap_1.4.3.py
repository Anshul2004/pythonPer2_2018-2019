from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import PIL
import numpy as np      # 'as' lets us use standard abbreviations

#Procedure: 1-3

#Part I: Using Arrays of Pixels

#4. Arrays can store elements of only one type while lists can store elements of
    #different data types. Both lists and arrays can store multiple objects.

#5.
'''
#Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

#Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Saves the figure
fig.savefig('women2')
print(type(img))
print(img[49][24][0])
print(len(img))
print(len(img[0]))
'''
#a. 943 pixels
#b. 574 pixels
#c. 94
#d. 62
#e. 73

#Part II: Manipulating Pixels

#6.
'''
###
# Make a rectangle of pixels yellow
###

#Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

#Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')

height = len(img)
width = len(img[0])
for row in range(420, 450):
    for column in range(140, 160):
        img[row][column] = [0, 255, 0] # red + green = yellow
fig.savefig('green_earing')
'''

#7.
'''
#Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')

img = plt.imread(filename)

#Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
'''
###
# Change a region if condition is True
###
'''
height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta
fig.savefig('woman_sky_earing')
'''
###
# Show the image data
###
    #7a. This set of loops and conditionals check to see if a certain pixel is
    #bright or not based on its rgb value. If it is then it changes the color magenta
    #7b. 
'''
#Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')

img = plt.imread(filename)

#Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta
for row in range(420, 450):
    for column in range(140, 160):
        img[row][column] = [0, 0, 255] # red + green = yellow
        
ax.imshow(img, interpolation='none')

fig.savefig('woman_sky_earing')
'''
#8. 
'''
def make_mask(rows, columns, stripe_width):
    An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns
    
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    
    for row in range(rows):
        for column in range(columns):
            if (row-column)/stripe_width % 2 == 0: 
                #(r+c)/w says how many stripes above/below line y=x
                # The % 2 says whether it is an even or odd stripe
                
                # Even stripe
                image[row][column] = [255, 127, 127, 250] # pale red, alpha=0
            
            else:
                # Odd stripe
                image[row][column] = [200, 200, 255, 255] # magenta, alpha=255
    
    for row in range(rows):
        for col in range(columns):
            if 500 == ((row-50)**2)+((col-50)**2):
                image[row][col] = [255, 127, 127, 250] # pale red, alpha=0
            elif 100 == ((row-50)**2)+((col-50)**2):
                image[row][col] = [255, 127, 127, 250] # pale red, alpha=0
    return image
    
if __name__ == "__main__":
    image = make_mask(100,100,20)
    
    fig, ax = plt.subplots(1, 1)
    ax.imshow(image)
    fig.savefig('mask') 
'''

#9.

directory = os.path.dirname(os.path.abspath(__file__)) 
filename = os.path.join(directory, 'woman_sky_earing.png')
filename2 = os.path.join(directory, 'mask.png')
img = plt.imread(filename)
img2 = plt.imread(filename2)

fig, ax = plt.subplots(1, 2)
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img2, interpolation='none')

fig.savefig("woman_and_mask");
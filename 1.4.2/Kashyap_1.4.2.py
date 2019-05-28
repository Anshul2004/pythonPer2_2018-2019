#Import statements
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

#1-3 NA

'''Part I: Working with a Filesystem'''
#4. C:/Users/Studentlogin/Desktop/nice.jpg is the absolute filename

#5. ../Studentlogin/Desktop/nice.jpg is the relative filename

#6. In the cloud 9 workspace, it is storing th information on the cloud 9 server
    #while C:/ shows that it is being stored on the local disk 

#6b. 

'''Part II: Rendering an Image on Screen:'''
#7. This runs without any errors. This is because cloud 9 is a non-GUI environment
    #which means that it won't allow us to see the image unless we save it to 
    #another image file without enabling GUI methods
    
    #a. The coords are (300, 400)
    #b. The coords are (60, 40)
'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
'''
Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat.gif')
# Read the image data into an array
img = plt.imread(filename)

Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('cat_plot.png')
'''

'''Part III: Objects and Methods'''
#8. fig is an object of the class Figure. ax is an object of the class AxesSubPlot
#8b. savefig(), fig, one argument, Figure
#8c. Multiple comments before each lin of code are used above to isolate groups 
    #of methods that focus on a certain tasks

'''Part IV: Arrays of Objects'''
#9a. The method imshow() is being called on the object ax[0] which is the first element in the ax array

'''
Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat.gif')
# Read the image data into an array
img = plt.imread(filename)

Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 5)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
ax[2].imshow(img, interpolation='none')
ax[3].imshow(img, interpolation='none')
ax[4].imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('cat_five')
'''
#9b. N/A

'''Part V: Keyword = Value Pairs'''
#10. Interpolating is being used to make the rigid color transitions between 
    #specific pixels go away to make a smoother transition. The library infers 
    #the colors between pixels
    
#11a.
'''
#Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat.gif')
# Read the image data into an array
img = plt.imread(filename)

#Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
ax.set_xlim(0, 100)
ax.set_ylim(100, 0)
# Show the figure on the screen
# fig.show()
fig.savefig('experiment')
'''

#11b.
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
fig, ax = plt.subplots(1, 3)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
ax[2].imshow(img, interpolation='none')
ax[0].set_xlim(0, 10)
ax[0].set_ylim(10, 0)
ax[1].set_xlim(10, 20)
ax[1].set_ylim(20, 30)
ax[2].set_xlim(20, 30)
ax[2].set_ylim(30, 40)
# Show the figure on the screen
# fig.show()
fig.savefig('three_closeup')
'''
#12. The matshow(M, N). This method is a wrapper method for imshow() which is 
    #useful for displaying matrices

#13. 
#Read the image data
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'mouse.jpg')
# Read the image data into an array
img = plt.imread(filename)

#Show the image data
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
plt.plot(38, 48, "ro")
plt.plot(138, 42, "ro")
plt.plot(115, 42, "ro")
# fig.show()
fig.savefig('crazy_mice')
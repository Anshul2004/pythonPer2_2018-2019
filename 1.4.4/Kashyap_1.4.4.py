#Procedure 9-12

#13.
    #matplotlib.pyplot - Allows the user to save images/manipulated images.
    #numpy - a math library that allows you to perform complex mathematical operations.
    #PIL - Python Imaging Library allows user to perform a series of methods on 
        #a specific image to manipulate it.
#14. N/A

#15a. subplots() from the matplotlibs library. This function is being called with
    #two arguments. The function returns two objects which are being assigned to
    #the fig and ax objects
#15b. imshow() in ax[1]
        #set_xticks() on ax[1]
        #set_xlim() on ax[1]
        #set_ylim() on ax[1]
        #savefig() on fig
#15c. The coordinates are (1162, 966)

#16a. Top-left: (966)1162, 
        #Top-right: (1253, 966)
        #Bottom-left: (1162, 1059)
        #Bottom-right:(1253, 1059)
        #Width: 89
        #Height: 87
        
#17a. 2 arguments, earth_file
#17b. earth_img
#17c. There could be more then one inputted paramtr. One of these paramters is 
    #a tuple for the x and y coordinates
#17d. Provides the height and width of the image
#17e. N/A
#17f. 
    #i. The other parameter you can pass in is filter
    #ii. It is NEAREST
    #iii. It is ANTIALIAS
#17g. The width and height of the given PIL object image
#17h. The first print statement orints out the width and height of the earth_img
    #image in a tuple. The second print statement prints out the width and height
    #of the earth_small image in a tuple as well. The third print statement 
    #prints out the width of the img object.
#17i. One of the images looks more pixelated which means that it contains less 
    #pixels since interpolation is turned off.

#18. Reize performs average/mean operation to find the average pixel value of a 
    #given area

#19a. Student_img bytes = 15667200
	#Earth_small bytes = 30972

#19b. N/A

#19c. Student.jpg bytes =  211,546
    #smallEarth.png bytes = 18,774

#19d. The computer compresses the file which is why the byte count is so small 
    #when we look at the image properties. But when we caluclated it, it took 
    #all the data into consideration. 

#19e. If a color is used as the first argument, it uses that specific color as 
    #the mask instead of a desired image input.

#19f. The pasted image is converted to the mode of the given image

#19g. The first parameter is the image to be pasted, the second is the tuple 
    #location, the third is what specific mask to use when pasting that image
#20. N/A
import random

'''Procedure'''
#1-3 N/A

'''Part 1: Tuples, Syntax'''
#4. (5, 6, 7)

#5. Each section should have a specific header and labeled question numbers. All
    #caps for fixed vars and camelCase for mutable vars.

#6a. There are three elements in the tuple which means that the indexes we have 
    #to use are 0, 1, and 2. This will return 'b' since the second element in 
    #the tuple is 'b'

#6b. This will return ('a', 'b') since the beginning bound which is inclusive is
    #the first element in the tuple which is 'a' and the closing bound which is 
    #exclusive is returning all the elements in the tuple except the last one.
    
#7a. This will return True since the secnd eement in the tuple is 10 and the 
    #'==' returns a boolean since you are not assigning any var.

#7b. This will return 15 since the value of a was changed to 15 after assigning 
    #the original tuple to (9, a, 11) when the value of a was 10

'''Part 2: Lists'''
#8. This will output ['b', 3] since the beginning index is 1 which means that it
    #will start of with the second element in the list. Since there is no upper 
    #bound, it will return a list with all the elements within the first and 
    #last elements inclusive.

#9. This will return False since the string '3' is not of the same data type as 
    #the integer 3.

#10a. Returns the list with the elements 4 and 5 appeneded at the end of the 
    #list.

#10b. This returns values with the list [6, 7] appeneded as one element at the 
    #end of it.

#11. This is because you cannot add or concatenate objects of different data
    #types. In this case, 5 is an integer while values is a list with multiple 
    #objects inside of it.

#12. This will return 18 since you are multiplying the value of a by three and 
    #putting the result within a again. 6 times 3 is 18 so the value f a is now 
    #18.

'''Part 3: Lists and the random module'''
#13. N/A

#14. 
def roll_two_dice():
    '''
    Parameters: None
    Returns: the sum of val1 and val2 which are two random integers between 1 
    and 6 inclusive.
    '''
    val1 = random.randint(1,6)
    val2 = random.randint(1,6)
    return val1 + val2

'''Conclusion'''
#1. a is a string, b is a tuple, c is a list

#2. It doesn't give the programmer a lot of power and it limits the things we 
    #can do. With a large amunt of data types, programmers can make a variety of
    #applications that are unique and different.

#3. Python is a very useful programming language that with its large data type 
    #set and available libraries/modules allows programmers to make a variety of
    #applications. Python allows the user to create functions to encapsulate 
    #blocks of code that might be used multiple times throughout the file. 
    #Python also allows the user to run certain blocks of code using 
    #conditionals. Python also allows the use to store multiple objects in 
    #tuples and lists. Python allows programmers to iterate through strings, 
    #tuples, and lists.

#1.3.6 Function Test
print(roll_two_dice())

#Reflection

#The function test outputted the expected value which was an integer between 2 
    #and 12 inclusive. Based on these results, I believe that I have succesfully
    #completed this assignment.
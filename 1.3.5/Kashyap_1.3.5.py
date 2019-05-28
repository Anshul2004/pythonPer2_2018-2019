from __future__ import print_function

'''Procedure'''
#1-4 N/A

#5. The integer, long, and float data types can represent six million

#6. The second one: type('tr' + 5), because you cannot concatenate a string and 
    #integer. Both data types have to be the same if you are concatenating or 
    #adding them.
    
#7. slogan[-7] outputs the seventh to last character in the string. It should 
    #output 'h'

#8. slogan[17:] will slice slogan to output 'best'

#9. slogan[:13] + 'cool' will output My school is cool

#10a. This will output 7 since there are seven characters in the string
#10b. This will output 'theate' since it starts at the beginning since the front
    #bound is 0 and ends one character before the actual length of the string 
    #which is why the string is missing one character.

#11. This returns true since the string 'test goo' is within the string being 
    #checked which means that the consition has been met.

#12.
def how_eligible(essay):
    '''
    Parameters: essay -> string
    Function creates a local var eligibility and increments it by one every time
    a specific condition is met. Used to check the 'eligibility' of the inputted
    string
    Returns: eligibility -> int value that represents eligibility
    '''
    eligibility = 0
    if '?' in essay:
        eligibility += 1
    if '!' in essay:
        eligibility += 1
    if ',' in essay:
        eligibility += 1
    if '"' in essay:
        eligibility += 1
    return eligibility

#1.3.5 Function Test
print(how_eligible('This? "Yes." No, not really!'))
print(how_eligible('Really, not a compound sentence.'))

#Reflection

#The function test outputted the expected values which were 4 and 1. Based on 
    #these results, I believe that I have succesfully completed this assignment.
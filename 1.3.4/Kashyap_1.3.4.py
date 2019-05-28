from __future__ import print_function # must be first in file 
import random


'''Procedure'''
#1-4 N/A

'''Part 1: Nested if structures and testing'''
def food_id(food):
    ''' 
    Returns categorization of food
    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'
#1a. 'NOT Citrus, Fruit' is the output the console provides
#1b.
  #i. 'orange' is the required input paramter to execute line 15
  #ii. 'apple' or 'banana' are the required inputs to execute line 17
  #iii. 'potato' is the required input parameter to execute line 20
  #iv. anything except 'apple', 'banana', 'orange', and 'potato'
#1c. This is because the first condition is met if banana is inputted which 
  #means that the alternate condition is not run. Line 20 is dependent on the 
  #whether or not the condition is met on line 13

#2. 
def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not 
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()' 
    # Add tests so that all lines of code are visited during test
    if food_id('potato') != 'Starchy, NOT Fruit':
        works = 'potato bug in food id()'
    if food_id('almond') != 'NOT Starchy, NOT Fruit':
        works = 'almond bug in food_id()'
        
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False

#3.
def f(n):
    '''
    Parameters: n -> Any data type
    This function utilizes multiple conditionals to check if n is a certain data
    type and to determine certain properties of it as well.
    Print statements are displayed depending of whether or not certain 
    conditions are met.
    Returns: Nothing
    '''
    if int(n) == n:
        if n% 2 == 0:
            if n% 3 == 0:
                return "n is an even integer that is a multiple of 6"
            else:
                return "n is an even integer"
        else:
            return "n is an odd integer"
    else:
        return "n is not an integer"

#4.
  #Input a string to make sure that the first condition is met.
  #Input 3 to make sure that the condition that checks if the number is even is 
    #tested
  #Input 4 to make sure that the condition that checks if the number is a 
    #multiple of 3 is tested
  #Input 6 to make sure that the condition that checks if the number is a 
    #multiple of 3's alternate condition is tested

#5.
def f_test():
    ''' Unit test for f()
    returns True if good, returns False and prints error if not 
    good
    '''
    works = True
    if f(3.5) != 'n is not an integer':
        works = 'float bug in f()'
    if f(3) != 'n is an odd integer':
        works = 'odd bug in f()'
    if f(4) != 'n is an even integer':
        works = 'even bug in f()'
    if f(6) != 'n is an even integer that is a multiple of 6':
        works = 'even and % 6 bug in f()'
    
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False

'''Part 2: The raw_input() function, type casting, and print() from Python 3'''
#7. + as a concatanation creates or replaces a string with 2 or more string 
  #objects. Depending on the order in which the strings are concatanated, a 
  #certain string might be appended in the beginning or the end. When using + to
  #add numerical values, + is used as a mathematcial operator and not as a 
  #concatenator. The values of the two integer or float types are mathematically
  #added.
 
#8a. In line 11, the print statement has 3 arguments: 2 strings and a 
  #keyword=value pair. This is print(s1, s2, end='!\n'). If end='!\n' was not 
  #there, the statement would print 3 strings seperated by spaces with a new 
  #line being created after printing the strings. The input begins on the line 
  #after the print command's statement is done printing (with an exclamation 
  #point at the end). If "end" was equal to "", then the input would continue on
  #the same line as the print command's statement.
    
    
#8b. 
def guess_once():
    '''
    Parameters: none
    Method that requests user input and uses conditionals to respond based on 
    the what was inputted.
    Return: none
    '''
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4.')
    guess = int(raw_input('Guess: '))
    if guess != secret:
        if guess > secret:
            print("Too high, my number was ", secret, end='!\n', sep="")
        else:
            print("Too low - my number was ", secret, end='!\n', sep="")
    else:
        print('Right on! I was number ', guess, end='!\n', sep="")

#9.
def quiz_decimal(low, high):
    '''
    Parameters: low, high -> float or integer values that are used as bounds by 
    this function to print certain statements if certain conditions are met
    Method checks if guess is within bounds. Prints certain statements if 
    specific conditions are met or not met
    Return: none
    '''
    guess = float(raw_input('Type a number between ' + str(low) + ' and ' + 
    str(high) + ': '))
    if guess > low and guess < high:
        print('Good!', low, '<', guess, '<', high)
    elif guess > high:
        print('No,', guess, 'is greater than', high)
    elif guess < low:
        print('No,', guess, 'is less than', low)
    elif guess == high:
        print('No,', guess, 'is equal to', high)
    else:
        print('No,', guess, 'is equal to', low)

'''Conclusion'''
#1. Glass box testing is used to check conditionals and to make sure that 
    #branching works in a given function.
#2. Only one block executes as long as the conditionals nested within the 
    #function are linked. The computer can travel through one path to execute a 
    #certain command at the end of the path.
#3. Test suites allow programmers to test their functions and make sure that 
    #everything is working and should be working. By doing it prior to making 
    #the function, you make a set of requirements that the function must posses.
#4. Yes you could

def isInteger(n):
    '''
    Parameters: n -> Float or Integer data type
    Calls set of functions to check if the parameter satisfies the given 
    conditionals. 
    Return: Nothing
    '''
    if int(n) != n:
        print('n is not an integer')
    else:
        even(n)
        
def even(n):
    '''
    Parameters: n -> Integer data type
    Calls set of functions to check if the parameter satisfies the given 
    conditionals. Prints statements to print if certain conditions are met. If 
    the # is even
    Return: Nothing
    '''
    if n % 2 == 0:
        multiple(n)
    else:
        odd(n)
        
def odd(n):
    '''
    Parameters: n -> Integer data type
    Calls set of functions to check if the parameter satisfies the given 
    conditionals. Prints statements to print if certain conditions are met. If 
    the # is odd
    Return: Nothing
    '''
    if n % 2 != 0:
        print('n is an odd number')
    else:
        even(n)
        
def multiple(n):
    '''
    Parameters: n -> Integer data type
    Calls set of functions to check if the parameter satisfies the given 
    conditionals. Prints statements to print if certain conditions are met. If 
    the # is a multiple of 6 or if it's not
    Return: Nothing
    '''
    if n % 3 == 0:
        print('n is a multiple of 6')
    else:
        print('n is an even number')

'''Challenge'''
def f_challenge(n):
    '''
    Parameters: n -> Integer data type
    Calls set of functions above
    Return: Nothing
    '''
    isInteger(n)
        
#1.3.4 Function Test
print(food_id('apple'))
food_id_test()
f(1.1)
f(2)
f(3)
f(6)
f_test()
guess_once()
guess_once()
quiz_decimal(4, 4.1)
quiz_decimal(4, 4.1)
f_challenge(1.1)
f_challenge(2)
f_challenge(3)
f_challenge(6)
        
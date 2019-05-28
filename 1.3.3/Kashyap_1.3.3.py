from __future__ import print_function # use Python 3.0 printing

'''Procedure'''
#1-5 N/A

'''Part 1: Conditionals'''
#6a. This returns true since the first part returns true and the second part 
  #returns true as well. Since the compound keyword being used is and, the final 
  #out put is true since true and true is true. My predictions were correct.
#6b. This will return true since both conditions in this compund conditional 
  #return true and since the compound keyword being used is or, true or true 
  #returns true. My predictions were correct.

#7. 40 < x and x < 130 and 100 < y and y < 120

#8. x, y = (90, 115)

'''Part 2: if-else structures and print() functions'''
#9a. I predict that the first function call with 10 as the inputed parameter
  #will print "10 is below the age limit." and the second function call will
  #print "16 is old enough". After each function call, the console should also 
  #output " Minimum age is 13"

def age_limit_output(age):
    '''Parameters: age -> Integer
    Conditional checks if age is < 13. 
    Prints statements depending on whether or not condition is made
    Does not return anything'''
    AGE_LIMIT = 13          # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print(' Minimum age is ', AGE_LIMIT)
    
#9b.
def report_grade(percent):
    '''Parameters: percent -> Integer
    Conditional prints depending on whether or not the percent value is < 80
    Does not return anything'''
    if percent < 80:
        print("A grade of " + str(percent) + " does not indicate mastery.")
        print("Seek extra practice or help.")
    else:
        print("A grade of " + str(percent) + " indicates mastery.")
        print("Keep up the good work!")
        
'''Part 3: The in operator and an introduction to collections'''
#10a. True
#10b. False

#11.
def letter_in_word(guess, word):
    '''Parameters: guess -> string, word -> string
    Conditional to check if character is in the given word
    Returns bolean value depending on whether the letter is in the word'''
    if guess in word:
        return True
    return False

#12.
def hint(color, secret):
    '''Parameters: color -> string, secret -> array od strings
    Conditional to print text to console depending on whether or not color 
    string is in array
    Does not return anything'''
    if color in secret:
        print("The color red IS in the secret sequence of colors.")
    else:
        print("The color green IS NOT in the secret sequence of colors.")

'''Conclusion'''
#1. "if" allows block to run if condition/conditions are met. If it's not met, 
  #it branches to the "else" or "elif". "elif" allows block to run if the first 
  #condition for the "if" is not met and the condition in the "elif" is met as 
  #well. "else" runs the block if all prior conditions are not met.
  
#2. ==, >=, <=, >, <, !=, or, and, not, is, is not, in, not it are some examples
  #of boolean operators in python
  
#3. Ira: Ira is not correct because the print statement is still only executed 
  #once which means that the amount of time it takes to compile and run the 
  #program is still the same.
    #Jayla: Jayla is correct because that print statement is going to execute 
  #inevitably so it will save time if you keep track of only one instance of 
  #it.
    #Kendra: Kendra is correct because the program will have less lines of code 
  #but still perform the same tasks which means that it saves memory for the 
  #same output.

#1.3.3 Function Test
age_limit_output(10)
age_limit_output(16)
report_grade(79)
report_grade(85)
print(letter_in_word('t', 'secret hangman phrase'))
secret = ['red','red','yellow','yellow','black']
hint('red', secret)
hint('green', secret)
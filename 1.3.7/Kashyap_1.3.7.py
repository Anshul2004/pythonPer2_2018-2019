from __future__ import print_function
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random

#Procedure 1-3

#Part I: for loops, range(), and help()
#4.
def days():
    ''' Two for loops, the first one iterates through the string 'MTWRFSS' and 
    prints the current character concatanated with the word 'day', the second
    one iterates through the numbers between 5 and 8, 5 inclusive and 8 exclusive
    '''
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')

#5.
def picks():
    a = [] # make an empty list
    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list]
    #    random.choice(   [brackets here to choose from a list])

    a += [random.choice([1, 3, 10])]
    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.savefig('1.3.7/pick_s')
    
#6a.
def roll_hundred_pair():
    '''Parameters: None
    This function creates a histogram with the data values of a hundred random 
    summed 6-sided dice values
    Return: None
    '''
    a = []
    for _ in range(100):
        a += [random.randint(1, 6) + random.randint(1, 6)]
        
    plt.hist(a)
    plt.savefig('1.3.7/hundre_d')
#6b.
def dice(n):
    '''
    Parameters: n -> Integer var that is used to define the number of dice are 
    supposed to be rolled
    This function utilizes the randint 
    Returns: The SUM of all the dice rolls
    '''
    sum = 0
    for i in range(n):
        sum += random.randint(1, 6)
    return sum

#Part II: While loops
#7. If line 2 wasn't their then the value you're trying to check wouldn't be 
    #there You have to initialize it to a certain value so that you can check 
    #if that exists in a certain string to allow the while lop to run
def validate():
    '''Parameters: None
    This function uses raw input to take a guess from the user and check if it 
    is in a certain keyword
    Return: None
    '''
    guess = '1' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')
    
#8.
def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''Parameters: Optional but default value is a tuple of the list of names 
    above. Can input tuple of strings as parameters.
    This function gets raw input from the user and checks if that specific input
    is in the paramaters inputted tuple.
    Return: The number of guesses that the user makes until the user guesses 
    correctly
    '''
    winner = random.choice(players) 

    ####
    # This function prints out the list of names of the possible choices the 
    #user can make
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: #The first through 2nd to last index
        print(p+', ', end='')
    print(players[len(players)-1]) #Prints the last item in the players tuple

    ####
    # Uses a while loop to make a reccurent sequence to constantly get user 
    # input from the user until the user gets it correct. Returns the number of
    # guess it took to properly guess
    ####
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses    
    
#9.
def goguess():
    '''Paramaters: None
    This function uses a loop to constantly get input from the user and prints 
    statements depending on whether or not it is too high or too low
    Return: None
    '''
    print("I have a number between 1 and 20 inclusive.")
    
    num = random.randint(0, 20)
    guess = raw_input("Guess: ")
    guess_num = 1
    while guess != str(num):
        if int(guess) > num:
            print(str(guess) + " is too high.")
        else:
            print(str(guess) + " is too low.")
        guess_num += 1
        guess = raw_input("Guess: ")
    print("Right! My number is " + str(guess) + "! You guessed in " + 
    str(guess_num) + " guesses!")

#10. It depends on where the number is between 1 and 6000. The number of guess 
    #can either be the (number-1)/2 or (6000-num)/2

#Part III: Practice
#11a.
def matches(ticket, winners):
    '''Parameters: Two arrays, lists, or tuples expected to have the same number
    of elements and the elements have to be of the same data type
    This function uses a for loop to 
    Return: The integer value which represents the number of elements ticket and
    winners have in common
    '''
    common = 0
    if len(ticket) == len(winners):
        for i in range(len(ticket)):
            if ticket[i] == winners[i]:
                common += 1
    else:
        print("The length of winners did not match the length of ticket")
        return
    return common

#11b.
def report(guess, secret):
    '''Parameters: two lists, tuples, or arrays with string elements that are 
    expected to have color names as the elements
    This function uses loops to iterate through guess and secret and update the 
    same and different vars based on specific conditionals
    Return: A list with two elements, the number of color that are in the same 
    position in both secret and guess, and the number of colors that are 
    different in each of the paramaters
    '''
    same = 0
    different = 0
    if len(guess) != len(secret):
        return
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            same += 1
    for i in guess:
        if i not in secret:
            different += 1
    return [same, different]
        
#Conclusion
#1. If there are say 1000 iterations, to rewrite that code over and over again 
    #can be extremely inefficient and a waste of time as well. As the number of 
    #iteration goess higher so does the effort to actully write the code

#2. You can analyze relationships between datasets by iterating through them 
    #using loops such as a for or while loop
    
#3. A while loop just rechecks a conditional and doesn't rely on a iterative 
    #stepper while a for loop need something to iterate through a dataset
    
#4. I did not work with my partner as we could not get in contact during the 
    #weekend. I feel like I was able to efficiently get this assignment done by 
    #myself.

#1.3.7 Function Test
days()
picks()
roll_hundred_pair()
validate()
guess_winner(players=("Anshul", "Aarav", "Pradeep", "Swaroopa"))
goguess()
print(matches([1, 2, 3, 4, 5], [1, 3, 3, 2, 5]))
print(report(['red','red','red','green','yellow'], ['red','red','yellow','yellow','black']))
#The function test outputted the expected values. I believe that this shows that
    #I have succesfully completed the project. I also feel like this was succesful
    #because I was able to finish it in an efficient amount of time
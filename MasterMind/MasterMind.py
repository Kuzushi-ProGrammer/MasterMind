# Randomly generates a number consisting of three digits                            (DONE)

# Code words 'Green', 'Yellow', and 'Red' will be used to evaluate a guess          (DONE) (GRY COMBO BUGGY)
# Green = Correct number, Correct position (Doesn't specify)                        
# Yellow = Correct number, Wrong position               
# Red = Wrong number, Wrong position

# All green = Win condition                                                         (DONE)
# Greens always appear first (for animosity)                                        (DONE)
# Only one colour is presented for each number                                      (DONE) (GRY EXCEPTION)   

# Ex. (number is 123): 213 - Green (for the 3), Yellow, Yellow

# Import random library (for num gem)                                               (DONE)
# Need ability to hardcode number (for testing purposes)                            (CAN COMMENT OUT RANDOM AND USE INT INSTEAD)

# -------------------------------------------------------------------------------------------- # IMPORTING AND EXAMPLES #
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset = True)

''' # - Colour testing - #
print(Fore.RED + 'bitch')           # Turns text red   (ONLY WORKS IN THE .PY EXECUTABLE)
print(Back.CYAN + 'cyan')           # Highlights the font (essentially a backlight)
print(Style.BRIGHT + 'my eyes')     # Makes text bright
print(Style.DIM + 'dark')           # Makes text dim
 '''

import random

# ans = int(100)                         # For debugging purposes (I had it set on 123 for most of my testing)
ans = random.randint(100, 999)      # Generating random int
Correct = False                     # For the while loop to function, used so I can account for 000 later on (me realizing I actually dont have to do that but did anyway)
num = 0                             # Setting initial value of num
GuessCount = 1                      # Guess tracker integer
Redone = False                      # These three are for detecting if I should print 'Red'
Redtwo = False
Redthree = False
zero = True

G = (Fore.GREEN + 'Green')          # Adding some colour to make it stand out
Y = (Fore.YELLOW + 'Yellow')
R = (Fore.RED + 'Red')

# print(ans)                          # I would have it print the answer at the top of each debug

# -------------------------------------------------------------------------------------------- # CONTEXT #
print("Welcome to MasterMind! It's a nice little guessing game where you pick a 3 digit number and i'll tell you how close you are!")
print("All the digits are in between numbers 1 and 9, so don't go using any zeros!")
print(G + " = Correct number, Correct location, But I won't tell you which one it is!")
print(Y + " = Correct number, Wrong location!")
print(R + " = All the numbers in the combination are wrong, try again!")
print('')

answer = str(ans)                               # I use this chunk of code three times, one for declaration, and once for each loop
answer1 = answer[0:1]                      
answer2 = answer[1:2]
answer3 = answer[2:3]

while (zero == True):                           # Re-rolling ans if any of the numbers equals zero
    answer = str(ans)                             
    answer1 = answer[0:1]                     
    answer2 = answer[1:2]
    answer3 = answer[2:3]
    if (answer1 == '0' ) or (answer2 == '0') or (answer3 == '0'):
        ans = random.randint(100, 999)

    else:
        zero = False

# -------------------------------------------------------------------------------------------- # MAIN LOOP # 
while Correct is False:
    Guessnum = ('Guess #{}!: ').format(GuessCount)              # Formats message to amount of times guessed
    num = input(Guessnum)                                       # Takes input
    print('')
    Redone = False                                              # Sets booleans to false every loop so it doesn't only assign it once or get all weird
    Redtwo = False
    Redthree = False
    numpos = ''                                                 # Sets strings in variables to empty so it doesn't fail later and resets with every loop
    numpos2 = ''
    numpos3 = ''

    try:
        num = int(num)                                          # Checks if input can be converted to integer
        if((int(num) <= 999) and (int(num) >= 100)):            # If num is equal to or less than 999 and greater than or equal to 100 to keep the number three digits
            GuessCount += 1
            try:
                numstr = str(num)                               # Converts input number to a string
                numstr1 = numstr[0:1]                           # Splits the string into segments to be used later
                numstr2 = numstr[1:2]
                numstr3 = numstr[2:3]                     

                answer = str(ans)                               # Converts randomly generated answer into a string 
                answer1 = answer[0:1]                           # Splits the string into segments for comparison against input
                answer2 = answer[1:2]
                answer3 = answer[2:3]

# ------------------------------------------------------------------------------------------ # Answer checks #                                   
                try:                          # Answer number one   
                    if (answer1 == numstr1):                                                                        # If the input is equal to the answer in that position, set numpos to green
                        numpos = ('Green')                 
                    elif (answer1 == numstr2) or (answer1 == numstr3):                                        # If the input is equal to one of the other two answers, set numpos to yellow
                        numpos = ('Yellow')                     
                    elif (answer1 != numstr1) and (answer1 != numstr2) and (answer1 != numstr3):          # If none of the input numbers equal any of the answers set numpos to red
                        numpos = ('Red')                      
                        Redone = True                                                                   # Setting boolean to true for later output if it's red

                except:
                    print('e')
# ------------------------------------------- # Answer number two
                try:                                                                         
                    if (answer2 == numstr2):                                                                        # Same thing but for second and third positions respectively
                        numpos2 = ('Green')
                    elif (answer2 == numstr1) or (answer2 == numstr3):
                        numpos2 = ('Yellow')
                    elif (answer2 != numstr1) and (answer2 != numstr2) and (answer2 != numstr3):
                        numpos2 = ('Red')
                        Redtwo = True
                except:
                    print('c')
# -------------------------------------------- # Answer number three
                try:
                    if (answer3 == numstr3):
                        numpos3 = ('Green')
                    elif (answer3 == numstr1) or (answer3 == numstr2):
                        numpos3 = ('Yellow')
                    elif (answer3 != numstr1) and (answer3 != numstr2) and (answer3 != numstr3):
                        numpos3 = ('Red')
                        Redthree = True
        
                except:
                    print('a')

            except:
                print('>:(')

# ---------------------------------------------------------------------------------------------- # SORTING #
            try:
                results = (numpos + numpos2 + numpos3)                                                          # Takes all three number positions and preps for sorting
                sortedresults = sorted(results)                                                                 # Sorts letters (automatically creates list somehow?)                     
                joinedresults = ''.join(sortedresults)                                                          # Gets rid of the pesky list

                strippedresults = joinedresults.strip('R e d r e n l o w')                                      # Removes all unnecessary characters (It should only leave G and Y)

                if (Redone is True) and (Redtwo is True) and (Redthree is True):                                # Uses the bools from earlier to determine if it should print red or not
                    print(R)

                elif strippedresults == 'G':                                                                    # All possible outcomes at this point are covered because there's only 8
                    print(G)
                elif strippedresults == 'GG':                                                                 
                    print(G + ', ' + G)                                                                      
                elif strippedresults == 'Y':                                                                   
                    print(Y)                                                                                  
                elif strippedresults == 'YY':
                    print(Y + ', ' + Y)
                elif strippedresults == 'YYY':
                    print(Y + ', ' + Y + ', ' + Y)
                elif strippedresults == 'GY':
                    print(G + ', ' + Y)
                elif strippedresults == 'GRY':
                    print(G + ', ' + Y)
                elif strippedresults == 'GYY':
                    print(G + ', ' + Y + ', ' + Y)
                elif strippedresults == 'GGG':
                    pass

                print('')

            except:
                print('no')
                                                                                                 
# ---------------------------------------------------------------------------------------------- #
              
            if (num == ans):                                                                           # If the answer is correct, breaks out of loop
                print('OMG CONGRATS!!!')                                                               # Congratulatory message
                print('')
                Correct = True
             
        else:
            print('Not Enough Characters or Too Many Characters, Please Try Again.')
            print('')
    except:
        print('Invalid Character, Please Try Again.')                                                  # If an invalid character is input (like e), prompts for retry
        print('')
    
# --------------------------------------------------------------------------------------------- #

input('-Press enter to Exit the Program-')   # Stops program from exiting


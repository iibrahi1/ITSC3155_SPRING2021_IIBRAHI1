# Python Activtiy
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# import regular expression module
import re

# Part A. ends_with_consonant(s)
# Define a function ends_with_consonant(s) that takes a string and returns true
# if it ends with a consonant and false otherwise.
# (For our purposes, a consonant is any letter other than A, E, I, O, U.)
# Note: Be sure to use RegEx and it works for both upper and lower case and for nonletters!

def ends_with_consonant(s):

  x = True;
  if re.search('[aeiou]$',s):
    x = False;
  return x;




 # Part B. ends_with_number
# Define a function ends _with_number(s) that takes a string and returns true
# if it ends with a number and false otherwise.
# (For our purposes, a number is any character that is 0,1,2,3,4,5,6,7,8, or 9.)
# Note: Be sure to use RegEx!
def ends_with_number(s):

  x = re.search(r'[0-9]$', s)
  if x == None:
    return False
  return True


# Part C. binary_multiple_of_6
# define a method binary_multiple_of_4(s) that takes a string and returns true
# if the string represents a binary number that is a multiple of 6.
# Note: Be sure it returns false if the string is not a valid binary number!
# Hint: Use regular expressions to match for the pattern of a binary number that is a multiple of 6.
def binary_multiple_of_6(s):

  x = re.search(r'^[0-1]+$', s)
  if x != None:
        binary = x.group()
        index = len(binary)-1
        num = 0
        expo = 0
        while index >= 0:
            if binary[index] == "1":
                n = 1
                for i in range(expo):
                    n *= 2
                num += n
            expo += 1
            index -= 1
        if num % 6 == 0:
            return True
  return False


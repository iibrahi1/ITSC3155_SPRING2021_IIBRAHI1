# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
  # YOUR CODE HERE

  return int(n/3)


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.

def longest_consecutive_repeating_char(s):
  # YOUR CODE
    count = 1
    maxCount = 0
    maxChar = s[0]
    for i in range(1,len(s)):
      if s[i] == s[i-1]:
        count = count + 1
      if count > maxCount:
          maxCount = count
          maxChar = s[i-1]
      if s[i] != s[i-1]:
         count = 1
    return maxChar


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).

def is_palindrome(s):
  # YOUR CODE HERE
  s = s.replace(" ","").lower()
  temp = ""
  for i in range(len(s)-1, -1,-1):
    temp += s[i]
  return temp == s

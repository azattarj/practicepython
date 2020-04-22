""" Ask the user for a string and print out whether this string is a palindrome or not.
 (A palindrome is a string that reads the same forwards and backwards.)"""

while True:
    string = input('Dear user, please enter the string')
    if not string:
        print('Wrong input')
        continue
    else:
        break

if string == ''.join(reversed(string)):
    print('It seems palindrome')
else:
    print('Not a palindrome string')

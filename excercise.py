from time import sleep

while True:
    try:
        number = int(input('Dear user, please enter a whole number'))
        break
    except:
        print('Wrong input!')
        continue
print('Thank you. Please wait until I check for even or odd')
sleep(5)
if number % 2 == 0:
    print('It seems the number is even!')
else:
    print('An odd number.')

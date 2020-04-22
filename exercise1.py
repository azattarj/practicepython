import datetime

name = input('Please tell what is you name.')
age = input('Now please tell your age.')
number = input('Good, now please tell a random number. :D')
this_year = datetime.date.today().year
year_of_100 = 100 - int(age) + this_year
for i in range(int(number)):
    print('Dear ' + name + ', you will turn 100 in ' + str(year_of_100) + '.')
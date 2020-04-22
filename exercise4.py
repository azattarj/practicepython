while True:
    try:
        number = int(input('Dear user, please enter a number!'))
        break
    except ValueError:
        print('Wrong input!')
        continue

count = 0
r = int(number/2)+1
for i in range(2, r):
    if number % i == 0:
        count += 1

print(count)

new_list = [item for item in range(2, r) if number % item == 0]
print(new_list)

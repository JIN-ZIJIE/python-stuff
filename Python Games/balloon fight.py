answer = input('Throw a water balloon? (y/n)')
while answer == 'y':
    print('Splash!')
    answer = input('Throw another water balloon? (y/n)')
while answer == 'n':
    answer = input('Are you sure? (y/n) ')
    if answer == 'y':
        quit()

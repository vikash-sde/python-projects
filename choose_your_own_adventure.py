name = input('type your name')
print('welcome',name, 'to this adventure')

answer = input('you can go left or right?').lower()
if answer == 'left':
    answer = input('you come to a river, you can walk around it or swim accross?')
    if answer == 'swim':
        print('you swim accross and were eaten by an alligator')
    elif answer == 'walk':
        print('you walked for miles, rat out of water and you lost')
    else:
        print('not a valid option. you lose')

elif answer == 'right':
    answer = input('you come to a bridge and find a key ? do you want to pick up or not?')
    if answer == 'pick up':
        print('you have got a key to locker room of famous egypt queen')
    elif answer == 'not':
        print('you have to got received a message your egypt queen about their key worth if you find that.. ')
    else:
        print('not a valid option')

else:
    print('not a valid option. you lose')
import random

upper_limit = input('type upper limit number: ')

if upper_limit.isdigit() :
    upper_limit = int(upper_limit)
    if upper_limit <=0 :
        print('please type valid number greater than 0')
        quit()
else:
    print('please type a number next time')
    quit()
    
random_number = random.randrange(0,upper_limit)
print(random_number)

guesses = 0

while True :
    user_guess = input('make a guess: ')
    guesses+=1

    if user_guess.isdigit() :
        user_guess = int(user_guess)
      
    else:
        print('please type a number next time')
        continue
    if user_guess == random_number:
        print('you got it right!')
        break
    elif user_guess > random_number:
        print('you were above the number!')
    else:
        print('you were below the number!')
    


print('you got it in',guesses,'guesses')

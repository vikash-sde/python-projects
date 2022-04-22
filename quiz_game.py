print('welcome to my computer quiz!!')

playing = input('do you want to play? ')

if playing.lower() != 'yes':
    quit()

print("Okay! let's play :)")

score = 0

# q1
answer = input('what does cpu stand for? ')

if answer.lower() == "central processing unit":
    print('correct answer!')
    score += 1
else:
    print('wrong answer!!')

# q2
answer = input('what does gpu stand for? ')

if answer.lower() == "graphics processing unit":
    print('correct answer!')
    score += 1
else:
    print('wrong answer!!')

# q3
answer = input('what does ram stand for? ')

if answer.lower() == "random access memory":
    print('correct answer!')
    score += 1
else:
    print('wrong answer!!')


print('you got ' + str(score) + ' questions correct!')
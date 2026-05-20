# while loop:
# this loop will repeat a block of code until the condition is False
number=3
guess=0
while guess!=number:
    guess=int(input('Guess the number(1-5):' ))
    if guess!=number:
        print('Wrong! Try Again')
print('You got it!')

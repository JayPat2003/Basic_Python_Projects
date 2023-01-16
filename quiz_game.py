# Quiz game
# Done by JAYESH PATTAMATTA

print('Welcome to my computer quiz!')

playing = input("Do you want to play? ")

"""
lower() is used to convert any type of caps string to the smaller case
For example:
text = "JaYeSH"
print(text.lower())

OUTPUT : jayesh

similarly, 
upper() is used to convert any small letters to caps.

"""

if playing.lower() != 'yes':
    quit()

print("Okay! Let's play :) ")
score = 0

answer = input('What does the CPU stand for? ').lower()

if answer == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect! Let us try the next question !')

answer = input('What does the BIOS stand for? ')

if answer.lower() == "basic input output system":
    print('Correct!')
    score += 1
else:
    print('Incorrect! Let us try the next question !')

answer = input('What does the GPU stand for? ')

if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect! Let us try the next question !')

answer = input('What does the ROM stand for? ')

if answer.lower() == "read only memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect! Let us try the next question !')

answer = input('What does the RAM stand for? ')

if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect! Let us try the next question !')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")
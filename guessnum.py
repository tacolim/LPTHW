from random import randint

correctnum = randint(1,100)

print "I have selected a number between 1 & 100. Let's play Warm or Cold. Try to guess what it is!"

guess = int(raw_input("> "))

while guess != correctnum:
    if (correctnum - guess) >= 50 or (guess - correctnum) >= 50:
        print "That's pretty far off. Ice cold. Guess again."
        guess = int(raw_input("> "))
    elif (30 <= (correctnum - guess) < 50) or (30 <= (guess - correctnum) < 50):
        print "Not close. Pretty cool. Guess again."
        guess = int(raw_input("> "))
    elif (15 <= (correctnum - guess) < 30) or (15 <= (guess - correctnum) < 30):
        print "You're warm, but not hot. Guess again."
        guess = int(raw_input("> "))
    elif (5 <= (correctnum - guess) < 15) or (5 <= (guess - correctnum) < 15):
        print "You're pretty warm now. Guess again."
        guess = int(raw_input("> "))
    elif (1 <= (correctnum - guess) < 5) or (1 <= (guess - correctnum) < 5):
        print "So close! Very hot! Guess again."
        guess = int(raw_input("> "))

else:
    print "You guessed %d which matches my number %d! You are on fire! You win!" % (guess, correctnum)

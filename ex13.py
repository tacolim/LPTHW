from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

film = raw_input("What's your favorite film? ")
char = raw_input("Who's your favorite character? ")
food = raw_input("What's your favorite food? ")

print "So you like %s, %s, and %s." % (film, char, food)

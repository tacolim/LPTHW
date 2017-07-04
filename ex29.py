people = 15
cats = 19
dogs = 10


if people < cats:
    print "Too many cats! The world is doomed!"
elif people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"
elif people > dogs:
    print "The world is dry!"


dogs += 5

if people > dogs:
    print "People are greater than or equal to dogs. Where are all the dogs?"
elif people < dogs:
    print "People are less than or equal to dogs. Who let the dogs out?"
else:
    print "People are dogs."

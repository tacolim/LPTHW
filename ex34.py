animals = ['bear', 'tiger', 'penguin', 'zebra']
print "This is the first animal or the animal at '0' postion: ", animals[0]

animal = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

print "The animal at '1' is the 2nd animal & is: ", animal[1]
print "The 3rd animal is at position '2' & is: ", animal[2]
print "The 1st animal is at position '0' & is: ", animal[0]
print "The animal at '3' is the 4th animal & is: ", animal[3]
print "The 5th animal is at position '4' & is: ", animal[4]
print "The animal at '2' is the 3rd animal & is: ", animal[2]
print "The 6th animal is at postion '5' & is: ", animal[5]
print "The animal at '4' is the 5th animal & is: ", animal[4]

print ("\nOr, to check our work:\n1st Animal/Postion 0: %s\n2nd Animal/Postion 1: %s" +
    "\n3rd Animal/Postion 2: %s\n4th Animal/Postion 3: %s\n5th Animal/Postion 4: %s" +
    "\n6th Animal/Postion 5: %s" % tuple(animal))

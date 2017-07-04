name = 'Cassidy S.N. Avery'
age = 32 # not a lie
height = 63 # inches
weight = 160 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Blonde'
itoc = 2.54
ptok = 0.453592

print "Let's talk about %s." % name
print "She's %d inches tall." % height
print "She's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "She's %r centimeters tall." % (height * itoc)
print "She's %r kilograms heavy." % (weight * ptok)

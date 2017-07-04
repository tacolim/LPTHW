def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30,2)
height = subtract(78,4)
weight = multiply(80,2)
cats = divide(6,3)

print "Age: %d, Height: %d, Weight: %d, Cats: %d" % (age, height, weight, cats)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide (cats, 2))))

print "That becomes: ", what, "Can you do it by hand?"

x = multiply(add(3,2),add(-1,1))

print "That becomes: ", x

y = (3 + 2)*(-1 + 1)

print "That becomes: ", y

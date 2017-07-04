the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)


# now we can print them out too
for i in elements:
    print "Element was: %d" % i

elements.__delslice__(1, 4)

for i in elements:
    print "Element was: %d" % i

fav_food = []

print "Let's talk about food. What's your favorite food?"
x = raw_input("> ")

fav_food.append(x)

for i in range(4):
    fav_food.append(raw_input("What's another food you like? "))

print "So you really like to eat %s, %s, %s, %s, & %s." % tuple(fav_food)

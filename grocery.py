print "I'll help you make a grocery list. Type 'end' when you are finished."

grocery_list = []

item = ''

while item != 'end':
    item = raw_input("Type item to add to list: ")

    if item != 'end':
        grocery_list.append(item)

sorted_grocery_list = sorted(grocery_list)

print "\n\nGrocery List:"

for elem in sorted_grocery_list:
    print elem

i = 0
numbers = []

def counting(i, myvar, myvar2):
    for i in range(0, myvar):
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + myvar2
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

print "By what increment should we count?"
countby = int(raw_input(">>> "))

print "What number should the count stop at?"
limit = int(raw_input(">>> "))

counting(i, limit, countby)

print "The numbers: "

for num in numbers:
    print num

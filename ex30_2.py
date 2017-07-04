people = 45
seats_in_cars = 40
seats_in_trucks = 30

if seats_in_cars >= people and seats_in_trucks < people:
    print "I guess we'll take the cars."
elif seats_in_trucks >= people and seats_in_cars < people:
    print "I guess we'll take the trucks."
elif seats_in_cars < people and seats_in_trucks < people:
    print "I guess we need to look into buses or vans."

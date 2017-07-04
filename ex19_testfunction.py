print "Let's go on a peanut butter and jelly picnic."
user_sammies = raw_input("How many sandwiches would you like? ")
user_sammies = int(user_sammies)
print "Great. I want one, so I'll make %r sammies." % (user_sammies + 1)
user_pb = raw_input("What type of peanut butter do you want? Crunchy or Creamy? ")
if user_pb == "Crunchy":
    print "Whoops, I apparently only have creamy. "
    my_pb = "creamy"
else:
    print "Whoops, I apparently only have crunchy. "
    my_pb = "crunchy"
user_jam = raw_input("What flavor of jam do you want? ")
if user_jam == "blackberry":
    print "Yuck, I hate blackberry, I'll have strawberry."
    my_jam = "strawberry"
else:
    print "That's a weird choice. I'll have blackberry."
    my_jam = "blackberry"

def pbjtime(num_sammies, type_pb, type_jam):
    print ("Ok. So we'll have %r sandwiches.  All will have %s peanut butter. %r will have %s jam and one will have %s."
    % (num_sammies, type_pb, user_sammies, user_jam, type_jam))

pbjtime(user_sammies + 1, my_pb, my_jam)

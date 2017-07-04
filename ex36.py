def start():
    print "You are in a stone room, bare except four tapestries on the walls. "
    print "The tapestries are a thick black fabric each with a skull & crossbone."
    print "You realize the tapestries cover heavy wooden doors. Which do you go down? "
    print "1, 2, 3, or 4?"

    choice = int(raw_input("> "))

    if choice == 1:
        mirrortobugs()
    elif choice == 2:
        bugs()
    elif choice == 3:
        snakes()
    elif choice == 4:
        mirrortosnakes()
    else:
        dead("You sit staring at the tapestries unable to make a choice eventually dying of thirst.")


def mirrortobugs():
    print "Behind the door you entered into a dark, narrow corridor and the door swings shut and locks behind you."
    print "You walk forward toward a growing light eventually entering a round, stone room with high ceilings."
    print "A panel slides closed blocking the corridor you had just walked in from."
    print "The room is bare except for a large mirror with an ornate, gilt frame."
    print "What do you do?"
    print "1: Stand in front of the mirror and say 'Bloody Mary' three times."
    print "2: Stand in front of the mirror and say 'Mirror Mirror on the wall... who's the fairest of them all?'"
    print "3: Punch the mirror."

    choice = int(raw_input("> "))

    if choice == 1:
        print "A woman coated in blood briefly appears in the mirror and cackles."
        print "The woman slowly fades leaving an image of you surrounded by bugs."
        print "A wall next to you slides open revealing a passage."
        bugs()
    elif choice == 2:
        print "The mirror shows you an image of Snow White cleaning a cottage with woodland animals."
        print "The image slowly fades leaving an image of you surrounded by bugs."
        print "A wall next to you slides open revealing a passage."
        bugs()
    elif choice == 3:
        print "You punch the mirror. Shards shower you and the ground."
        print "Your hand bleeds from many small cuts."
        print "You can't think of what to do now so you begin to count the bricks."
        dead ("You realize there is no way out and eventually die of thirst.")
    else:
        dead("You're stuck in this room. Eventually you die of thirst.")


def mirrortosnakes():
    print "Behind the door you entered into a dark, narrow corridor and the door swings shut and locks behind you."
    print "You walk forward toward a growing light eventually entering a round, stone room with high ceilings."
    print "A panel slides closed blocking the corridor you had just walked in from."
    print "The room is bare except for a large mirror with an ornate, gilt frame."
    print "What do you do?"
    print "1: Stand in front of the mirror and say 'Bloody Mary' three times."
    print "2: Stand in front of the mirror and say 'Mirror Mirror on the wall... who's the fairest of them all?'"
    print "3: Punch the mirror."

    choice = int(raw_input("> "))

    if choice == 1:
        print "A woman coated in blood briefly appears in the mirror and cackles."
        print "The woman slowly fades leaving an image of you surrounded by snakes."
        print "A wall next to you slides open revealing a passage."
        bugs()
    elif choice == 2:
        print "The mirror shows you an image of Snow White cleaning a cottage with woodland animals."
        print "The image slowly fades leaving an image of you surrounded by snakes."
        print "A wall next to you slides open revealing a passage."
        bugs()
    elif choice == 3:
        print "You punch the mirror. Shards shower you and the ground."
        print "Your hand bleeds from many small cuts."
        print "You can't think of what to do now so you begin to count the bricks."
        dead ("You realize there is no way out and eventually die of thirst.")
    else:
        dead("You're stuck in this room. Eventually you die of thirst.")

def bugs():
    print "Behind the door you entered into a dark, narrow corridor and the door swings shut and locks behind you."
    print "You walk forward in the dark and the corridor becomes increasingly steep downward until you lose your footing and begin sliding."
    print "You are dumped unceremoneously into a room with cases upon cases of bugs squirming over and around each other."
    print "An occasional bug skitters across the floor or up a wall."
    print "A panel slides closed blocking the corridor you had just wakled in from."
    print "You look around and you see centipede the size of a man on the far side of the room in front of two doors."
    print "Its mirror-like eyes stare into you while its mandibles open and close menicingly."
    print "What do you do?"
    print "1: Intimidate: Step on the next bug in front of you to intimidate the large bug."
    print "2: Distract: Push over the cases of bugs sending millions of creepy crawlies scattering in all directions."
    print "3: Confuse: Begin babbling at the centipede and toss the occasional bug at it."
    print "4: Assault: Scream like a banshee then run toward the centipede attempting to land a punch or kick on one of its plated segments."

    while True:
        choice = int(raw_input("> "))

        if choice == 2:
            print "The centipede begins racing around trying to corral the bugs together leaving the doors unattended."
            print "You race toward them, which do you choose? Left or Right?"

            door_choice = raw_input("> ")

            if door_choice == "Left" or door_choice == "left":
                snakes()
            if door_choice == "Right" or door_choice == "right":
                food()
            else:
                dead("You didn't choose Left or Right door quickly enough. The centipede returns and kills you in a slow and painful manner.")

        elif choice == 3:
            print "The centipede begins catching the bugs as you toss them and eats them. You toss a bug to the side and the centipede runs off to grab it, leaving the doors unattended."
            print "You race toward them, which do you choose? Left or Right?"

            door_choice = raw_input("> ")

            if door_choice == "Left" or door_choice == "left":
                snakes()
            if door_choice == "Right" or door_choice == "right":
                food()
            else:
                dead("You didn't choose Left or Right door quickly enough. The centipede returns and kills you in a slow and painful manner.")

        else:
            dead("The centipede emits a high pitched scream and kills you in a slow and painful manner.")



def snakes():
    print "Behind the door you entered into a dark, narrow corridor and the door swings shut and locks behind you."
    print "You walk forward in the dark and the corridor becomes increasingly steep downward until you lose your footing and begin sliding."
    print "You are dumped unceremoneously into a room with an extremely large snake at one end blocking two doors."
    print "There are small pebbles and bones littering the floor."
    print "A panel slides closed blocking the corridor you had just wakled in from."
    print "What do you do?"
    print "1: Intimidate: Scream like a banshee and run toward the snake making yourself look as large and intimidating as you can."
    print "2: Confuse: Begin babbling at the snake and toss the occasional bone or pebble at it."

    while True:
        choice = int(raw_input("> "))

        if choice == 1:
            print "The snake is spooked and slithers off into a corner leaving the doors unattended."
            print "You race toward them, which do you choose? Left or Right?"

            door_choice = raw_input("> ")

            if door_choice == "Left" or door_choice == "left":
                gold()
            if door_choice == "Right" or door_choice == "right":
                bugs()
            else:
                dead("You didn't choose Left or Right door quickly enough. The snake returns and kills you in a slow and painful manner.")

        elif choice == 2:
            print "The snake is confused and spooked.  It slithers off into a corner leaving the doors unattended."
            print "You race toward them, which do you choose? Left or Right?"

            door_choice = raw_input("> ")

            if door_choice == "Left" or door_choice == "left":
                gold()
            if door_choice == "Right" or door_choice == "right":
                bugs()
            else:
                dead("You didn't choose Left or Right door quickly enough. The snake returns and kills you in a slow and painful manner.")

        else:
            dead("The snake emits a high pitched scream and kills you in a slow and painful manner.")

def food():
    print "You walk through the door which shuts and locks behind you."
    print "You walk down a long corridor which ends in a room full of table upon table of amazing food."
    print "There is a door at the other end of the room."
    print "1. Eat."
    print "2. Knock on the door."

    choice = int(raw_input("> "))

    if choice == 1:
        print "This is the most delicious food you've ever eaten."
        print "Eat more or knock on door?"

        eatorgo = raw_input("> ")

        if "eat" in eatorgo or "Eat" in eatorgo:
            dead("You continue eating. You are unable to stop. You eventually die in this room.")
        elif "knock" in eatorgo or "Knock" in eatorgo:
            print "You reluctantly pull yourself away from the delicious food."
            print "You knock on the door and it swings open revealing a dazzingly sunny day."
            print "You run out into the sunlight and escape. Never to look back."
            exit(0)
        else:
            dead("You eventually die in this room.")

    elif choice == 2:
        print "You reluctantly walk past all the decident food and knock on the door which swings open."
        print "You escape into the brilliant light of day never to look back."
        exit(0)
    else:
        dead("You eventually die in this room.")


def gold():
    print "You walk through the door which shuts and locks behind you."
    print "You walk down a long corridor which ends in a room full of table upon table of gold and treasure."
    print "There is a door at the other end of the room."
    print "1. Take some treasure."
    print "2. Knock on the door."

    choice = int(raw_input("> "))

    if choice == 1:
        dead("The gold is all tainted by a fast acting poison which enters through your skin killing you.")

    elif choice == 2:
        print "You reluctantly walk past all the treasure and knock on the door which swings open."
        print "You escape into the brilliant light of day never to look back."
        exit(0)
    else:
        dead("You eventually die in this room.")

def dead(why):
    print why, "Better luck next life!"
    exit(0)

start()

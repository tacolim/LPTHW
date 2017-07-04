
"""
'Aliens have invaded a space ship and our hero has to go through a maze of rooms\
 defeating them so he can escape into an escape pod to the planet below.\
 erThe game will be more like a Zork or Adventure type game with text outputs and\
  funny ways to die. The game will involve an engine that runs a map full of rooms or scenes.\
   Each room will print its own description when the player enters it and then tell \
   the engine what room to run next out of the map.'

OBJECT TREE
* Map
  - next_scene
  - opening_scene
* Engine
  - play
* Scene
  - enter
  * Death
  * Central Corridor
  * Laser Weapon Armory
  * The Bridge
  * Escape Pod
"""
from sys import exit
from random import randint

class Scene(object):

     def enter(self):
         print "This scene is not yet configured. Subclass it and implement enter()."
         exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Death(Scene):

    quips = [
        "\nYou died. Way to go.",
        "\nYou died. Better luck next time.",
        "\nYou died. No one can stop these Gorthons!",
        "\nYou died wondering why you even got out of bed this morning.",
        "\nYou died... without honor... without glory... and you will be forgotten.",
        "\nYou died. How does it feel to be Gorthon food?"
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
        print "your entire crew. You only survived by the shear luck that you were"
        print "hiding from your boss and napping in a broom closet."
        print "Now you have to get the heck out of here and might as well take some"
        print "of these Gothons out with you."
        print "You should get a neutron destruct bomb or two from the Weapons Armory,"
        print "set it on the bridge, and blow up the ship after getting into an"
        print "escape pod.\n\n"
        print "You're running down the central corridor to the Weapons Armory when"
        print "you nearly run directly into a Gothon blocking the Armory door."
        print "He's about to pull a weapon and blast you. Think fast!"

        action = raw_input("> ")

        if "shoot" in action:
            print "\nYou draw your weapon, but you are shakey from the shock of losing"
            print "your entire crew. Your aim is off and you miss entirely. He shoots"
            print "you until you are dead. Then he eats you."
            return 'death'

        elif "dodge" in action:
            print "\nLike a world class boxer you dodge, weave, slip to the right"
            print "as a blast from the Gorthon's weapon shoots past your head."
            print "In the middle of your artful dodge, your foot slips and you"
            print "bang your head on the wall and pass out."
            print "You wake shortly after only for the Gorthon to stomp on your"
            print "head and eat you."
            return 'death'

        elif "run" in action:
            print "\nLike the coward you are, you decide to give up on the idea of"
            print "bombing the ship. You take off in the other direction in hopes"
            print "of getting to an escape pod. Lasers whiz past your head and the"
            print "Gorthon behind you yells repeadedly in its language."
            print "Suddenly, Gorthons rush into the corridor from all sides. One"
            print "walks swiftly to you and breaks your neck. The Gorthons all fight"
            print "over who gets to eat you."
            return 'death'

        elif "joke" in action:
            print "\nLucky for you they made you learn some elementary Gorthon in the"
            print "Academy. You tell the first raunchy joke that comes to mind."
            print "The Gorthon stops, tries not to laugh, then bursts out laughing"
            print "so hard that he is nearly doubled over."
            print "While he is distracted, you run up and shoot him in the head."
            print "Then you jump through the Armory door."
            return 'laser_weapon_armory'

        else:
            print "\nDOES NOT COMPUTE!\n"
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print "\nYou dive rool into the Armory and crouch scanning for more Gorthons."
        print "It's dead quiet. You stand and run to the far side of the room."
        print "The neutron bombs are in a container with a keypad lock."
        print "If you get the code wrong 10 times then the lock closes forever"
        print "and you can't get the bomb."

        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        print code
        guess = raw_input("[keypad]> ")
        guesses = 1

        while guess != code and guesses < 10:
            print "BZZZZZEDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "\nThe container clicks open. You grab a neutron bomb and run as"
            print "fast as you can toward the bridge where you must place it."
            return 'the_bridge'

        else:
            print "BZZZZZEDD!"
            print "\nAnd then you hear a sickening melting sound as the mechanism"
            print "is fuzed together proving that you did not correctly guess"
            print "the code. You take off in the direction of the escape pods."
            print "Suddenly, Gorthons rush into the corridor from all sides. One"
            print "walks swiftly to you and breaks your neck. The Gorthons all fight"
            print "over who gets to eat you."
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print "\nYou burst onto the Bridge with the neutron bomb under your arm and"
        print "surprise five Gothons who are trying to take control of the ship."
        print "They all reach for their weapons, but seeing the bomb under your"
        print "arm, they hesitate. What do you do?"

        action = raw_input("> ")

        if "throw" in action:
            print "\nYou panic and throw the bomb and make a leap for the door, but"
            print "a Gothon shoots you in the back before you can make your escape."
            print "As you die you watch the Gothons trying desperately to disarm"
            print "the bomb. You are hopeful that the bomb will still explode and"
            print "kill them so hopefully they won't eat your corpse."
            return 'death'

        elif "place" in action:
            print "\nYou point your blaster at the bomb, knowing the Gorthons won't"
            print "make any sudden moves with all their lives on the line. You inch"
            print "back toward the door and carefully place the bomb on the floor,"
            print "still pointing your blaster at it. You jump through the door and"
            print "punch the close button then blast the lock so the Gorthons can't"
            print "follow you."
            print "Now that the bomb is placed, you run to the escape pods."
            return 'escape_pod'

        else:
            print "\nDOES NOT COMPUTE!\n"
            return 'the_bridge'

class EscapePod(Scene):

    def enter(self):
        print "\nYou rush through the ship and luckily encounter no more Gorthons."
        print "You get to the chamber with the escape pods and realize you don't"
        print "have time to check them over for damage, you just have to pick"
        print "one and hope."

        good_pod = randint(1,5)
        print good_pod
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "\nYou jump into pod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            return 'death'

        elif int(guess) == good_pod:
            print "\nYou jump into pod %s and hit the eject button." % guess
            print "The pod escapes out into space and heads toward"
            print "the planet below. As it flies, you look back and"
            print "see your ship implode then explode like a bright"
            print "star, taking out the Gothon ship at the same time."
            print "You won!"
            return 'finished'

        else:
            print "\nDOES NOT COMPUTE!\n"
            return 'escape_pod'

class Finished(Scene):

    def enter(self):
        print "\nYou won! Good job!"
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor' : CentralCorridor(),
        'laser_weapon_armory' : LaserWeaponArmory(),
        'the_bridge' : TheBridge(),
        'escape_pod' : EscapePod(),
        'death' : Death(),
        'finished' : Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

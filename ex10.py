tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "I am 6'2\" tall."
print 'I am 6\'2" tall.'

print '''
When you need to print multiple lines you can type this:
"""
Hello I am typing three single quotes.
I don't know why this would be better.
Is it in fact any better?
Why would I use this?
"""
'''

formatter = "%r %r %r %r"
sformatter = "%s %s %s %s"

print formatter % ("Dad isn't \"bar\".", 'mom isn\'t "foo".', "Daugter.", 'cats!')
print sformatter % ("Dad isn't \"bar\".", 'mom isn\'t "foo".', "Daugter.", 'cats!')

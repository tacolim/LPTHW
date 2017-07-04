formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
print formatter % ("C", "D", "B", "A&T")

#This is useful for printing many variables quickly together.
#Formatter is the placeholder/variable.
#formatter is "holding" four variables "%r %r %r %r"
#when you print formatter % (x, y, z, a) the characters/strings in the parenthetical
#will take the place of the %r.

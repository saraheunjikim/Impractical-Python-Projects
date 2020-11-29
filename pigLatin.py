""" Take the input and return it as a Pig Latin words. """
import sys

vowels = 'aioeuy'

while True:
    print("Please type any word here: ")
    word = input()

    if word[0] in vowels:
        Pig_Latin = word + "way"
    else:
        Pig_Latin = word[1:] + word[0] + "ay"

    print("{}".format(Pig_Latin), file=sys.stderr)

    try_again = input("Wish to exit, please press 'q'.")
    if try_again.lower() == 'q':
        break





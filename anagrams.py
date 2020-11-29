import load_dictionary
word_list = load_dictionary.load('2of4brif.txt')

### This is incorrect version, before the solution.
# def find_anagram():
#     anagram_list = []
#     question = input("Please enter any single word without any space: ")
#     sorted_word = sorted(question)
#     for word in word_list:
#         if sorted_word == word:
#             word.append(anagram_list)
#         else:
#             print("There is no match.")
#             break
#     print(anagram_list)

    
# find_anagram()

anagram_list = []

### The correct answer from the book.
# input a SINGLE word or SINGLE name below to find its anagram(s):
# name = 'Foster'
# print("Input name = {}".format (name))
# name = name.lower()
# print("Using name = {}".format(name))

# ask a user to input the name
name = input("Please enter any single word or name: ")
name = name.lower()

# sort name & find anagrams
name_sorted = sorted(name)
for word in word_list:
    word = word.lower()
    if word != name:
        if sorted(word) == sorted(name):
            anagram_list.append(word)

print()  # add a new line inbetween

# print out list of anagrams
if len(anagram_list) == 0:
    print("You need a larger dictionary or a new name!")
else:
    print("Anagrams: ", *anagram_list, sep="\n")
    
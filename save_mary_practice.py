from random import randint
import load_dictionary
import string

# open dictionary file
word_list = load_dictionary.load('supporters.txt')

input_message = "Give your word and we rise"

# remove whitespace
message = ''
for char in input_message:
    if char in string.ascii_letters:
        message += char
print(message, "\n")

vocab_list = []
count = 1
vocab_list.insert(0, 'first')

for letter in message:
    for word in word_list:
        if len(word) > 2 and word not in vocab_list:
            if count % 2 == 0 and word[2].lower() == letter.lower():
                vocab_list.append(word)
                count += 1
                break
            elif count % 2 != 0 and word[1].lower() == letter.lower():
                vocab_list.append(word)
                count += 1
                break

vocab_list.insert(3, 'Stuart')
vocab_list.insert(6, 'Jacob')
            
print(*vocab_list, sep='\n')

    

#-----------------------------------------------------------------------------------------------------------------

# """Hide a null cipher within a list of names using a variable patters."""
# import load_dictionary

# # write a short message and use no punctuation or numbers!
# message = "Give your word and we rise"
# message = "".join(message.split())

# # open name file
# names = load_dictionary.load('supporters.txt')

# name_list = []

# # start list with null word not used in cipher
# name_list.append(names[0])

# # add letter of null cipher to 2nd letter of name, then 3rd, then repeat
# count = 1
# for letter in message:
#     for name in names:
#         if len(name) > 2 and name not in name_list:
#             if count % 2 == 0 and name[2].lower() == letter.lower():
#                 name_list.append(name)
#                 count += 1
#                 break
#             elif count % 2 != 0 and name[1].lower() == letter.lower():
#                 name_list.append(name)
#                 count += 1
#                 break

# # add two null words early in message to throw off cryptanalysts
# name_list.insert(3, 'Stuart')
# name_list.insert(6, 'Jacob')

# # display cover letter and list with null cipher
# print("""
# Your Royal Highness: \n
# It is wit hthe greatest pleasure I present the list of noble familes who
# have undertaken to support your cause and petition the usurper for the
# release of your Majesty from current tragical circumstances.
# """)

# print(*name_list, sep='\n')

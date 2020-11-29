import load_dictionary

word_list = load_dictionary.load('2of4brif.txt')

# diagram = ['dt', 'lr', 'md', 'ml', 'mr', 'mt', 'mv',
#     'td', 'vd', 'vl', 'vm', 'vr', 'vt', 'ld', 'lm', 
#     'lt', 'lv', 'rd', 'rl', 'rm', 'rt', 'rv', 'tl' ,'tm']

# def find_diagram(word):
#     dia_in_word = []
#     frequency = 0
#     for dia in diagram:
#         if dia in word:
#             dia_in_word.append(dia)

#     for rep in dia_in_word:
#         for word in word_list:
#             if rep in word:
#                 frequency += 1
    
#     print(frequency)

# find_diagram('tmvoordle')


"""Generate letter pairs in Voldemort & find their frequency in a dictionary."""

import re
from collections import defaultdict
from itertools import permutations

name = 'Voldemort' #(tmvoordle)
name = name.lower()

# generate unique letter paris from name
diagrams = set()
perms = {''.join(i) for i in permutations(name)}
for perm in perms:
    for i in range(0, len(perm) - 1):
        diagrams.add(perm[i] + perm[i+1])
print(*diagrams, sep='\n')
print("\nNumber of diagrmas = {}\n".format(len(diagrams)))

# use regular expressions to find repeating diagrams in a word
mapped = defaultdict(int)
for word in word_list:
    word = word.lower()
    for diagram in diagrams:
        for m in re.finditer(diagram, word):
            mapped[diagram] += 1

print("diagram frequency count: ")
count = 0
for k in mapped:
    print("{} {}".format(k, mapped[k]))



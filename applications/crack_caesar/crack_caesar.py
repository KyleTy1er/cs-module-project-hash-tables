# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
file = "ciphertext.txt"

most_frequent = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', ]

encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}

# create a dict of letter counts?

letters = {}

with open(file) as f:
    words = f.read()



for i in words:
    if i in letters:
        letters[i] += 1
    else:
        letters[i] = 1


sort_dict = sorted(letters.items(), key=lambda x: x[1], reverse=True)

new_dict = {}
for i in range(len(sort_dict)):
    if sort_dict[i][0] in most_frequent:
       new_dict[i]= sort_dict[i][0]

final_encode = {}
counter = 0
for i in new_dict:
    i = most_frequent[counter]
    counter += 1
    print(i)
    # print(new)
# for i in most_frequent:
#     print(i)




print(new_dict)




    # if sort_dict[i][0] not in most_frequent:
    #     del sort_dict[i]
# unwanted = set(keys) - set(your_dict)
# for unwanted_key in unwanted: del your_dict[unwanted_key]
# keys_to_remove = ["one", "three"]
# for key in keys_to_remove:
#   del a_dictionary[key]
#
# dict_you_want = {your_key: sort_dict[your_key] for your_key in most_frequent}
# print(dict_you_want)

# dict((key,value) for key, value in sort_dict.iteritems() if key in most_frequent)
# print(sort_dict)


import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# Read the file input.txt and split it into words.
words = words.split(' ')

# print(words[0:20])
# TODO: analyze which words can follow other words

# key is value, value is list...

markov_dict = {}
start_words = []
end_words = []

# attempting to store each word as a key with its following word as a value

capitals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '"']
ends = ['.', '?', '!', '"']





for i in range(len(words)-1):
    if words[i][0] in capitals:
        start_words.append(words[i])
    if words[i][-1] in ends:
        end_words.append(words[i])
    markov_dict[words[i]] = markov_dict.get(words[i], [])
    markov_dict[words[i]].append(words[i+1])


# TODO: construct 5 random sentences

for i in range(5):
    sentence = ""
    start = random.choice(start_words)
    sentence += start + " "
    next_word = random.choice(markov_dict[start])
    while start not in end_words:
        if next_word in end_words:
            sentence += next_word
            break
        sentence += next_word + " "
        next_word = random.choice(markov_dict[next_word])

    print(sentence)


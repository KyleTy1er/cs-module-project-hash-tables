
# Your code here



def count_words(file):
    ignored = "\":;,.-+=/\|[]{}()*^&?!"

    wordmap = {}

    with open(file) as f:
        words = f.read().lower()

        for char in ignored:
            words = words.replace(char, "")

        words = words.split()

        for word in words:
            if word not in wordmap:
                # if key doesnt exist
                # at this key input value of 1
                wordmap[word] = 1
            else:
                # if key exists...
                # at this key increment value by 1
                wordmap[word] += 1

        return wordmap

def render_word_count(dict):
    counts = [(dict[word], word) for word in dict]
    counts.sort(key = lambda e: (-e[0], e[1]))
    max_length = 0
    for word in counts:
        if len(word[1]) > max_length:
            max_length = len(word[1])
    for i in range(len(counts)):
        hashtags = counts[i][0] * "#"
        print (f'{counts[i][1]}\t'.expandtabs(17), hashtags)






print(render_word_count(count_words("robin.txt")))






def word_count(s):

    results = {}

    translation_table = dict.fromkeys(map(ord, '"{:;,.-+=/|\[]}()*^&"'), None)

    s = s.translate(translation_table)

    print(s)

    if s:

        words = s.lower().split(' ')
        while '' in words:
            words.remove('')

        for i in range(len(words)):
            words[i] = words[i].strip()

        for word in words:
            if word in results:
                results[word] += 1
            else:
                results[word] = 1

        return results

    if not s:

        return results

    # count each word and return the count
    # remove special characters
    # convert string to lowercase
    # we are not ignoring apostrophes
    # if letter is in dict remove it from array


'''
{'hello': 2, 'my': 2, 'cat': 2, 'and': 1, "doesn't": 1, 'say': 1, 'back': 1}
'''
#
if __name__ == "__main__":
    # x = word_count("")
    # print("expected outcome {}")
    # print(f"Outcome: {x}")
    #
    #
    # x = word_count("Hello    hello")
    # print("expected outcome {""hello"": 2}")
    # print(f"Outcome: {x}")
    #
    # print("expected outcome {""hello"": 2}")
    # print(f"Outcome: {x}")

    x = word_count('a a\ra\na\ta \t\r\n')
    # print(f"expected outcome: "'a'": 5")
    # print(f"Outcome: {x}")

    # white_chars = [c for c in x.whitespace]

    for i in x:
        x[i] = str(x[i])
        white_chars = [c for c in x[i].whitespace]

    # x = (word_count(""))
    #
    # print(x)
    #
    # if x == {}:
    #     print("success")


    # print(word_count("Hello      hello"))
    # print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    # print(word_count('This is a test of the emergency broadcast network. This is only a test.'))


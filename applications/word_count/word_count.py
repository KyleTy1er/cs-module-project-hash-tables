


def word_count(s):

    results = {}

    translation_table = dict.fromkeys(map(ord, '"{:;,.-+=/|[]}()*^&"'), None)

    s = s.translate(translation_table)
    # print(f" this is the translate: {s}")

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

if __name__ == "__main__":


    x = (word_count(""))

    print(x)

    if x == {}:
        print("success")
    # print(word_count("Hello      hello"))
    # print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    # print(word_count('This is a test of the emergency broadcast network. This is only a test.'))

# #
# self.assertTrue(x == {'hello': 2, 'my': 2, 'cat': 2, 'and': 1, "doesn't": 1, 'say': 1, 'back': 1}
#                      {'hello': 2, 'my': 2, 'cat': 2, 'and': 1, "doesn't": 1, 'say': 1, 'back': 1}

# this = 'Hello, my cat. And my cat doesn\'t say "hello" back.'
#
# print(this.strip())

#
# ignored_characters = ["'", "{", ":", ";" , "," , ".", "-", "+", "=", "/", "|", "[", "]" , "{", "}", "(", ")", "*", "^", "&","'"]
#
# def ignore_chars(x):
#     if x in ignored_characters:
#         return x.replace(x, '')
#
# string_ex = "these { strings are + here"
#
# for i in string_ex:
#     print(checker(i))
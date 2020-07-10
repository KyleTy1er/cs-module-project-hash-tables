
'''
# No Duplicates

Input: a string of words separated by spaces. Only the letters `a`-`z`
are utilized.

Output: the string in the same order, but with subsequent duplicate
words removed.

There must be no extra spaces at the end of your returned string.

The solution must be `O(n)`.
'''



def no_dups(s):

    huh = ""

    if len(s) > 0:

        words = s.split(' ')
        new_list = [None] * len(words)

        for i in range(len(words)):
            if words[i] not in new_list:
                new_list[i] = words[i]

        Not_none_values = filter(None.__ne__, new_list)
        new_list = list(Not_none_values)
        new_list = ' '.join(new_list)

        return new_list

    else:

        return huh



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))

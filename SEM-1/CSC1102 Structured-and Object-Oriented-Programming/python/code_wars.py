def opposite(number):
    return -number

# Reversing a string in python
# using [::-1] eg reversed_txt = 'hello world'[::-1]
def reverse_words(text):
    newText = text.split(" ")
    reversed_word = ''

    for word in newText:
        reversed_word = reversed_word + ' ' + word[::-1]

    return reversed_word[1:]
# print(reverse_words("This is an example!"))

# print(bool(None)) #False


def disemvowel(string_):
    vowels = [ 'a', 'e', 'i', 'o', 'u' ]
    chunks = list(string_)
    for i in chunks:
        if i.lower() in vowels:
            chunks.remove(i)
    return ''.join(chunks)


def is_isogram(string):
    characters = list(string)
    new_list = []
    for i in characters:
        if i in new_list:
            return False
        else:
            new_list.append(i)
    return True

print(is_isogram('boy'))
def freq_palavras(frases):
	''' Function that, given a phrase as parameter,
    returns a dictionary with the words as keys and
    the number of ocurrences as values.
    Str --> Dict'''
    dictionary = {}
    wordsSplitted = str.split(frases)
    for word in wordsSplitted:
        ocurrences = list.count(wordsSplitted, word)
        dict.update(dictionary, {word:ocurrences})
    return dictionary
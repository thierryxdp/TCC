def freq_palavras(frases):
	'''	'''
    dictionary = {}
    wordsSplitted = str.split(frases)
    for word in wordsSplitted:
        ocurrences = list.count(wordsSplitted, word)
        dict.update(dictionary, {word:ocurrences})
    return dictionary
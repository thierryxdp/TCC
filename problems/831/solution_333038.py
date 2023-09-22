def lingua_p (Word):
	'''Given a portuguese word, this function returns 
	this same word in the p language, in other words, with 
    the letter p after each vogal and the vogal repeated
    after the p.
    Str --> Str'''
    newWord = ''
    lowerCase = str.lower(Word)
    for i in lowerCase:
        if i in 'aeiou':
            newWord = newWord + str(i) + 'p' + str(i)
        else: 
            newWord = newWord + str(i)
    return newWord
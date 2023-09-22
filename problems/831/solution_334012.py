def lingua_p(palavra):
    '''Traduz uma string em portugues para lingua do p.
    str->str'''
    word = palavra.lower()
    for i in range(0,len(word)):
        if word[i] in 'aeiou':
            wordp = word.replace(word[i], word[i]+'p'+word[i])
    return wordp
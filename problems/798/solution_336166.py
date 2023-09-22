def freq_palavras(frases):
    '''Uma função que recebe uma frasa e numera as
    palavras por quantidade str --> dict(str:int)'''
    d = dict()
    for palavras in frases:
        if palavras not in d:
            d[palavras] = 1
        else:
            d[palavras] += 1
    for key in d:
        val = d[key]
        if val not in d:
            d[val] = [key]
        else:
            d[val].append(key)
    return d
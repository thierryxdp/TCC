def freq_palavras(frases):
    '''Uma função que recebe uma frasa e numera as
    palavras por quantidade str --> dict(str:int)'''
    nw_dictionary ={}
    for elemento in frases:
        if not (dict.get(nw_dictionary,elemento)):
            nw_dictionary[elemento] = 1
        else:
            nw_dictionary[elemento] += 1
    return nw_dictionary
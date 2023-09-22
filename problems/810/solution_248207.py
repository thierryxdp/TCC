def inverte (frase):
    ''' retorna o inverso da frase dada'''
        frase = str.replace (frase, '-', ' ')
    frase = str.replace (frase, ',' ,'')
    frase = str.replace (frase, ':', '')
    frase = str.replace (frase, ';', '')
    frase = str.replace (frase, '.', '')
    frase = str.replace (frase, '!', '')
    frase = str.replace (frase, '?', '')
    frase = str.replace (frase, '...', '')
    frase = str.lower(frase)
    frase = str.split(frase)
    inverte=" ".join(frase[::-1])
    return inverte
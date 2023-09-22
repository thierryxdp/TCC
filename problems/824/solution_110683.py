def uppCons(frase):
    '''recebe uma frase, e retorna a mesma com as consoantes
    em maiusculo;
    string->string'''
    consoantes=list('bcdfghjklmnpqrstvwxyz')
    i=0
    frasesep=list(frase)
    while i<len(frasesep):
        if frasesep[i] in consoantes:
            str.upper(frasesep[i])
        i=i+1
        ''.join(map(str,frasesep))
    return frasesep
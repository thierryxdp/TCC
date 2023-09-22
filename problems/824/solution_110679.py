def uppCons(frase):
    '''recebe uma frase, e retorna a mesma com as consoantes
    em maiusculo;
    string->string'''
    consoantes=['bcdfghjklmnpqrstvwxyz']
    i=0
    frasesep=str.split(frase,'')
    while i<len(frasesep):
        if frasesep[i] in consoantes:
            str.upper(frasesep[i])
        i=i+1
        ''.join(map(frasesep))
    return frasesep
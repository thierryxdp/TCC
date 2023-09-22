def uppCons(frase):
    '''recebe uma frase, e retorna a mesma com as consoantes
    em maiusculo;
    string->string'''
    consoantes=list('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    frasesep=list(frase)
    i=0
    tamanho=len(frasesep)
    while i<tamanho:
        if frasesep[i] in consoantes:
            str.upper(frasesep[i])
        i=i+1
    return frasesep
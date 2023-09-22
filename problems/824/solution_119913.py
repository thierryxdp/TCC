def uppCons(frase):
    '''Função que retorna a frase com as consoantes maiúsculas.
    str->str'''
    i=0
    while i<len(frase):
        if frase[i] not in 'aeiou':
            str.upper(frase[i])
            i=i+1
    return frase
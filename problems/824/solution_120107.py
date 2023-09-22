def uppCons(frase):
    '''Função que retorna a frase com as consoantes maiúsculas.
    str->str'''
    i = 0
    frase2 = ""
    while i < len(frase):
        if frase[i] not in 'aeiou':
            frase2 = str.upper(frase[i])
        else:
            frase2 = str.lower(frase[i])
        i =  i + 1
    return frase2
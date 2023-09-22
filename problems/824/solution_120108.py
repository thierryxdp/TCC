def uppCons(frase):
    '''Função que retorna a frase com as consoantes maiúsculas.
    str->str'''
    i = 0
    frase2 = ""
    while i < len(frase):
        if frase[i] not in 'aeiou':
            frase2 = frase[i].upper()
        else:
            frase2 = frase[i].lower()
        i =  i + 1
    return frase2
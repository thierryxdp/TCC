def uppCons(frase):
    '''função que retorna a frase com todas as suas consoantes
    em maiúsculas
    str -> str'''
    i = 0
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiou':
            frase[i] = str.upper(frase[i])
        i += 1
    return frase
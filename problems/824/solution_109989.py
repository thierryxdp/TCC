def uppCons(frase):
    '''função que retorna a frase com todas as suas consoantes
    em maiúsculas
    str -> str'''
    str.split(frase,'')
    i = 0
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiou':
            frase[i] = str.upper(frase[i])
        i += 1
    str.join(frase,'')
    return frase
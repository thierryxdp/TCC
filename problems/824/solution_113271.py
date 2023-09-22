def uppCons(frase):
    '''Dada uma frase retorna a mesma frase com todas as
    consoantes maiúculas.
    str -> str'''
    l_frase = list(frase)
    cont = 0
    while cont < len(l_frase):
        if l_frase[cont] in 'bcdfghjklmnpqrstvwxyzç':
            l_frase[cont] = str.upper(l_frase[cont])
        cont = cont + 1
    return str.join('',l_frase)
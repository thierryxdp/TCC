def uppCons(frase):
    '''Dada uma strig frase retorna a frase com as consoantes
    em maiúsculas.
    str -> str'''
    for minus, maius in zip((['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']),(['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z'])):
        frase.replace(minus,maius)
    return frase
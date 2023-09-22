def uppCons(frase):
    '''Função que recebe uma frase e retorna a frase com todas suas consoantes maiúsculas: str -> str'''
    i = 0
    while i < len(frase):
        if frase[i] not in 'bcdfghjklmpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            frase[i]
        i += 1
        if frase [i] in 'bcdfghjklmpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            frase == str.upper(frase[i])
        i += 1
    return frase
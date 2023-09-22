def uppCons(frase):
    '''Função que recebe uma frase e retorna a frase com todas suas consoantes maiúsculas: str -> str'''
    i = 0
    while i < len(frase):
        letra = frase[i]
        if letra in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
            frase = str.replace(frase,str(letra),str.upper(letra))
        i += 1
    return frase
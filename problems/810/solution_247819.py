def inverte(frase):
    '''Recebe uma frase e retorna essa frase invertida'''
    frase = str.lower(frase)
    frase1 = str.split(frase, ' ')
    frase_invertida = frase1[::-1]
    return frase_invertida
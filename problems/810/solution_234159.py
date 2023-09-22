def inverte(frase):
    """funcao que recebe uma frase e retorna as palavras da mesma frase em ordem inversa, minusculo, sem pontuacao
    str -> str"""
    
    frase = str.split(frase,)
    frase = list(frase[::-1])
    frase = str.join('',frase)
    frase = str.lower(frase)


    if '.' in frase:
        frase = frase.replace('.',' ')
    
    if '!' in frase:
        frase = frase.replace('!',' ')

    if '?' in frase:
        frase = frase.replace('?',' ')

    if '...' in frase:
        frase = frase.replace('...',' ')

    if '-' in frase:
        frase = frase.replace('-',' ')

    if ',' in frase:
        frase = frase.replace(',',' ')

    if ':' in frase:
        frase = frase.replace(':',' ')

    if ';' in frase:
        frase = frase.replace(';',' ')

    

    return frase
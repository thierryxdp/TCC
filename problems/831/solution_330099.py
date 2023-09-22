def lingua_p(palavra):
    '''
    '''
    palavra = palavra.lower()
    for letra in palavra:
        if letra in 'aeiou':
            palavra.replace(letra,(letra+'p'+letra))
    return palavra
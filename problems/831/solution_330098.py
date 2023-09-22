def lingua_p(palavra):
    '''
    '''
    palavra = palavra.lower()
    for letra in palavra:
        if letra in 'aeiou':
            index = palavra.index(letra)
            palavra[index] = palavra[index]+'p'+palavra[index]
    return palavra
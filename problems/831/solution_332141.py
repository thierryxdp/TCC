def lingua_p(palavra):
    '''Função que traduz uma frase para a lingua do "p" '''
    'str--->str'

    frase_modificada=''
    for letra in palavra:
        if letra in 'aeiou' :
            frase_modificada+=letra+'p'+letra
        else:
            frase_modificada+=letra

    return frase_modificada
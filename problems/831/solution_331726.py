def lingua_p(palavra):
    ''' '''
    traduzido=()
    for letra in palavra:
        if letra in 'aeiou':
            traduzido.append(letra+p+letra)
    return traduzido
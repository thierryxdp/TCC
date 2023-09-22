def lingua_p(palavra):
    ''' '''
    traduzido=''
    for letra in palavra:
        if letra in 'aeiouáéíóú':
            traduzido+=traduzido.append(letra+'p'+letra)
        else:
            traduzido+=traduzido.append(letra)
    return traduzido
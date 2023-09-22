def lingua_p(palavra):
    ''' '''
    traduzido=''
    for letra in palavra:
        if letra in 'aeiouáéíóú':
            traduzido.append(letra+'p'+letra)
        else:
            traduzido.append(letra)
    return traduzido
def lingua_p(palavra):
    ''' '''
    traduzido=[]
    for letra in palavra:
        if letra in 'aeiou':
            traduzido+=traduzido.append(letra+'p'+letra)
        else:
            traduzido+=traduzido.append(letra)
    return traduzido
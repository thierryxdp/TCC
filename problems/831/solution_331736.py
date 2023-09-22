def lingua_p(palavra):
    ''' '''
    traduzido=[]
    for letra in palavra:
        if letra in 'aeiou':
            traduzido+=traduzido.append(letra+'p'+letra)+letra
        else:
            traduzido+=traduzido.append(letra)+letra
    return traduzido
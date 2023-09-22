def lingua_p(palavra):
    ''' '''
    traduzido= ''
    for letra in palavra:
        if letra in 'aeiou':
            traduzido += letra+'p'+letra
        else:
            traduzido += letra
    return traduzido
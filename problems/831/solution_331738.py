def lingua_p(palavra):
    ''' '''
    traduzido=[]
    for letra in palavra:
        if letra in 'aeiou':
            traduzido+=traduzido.append(letra+'p'+letra)+palavra
        else:
            traduzido+=traduzido.append(letra)+palavra
    return traduzido
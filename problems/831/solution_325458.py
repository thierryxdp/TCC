def lingua_p(palavra):
    """ """
    saida = ''
    for i in palavra:
        saida =i
        if i == 'aeiouAEIOU':
            saida += 'p'
            saida +=i
    return saida